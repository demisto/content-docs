#!/usr/bin/env python3

import argparse
import dataclasses
import html
import json
import os
import re

import docspec
from pydoc_markdown import FilterProcessor, MarkdownRenderer, PydocMarkdown, PythonLoader, SmartProcessor
from pydoc_markdown.contrib.processors.sphinx import SphinxProcessor, generate_sections_markdown


@dataclasses.dataclass
class DemistoMarkdownRenderer(MarkdownRenderer):
    func_prefix: str | None = None
    module_overview: str | None = None

    # Overriding header levels from MarkdownRenderer to Function header to level 2
    header_level_by_type: dict[str, int] = dataclasses.field(
        default_factory=lambda: {
            "Module": 1,
            "Class": 2,
            "Method": 4,
            "Function": 2,
            "Variable": 4,  # v4 uses 'Variable' instead of 'Data'
            "Data": 4,  # keep for backwards compat
        }
    )

    def _format_function_signature(
        self, func: docspec.Function, override_name: str | None = None, add_method_bar: bool = True
    ) -> str:
        function_signature = super()._format_function_signature(func, override_name, add_method_bar)
        if self.func_prefix:
            function_signature = f"{self.func_prefix}{function_signature}"
        return function_signature

    def _render_signature_block(self, fp, obj):
        if "__init__" in obj.name:
            return
        super()._render_signature_block(fp, obj)

    def _render_header(self, fp, level, obj):
        if "__init__" in obj.name:
            return
        try:
            parent = obj.parent
        except (RuntimeError, AttributeError):
            parent = None
        parent_docstring = parent.docstring.content if (parent and parent.docstring) else ""
        if type(obj).__name__ in ("Data", "Variable") and "Enum" in parent_docstring:
            fp.write(f"- {obj.name}")
            fp.write("\n\n")
            return
        super()._render_header(fp, level, obj)

    def _render_object(self, fp, level, obj):
        if not isinstance(obj, docspec.Module) or self.render_module_header:
            self._render_header(fp, level, obj)
        url = self.source_linker.get_source_url(obj) if self.source_linker else None
        source_string = self.source_format.replace("{url}", str(url)) if url else None
        if source_string and self.source_position == "before signature":
            fp.write(source_string + "\n\n")
        self._render_signature_block(fp, obj)
        if source_string and self.source_position == "after signature":
            fp.write(source_string + "\n\n")
        # Skip module-level docstring — it is provided via module_overview in the article header
        if obj.docstring and not isinstance(obj, docspec.Module):
            # In v4, obj.docstring is a Docstring object with a .content attribute
            docstring_content = obj.docstring.content
            should_escape = self.escape_html_in_docstring and ">>>" not in docstring_content
            docstring = html.escape(docstring_content) if should_escape else docstring_content
            lines = docstring.split("\n")
            if self.docstrings_as_blockquote:
                lines = ["> " + x for x in lines]
            fp.write("\n".join(lines))
            fp.write("\n\n")


class CommonServerPythonProcessor(SphinxProcessor):
    def _process(self, node):
        if not node.docstring:
            return

        # In v4, node.docstring is a Docstring object; access content via .content
        docstring_content = node.docstring.content

        lines = []
        in_codeblock = False
        keyword = None
        components: dict[str, list[str]] = {}
        param_type = ""
        return_desc = ""

        for line in docstring_content.split("\n"):
            line = line.strip()

            if line.startswith("```"):
                in_codeblock = not in_codeblock

            line_codeblock = line.startswith("    ")

            if not in_codeblock and not line_codeblock:
                match = re.match(r"\s*:(?:type)\s+(\w+)\s*:(.*)?$", line)
                if match:
                    param_type = match.group(2).strip().replace("`", "")
                    continue

                match = re.match(r"\s*:(?:arg|argument|param|parameter)\s+(\w+)\s*:(.*)?$", line)
                if match:
                    keyword = "Arguments"
                    param = match.group(1)
                    text = match.group(2)
                    text = text.strip()

                    component = components.setdefault(keyword, [])
                    component.append(f"- `{param}` _{param_type}_: {text}")
                    continue

                match = re.match(r"\s*:(?:return|returns)\s*:(.*)?$", line)
                if match:
                    return_desc = match.group(1).strip()
                    continue

                match = re.match(r"\s*:(?:rtype)\s*:(.*)?$", line)
                if match:
                    keyword = "Returns"
                    return_type = match.group(1).strip().replace("`", "")
                    if "None" in return_type:
                        continue

                    component = components.setdefault(keyword, [])
                    component.append(f"- `{return_type}` - {return_desc}")
                    continue

                match = re.match("\\s*:(?:raises|raise)\\s+(\\w+)\\s*:(.*)?$", line)
                if match:
                    keyword = "Raises"
                    exception = match.group(1)
                    text = match.group(2)
                    text = text.strip()

                    component = components.setdefault(keyword, [])
                    component.append(f"- `{exception}`: {text}")
                    continue

            stripped_line = line.strip()
            if stripped_line.endswith("Examples:"):
                continue

            if stripped_line.startswith(">>>"):
                keyword = "Examples"

                component = components.setdefault(keyword, ["```python"])
                component.append(stripped_line)
                continue

            if keyword is not None:
                components[keyword].append(line)
            else:
                lines.append(line)

        if "Examples" in components:
            components["Examples"].append("```")
        generate_sections_markdown(lines, components)
        node.docstring.content = "\n".join(lines)


class IgnoreDocstringProcessor(FilterProcessor):
    def process(self, modules, _resolver):
        if not modules:
            return
        module = modules[0]
        kept = []
        for member in list(getattr(module, "members", [])):
            # In v4, member.docstring is a Docstring object; access content via .content
            docstring_content = member.docstring.content if member.docstring else None
            if docstring_content and "ignore docstring" not in docstring_content:
                kept.append(member)
            else:
                print(f"Skipping {member}")
        kept.sort(key=lambda obj: obj.name)
        # Mutate members in-place and re-sync parent weak-refs (v4 docspec requirement)
        module.members = kept
        module.sync_hierarchy()


def generate_pydoc(
    module: str,
    article_id: str,
    article_title: str,
    target_dir: str,
    module_overview: str,
    func_prefix: str | None = None,
) -> None:
    """
    Args:
         module (str): The Python module to parse and generate docs for.
         article_id (str): The article ID.
         article_title (str): The article title.
         target_dir (str): The target directory to generate docs at.
         func_prefix (str): Prefix to add to function signature.
         module_overview (str): Module overview to add to the doc header.

    Returns:
        None: No data returned.
    """
    pydocmd = PydocMarkdown()
    pydocmd.processors[0] = IgnoreDocstringProcessor()
    pydocmd.processors[1] = SmartProcessor(sphinx=CommonServerPythonProcessor())
    pydocmd.renderer = DemistoMarkdownRenderer(
        insert_header_anchors=False,
        func_prefix=func_prefix,
        module_overview=module_overview,
        escape_html_in_docstring=False,
        classdef_code_block=False,
        descriptive_class_title=False,
        signature_with_decorators=False,
        signature_class_prefix=True,
        render_module_header=False,
        format_code=False,
    )
    loader: PythonLoader = next((ldr for ldr in pydocmd.loaders if isinstance(ldr, PythonLoader)), None)
    loader.modules = [module]
    modules = pydocmd.load_modules()
    pydocmd.process(modules)

    pydoc = pydocmd.renderer.render_to_string(modules)

    article_description = f"API reference documentation for {article_title}."
    content = (
        f"---\nid: {article_id}\ntitle: {article_title}\ndescription: {article_description}\n---\n\n{module_overview}\n\n{pydoc}"
    )
    with open(f"{target_dir}/{article_id}.md", mode="w", encoding="utf-8") as f:
        f.write(content)


def generate_demisto_class_docs(target_dir: str):
    overview = """All Python integrations and scripts have available as part of the runtime the `demisto` class
object. The object exposes a series of API methods which are used to retrieve and send data to the Cortex XSOAR Server.

:::note
The `demisto` class is a low level API. For many operations we provide a simpler and more robust API as
part of the [Common Server Functions](https://xsoar.pan.dev/docs/integrations/code-conventions#common-server-functions).
:::"""
    generate_pydoc(
        module="demisto",
        article_id="demisto-class",
        article_title="Demisto Class",
        target_dir=target_dir,
        func_prefix="demisto.",
        module_overview=overview,
    )


def generate_common_server_python_docs(target_dir: str):
    overview = "Common functions that will be appended to the code of each integration/script before being executed."
    generate_pydoc(
        module="CommonServerPython",
        article_id="common-server-python",
        article_title="Common Server Python",
        target_dir=target_dir,
        module_overview=overview,
    )


def main():
    parser = argparse.ArgumentParser(
        description="Generate Content Python Docs", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-t", "--target_dir", help="Target directory to generate docs at.", required=True)
    args = parser.parse_args()
    target_sub_dir = f"{args.target_dir}/api"
    if not os.path.exists(target_sub_dir):
        os.makedirs(target_sub_dir)
    os.rename("demistomock.py", "demisto.py")
    generate_demisto_class_docs(target_sub_dir)
    os.rename("demisto.py", "demistomock.py")
    generate_common_server_python_docs(target_sub_dir)
    api_ref_path = f"{os.path.basename(args.target_dir)}/api"
    sidebar = {
        "type": "category",
        "label": "API Reference",
        "items": [
            f"{api_ref_path}/demisto-class",
            f"{api_ref_path}/common-server-python",
        ],
    }
    # IMPORTANT: if you add additional API items edit the reference index page at gendocs.py
    # See: https://github.com/demisto/content-docs/blob/5e58290cad5a70d7217264ad31dafe388dd5f5a9/content-repo/gendocs.py#L682
    with open(f"{args.target_dir}/sidebar.json", "r+") as f:
        data = json.load(f)
        rn_item_index = next(data.index(item) for item in data if item.get("label") == "Content Release Notes")
        data.insert(rn_item_index, sidebar)
        f.seek(0)
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    main()

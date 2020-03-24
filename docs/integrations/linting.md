---
id: linting
title: Linting
---

As part of the build process we run a few linters to catch common programming errors, stylistic errors and possible security issues. Linters are run only when working with the [package (directory) structure](package-dir).

All linters are run via the demisto-sdk:

```
demisto-sdk lint -h
Usage: demisto-sdk lint [OPTIONS]

Options:
  -h, --help                 Show this message and exit.
  -d, --dir TEXT             Specify directory of integration/script
  --no-pylint                Do NOT run pylint linter
  --no-mypy                  Do NOT run mypy static type checking
  --no-flake8                Do NOT run flake8 linter
  --no-bandit                Do NOT run bandit linter
  --no-test                  Do NOT test (skip pytest)
  -r, --root                 Run pytest container with root user
  -k, --keep-container       Keep the test container
  -v, --verbose              Verbose output - mainly for debugging purposes
  --cpu-num INTEGER          Number of CPUs to run pytest on (can set to
                             `auto` for automatic detection of the number of
                             CPUs)
  -p, --parallel             Run tests in parallel
  -m, --max-workers INTEGER  How many threads to run in parallel
  -g, --git                  Will run only on changed packages
  -a, --run-all-tests        Run lint on all directories in content repo
  --outfile TEXT             Save failing packages to a file

```

**Note**: this script is also used to run pytest. See: [Unit Testing](unit-testing)

An example of the result for running our lint checks on the HelloWorld package will look like: 
```buildoutcfg
➜  content git:(master) ✗ demisto-sdk lint -d Packs/HelloWorld/Integrations/HelloWorld
Detected python version: [3.7] for docker image: demisto/python3:3.7.4.2245
============ Starting process for: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/ ============


========= Running flake8 on: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py===============
flake8 completed for: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py

========= Running mypy on: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py ===============
Success: no issues found in 1 source file

mypy completed for: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py

========= Running bandit on: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py ===============
bandit completed for: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/HelloWorld.py

Detected python version: [3.7] for docker image: demisto/python3:3.7.4.2245
2020-03-06 16:11:29.678067: Using already existing docker image: devtestdemisto/python3:3.7.4.2245-4bbcae9c522cbe0aaa1818e29a66aae0

========== Running tests/pylint for: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/ =========
a9fd500285f9bb96ada38e3bb71de4e2316eed51190269224895208f6fa963a2



=============== Running pylint on files: HelloWorld.py ===============
Pylint completed with status code: 0

========= Running pytest ===============
collecting tests...
============================= test session starts ==============================
platform linux -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /devwork
plugins: xdist-1.31.0, asyncio-0.10.0, requests-mock-1.7.0, datadir-ng-1.1.1, mock-1.13.0, forked-1.1.3
collecting ... collected 2 items

HelloWorld_test.py::test_say_hello PASSED                                [ 50%]
HelloWorld_test.py::test_say_hello_over_http PASSED                      [100%]

=========================== 2 passed in 0.23 seconds ===========================
Pytest completed with status code: 0

============ Finished process for: /Users/rkozakish/dev/demisto/content/Packs/HelloWorld/Integrations/HelloWorld/  with docker: demisto/python3:3.7.4.2245 ============


******* SUCCESS PKGS: *******

	Packs/HelloWorld/Integrations/HelloWorld
```

## Flake8

This is a basic linter. It can be run without having all the dependencies available and will catch common errors. We also use this linter to enforce the standard python pep8 formatting style. On rare occasions you may encounter a need to disable an error/warning returned from this linter. Do this by adding an inline comment of the sort on the line you want to disable the error:

```python
#  noqa: <error-id>
```

For example:

```python
example = lambda: 'example'  # noqa: E731
```

When adding an inline comment always also include the error code you are disabling for. That way if there are other errors on the same line they will be reported.

More info: https://flake8.pycqa.org/en/latest/user/violations.html#in-line-ignoring-errors

## Pylint

This linter is similar to flake8 but is able to catch some additional errors. We run this linter with error reporting only. It requires access to dependent modules and thus we run it within a docker image similar with all dependencies (similar to how we run pytest unit tests). On rare occasions you may encounter a need to disable an error/warning returned from this linter. Do this by adding an inline comment of the sort on the line you want to disable the error:

```
# pylint: disable=<error-name>
```

For example:

```python
a, b = ... # pylint: disable=unbalanced-tuple-unpacking
```

Is is also possible to `disable` and then `enable` a block of code. For example (taken from CommonServerPython.py):

```python
# pylint: disable=undefined-variable
if IS_PY3:
    STRING_TYPES = (str, bytes)  # type: ignore
    STRING_OBJ_TYPES = (str)
else:
    STRING_TYPES = (str, unicode)  # type: ignore
    STRING_OBJ_TYPES = STRING_TYPES  # type: ignore
# pylint: enable=undefined-variable
```

**Note**: pylint can take both the error name and error code when doing inline comment disables. It is best to use the name which is clearer to understand.

More info: https://pylint.readthedocs.io/en/latest/user_guide/message-control.html

For classes that generate members dynamically (such as goolgeapi classes) pylint will generate multiple `no-member` errors as it won't be able to detect the members of the class. In this case it is best to add a `.pylintrc` file which will include the following:

```
[TYPECHECK]

ignored-classes=<Class Name List>
```

See following [example](https://github.com/demisto/content/blob/fe2bd5cddc6e521e08ef65fcd456a4214f8c4d93/Integrations/Gmail/.pylintrc)

## Mypy

Mypy uses type annotations to check code for common errors. It contains type information for many popular libraries (via [typeshed project](https://github.com/python/typeshed)). Additionally, it allows you to define type annotations for your own functions and data structures. Type annotations are fully supported as a language feature in python 3.6 and above. In earlier versions type annotations are provided via the use of comments.

We run mypy in a relatively aggressive mode so it type checks also functions which don't contain type definitions. This may sometimes cause extra errors. If you receive errors you can always ignore the line with an inline comment of:

```python
# type: ignore[<error-name>]
```

For example:

```python
a = 1
b = "2"
a = b  # type: ignore[assignment]
```

**Note**: mypy introduced the `ignore[<error-name>]` syntax only in version 0.730. See: [error code docs](https://mypy.readthedocs.io/en/latest/error_codes.html). You may see in the code ignores of the form: `type: ignore` without the `error-name`. This would usually be from old code written before the support for `error-name` ignores. We do not recommend using this ignore style as it ignores all errors and increases the risk of ignoring unexpected serious errors.

Dealing with **_Need type annotation errors_**: If you receive such an error instead of simply adding an `ignore` comment it is better to define the type of the variable which is missing type annotation. This error is usually received when an empty dict or list is defined and mypy can not infer the type of the object. In this case it is better to define the type as `dict` or `list`. For example python 2 code:

```python
my_list = []  # type: list
```

Or with python 3 annotations

```
my_list: list = []
```

If you know the type that the list will hold use the type constructor `List` that can specify also what type it holds. For example a list which we know that will hold strings in python 2 code:

```python
my_list = []  # type: List[str]
```

Or with python 3 annotations

```python
my_list: List[str] = []
```

**Note:** When using type constructors such as `List` or `Dict` there is need to import the type from the typing module in python 3. In python 2 as part of running mypy our wrapper script will include the typing module.

More info at: https://mypy.readthedocs.io/en/latest/index.html

## Bandit

[Bandit](https://github.com/PyCQA/bandit) is a tool designed to find common security issues in Python code.

We run `bandit` with a confidence level of HIGH. In the rare case that it reports a false positive, you can execlude the code by adding a comment of the sort: `# nosec`. See: https://github.com/PyCQA/bandit#exclusions .

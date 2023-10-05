---
id: images_in_documentation_files
title: Images in Documentation Files
---



Images in documentation markdown files are divided into 2 different types:
- Images that appear in integration/script/playbook readmes. These images only appear in https://xsoar.pan.dev/. They do not appear in the Cortex XSOAR/XSIAM product UI.
- Images that appear in pack readmes and integration description files. These images appear in both https://xsoar.pan.dev/ and in the Cortex XSOAR/XSIAM product UI. 

## Integration/Script/Playbook Readme Images

When creating markdown `README` documents for playbooks, integrations, or scripts that appear in https://xsoar.pan.dev/ only, you can use a relative or absolute URL.

### Relative Image URLs for Integration/Script/Playbook Readmes
You can use relative URLs  to documentation images stored in the `doc_files` or `doc_imgs` directories. To use relative URLs simply link the image using a relative path such as:
```
![Setup Account](./../../doc_files/create-account.png)
```

Make sure to view the `README.md` file in GitHub's web interface and validate that the images display properly.

**Documentation with Relative URL examples:**
* Google Calendar: https://github.com/demisto/content/blob/master/Packs/GoogleCalendar/Integrations/GoogleCalendar/README.md
* G Suite Admin: https://github.com/demisto/content/blob/master/Packs/GSuiteAdmin/Integrations/GSuiteAdmin/README.md

### Absolute Image URLs for Integration/Script/Playbook Readmes

To obtain an absolute URL to an image from GitHub:

* Commit the image and push to GitHub.
* View the file in the GitHub web interface. 
* Copy the URL from the `Download` button.
* Make sure the URL you are copying is not referring to a branch which will be deleted after the PR is merged. The URL should refer to a commit hash or the `master` branch.
* Note: if you click the `Download` button, GitHub will perform a redirect and the url in the browser will point to the domain: `raw.githubusercontent.com`. You may also use this URL as the absolute URL.


Embed the image in the README.md using a Markdown Image Link, such as:
```
![Playbook Image](https://github.com/demisto/content/raw/2d6e082cfb181f823e5b1446ae71e10537591ea6/Packs/AutoFocus/doc_files/AutoFocusPolling.png)
```
If you want more control on the image (for example setting width dimension) you can use the HTML `<img>` tag, such as:

```
<img width="500" src="https://github.com/demisto/content/raw/2d6e082cfb181f823e5b1446ae71e10537591ea6/Packs/AutoFocus/doc_files/AutoFocusPolling.png" />
```
**Screenshot of `Download` button:**
![Github Download](/doc_imgs/integrations/github-download-button.png)

**Absolute Image URL Examples:**
* URL to commit hash: https://github.com/demisto/content/raw/2d6e082cfb181f823e5b1446ae71e10537591ea6/Packs/AutoFocus/doc_files/AutoFocusPolling.png
* URL to `master` branch: https://github.com/demisto/content/raw/master/Packs/AutoFocus/doc_files/AutoFocusPolling.png
* URL after redirection (also valid): https://raw.githubusercontent.com/demisto/content/master/Packs/AutoFocus/doc_files/AutoFocusPolling.png

:::note
To keep our main Content repo small we limit images to 2MB. For larger images, follow the instructions for [Videos](#videos) on how to store large media files in our [content-assets](https://github.com/demisto/content-assets) repository. 
:::

## Pack Readmes and Integration Description Files Images

When creating a markdown pack `README` or an integration description file for XSOAR/XSIAM entities you must use an absolute URL.

To obtain an absolute URL to an image from GitHub:

* Commit the image and push to GitHub.
* View the file in the GitHub web interface. 
* Copy the URL from the `Download` button.
* Make sure the URL you are copying is not referring to a branch which will be deleted after the PR is merged. The URL should refer to a commit hash or the `master` branch.
* Note: if you click the `Download` button, GitHub will perform a redirect and the url in the browser will point to the domain: `raw.githubusercontent.com`. You may also use this URL as the absolute URL.


Embed the image in the README.md using a Markdown Image Link, such as:
```
![Playbook Image](https://github.com/demisto/content/raw/2d6e082cfb181f823e5b1446ae71e10537591ea6/Packs/AutoFocus/doc_files/AutoFocusPolling.png)
```

**Screenshot of `Download` button:**
![Github Download](/doc_imgs/integrations/github-download-button.png)

**Absolute Image URL Examples:**
* URL to commit hash: https://github.com/demisto/content/raw/2d6e082cfb181f823e5b1446ae71e10537591ea6/Packs/AutoFocus/doc_files/AutoFocusPolling.png
* URL to `master` branch: https://github.com/demisto/content/raw/master/Packs/AutoFocus/doc_files/AutoFocusPolling.png
* URL after redirection (also valid): https://raw.githubusercontent.com/demisto/content/master/Packs/AutoFocus/doc_files/AutoFocusPolling.png

:::note
To keep our main Content repo small we limit images to 2MB. For larger images, follow the instructions for [Videos](#videos) on how to store large media files in our [content-assets](https://github.com/demisto/content-assets) repository. 
:::
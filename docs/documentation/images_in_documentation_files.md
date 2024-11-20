---
id: images_in_documentation_files
title: Images in Documentation Files
---



Images in documentation markdown files are divided into 2 different types:
- Images that appear in integration/script/playbook readmes. These images only appear in https://xsoar.pan.dev/. They do not appear in the Cortex XSOAR/XSIAM product UI.
- Images that appear in pack readmes and integration description files. These images appear in both https://xsoar.pan.dev/ and in the Cortex XSOAR/XSIAM product UI.

## Instructions for uploading images to markdown files:


When creating markdown documentation files, you should use a relative path to the `doc_files` folder located in the pack's root path.

### Relative Image paths
You should use relative paths to documentation images stored in the `doc_files` directories. To use relative paths simply link the image using a relative path such as:
```
![Setup Account](./../../doc_files/create-account.png)
```

Make sure to view the image by clicking the path to ensure you've typed in the right path, and view the `README.md` file in GitHub's web interface and validate that the images display properly.

**Documentation with Relative path examples:**
* Google Calendar: https://github.com/demisto/content/blob/master/Packs/GoogleCalendar/Integrations/GoogleCalendar/README.md
* G Suite Admin: https://github.com/demisto/content/blob/master/Packs/GSuiteAdmin/Integrations/GSuiteAdmin/README.md

### Absolute URLs

Note that using absolute URLs is only relevant when dealing with larger file types (such as gif and mp4 files).
In that case, the file should be uploaded to `content-assets` repo.

For more information, refer to [large files absolute image urls](../documentation/readme_file#Large-Files).


---
id: docker
title: Using Docker
---
![](/doc_imgs/integrations/docker-for-beginners.png)
## What is Docker?
Docker is a tool used by developers to package together dependencies into a single container (or image). What this means for *you* is that in order to use your integration, you are not required to "pip install" all of the packages required. They are part of a container that "docks" to the server and contains all of the libraries you need. To learn more about Docker, visit their site [here](https://docs.docker.com/).
## Why Use Docker?
We use Docker to run Python scripts and integrations in a controlled environment. The scripts and integrations run isolated from the server to prevent them from accidentally damaging the server. By packaging libraries and dependencies together, we can prevent unknown issues from occurring since the environment is all the same.
## Script/Integration Configuration
Specifying which Docker image to use is done in the Cortex XSOAR IDE (under Settings -> Docker image name). If you don't specify a Docker image, a default Docker image using Python 2.7 is used. For new scripts and integrations, unless there is a specific reason to use Python 2 (for example to use a library unavailable in Python 3), we require using a Python 3 image.  
**Note:**  
Starting in Demisto 5.0, you can specify in the Cortex XSOAR IDE the Python version (2.7 or 3.x). Once you choose 3.x, the latest Cortex XSOAR Python 3 Docker image will be selected automatically.
The selected Docker image is configured in the script/integration YAML file under the `dockerimage` key. See the [YAML file overview](yaml-file).
## Update Docker Images Automatically via Pull Request
Every integration or script is updated automatically whenever a newer tag is available.
This happens via an automatic recurring job that updates the Docker image of the content item by a Pull Request in the content Git repository.
The pack is then distributed in the Marketplace.
### Disable Docker Image Automatic Update
You can cancel the automatic image updates by setting the `autoUpdateDockerImage` key to `false` in the YML file.
For example, the following will halt updates for the integration `MyIntegration`'s Docker image:
```yml
commonfields:
  id: MyIntegration
  version: -1
name: MyIntegration
display: MyIntegration
script:
 dockerimage: demisto/oauthlib:1.0.0.16907
autoUpdateDockerImage: false
```
## Docker Images
Palo Alto Networks maintains a large repository of Docker images. All Docker images are available via Docker hub under the Demisto organization [here](https://hub.docker.com/u/demisto/). The Docker image creation process is managed via the open source project [demisto/dockerfiles](https://github.com/demisto/dockerfiles). Before creating a new Docker image, check if there is one available already. You can search the [dockerfiles-info repository](https://github.com/demisto/dockerfiles-info/blob/master/README.md) which is updated nightly with image metadata and os/python packages used in the images.  
**Important:**  
- For security reasons, we cannot accept images which are not part of the Docker hub Palo Alto Networks (Demisto) organization.
- When modifying an existing Docker image, to ensure the change will not disrupt other integrations that use that same package, all Docker images are created with a unique immutable version tag that cannot be overriden.
  
If you cannot find an existing image, you can create a Docker image for testing and production use.
### Package Requirements
Before selecting a package to use in your integration, consider the following.
* Does this package have known security issues?
* Is the package licensed?
* If so, what type of license is used?
### Licensing
The Cortex XSOAR content repository is produced with an MIT (Massachusetts Institute of Technology) license, which means that we use only packages whose license is compatible with the MIT license. As a general rule of thumb, we only use `permissive` licenses. For a complete list of OSS licenses and their types see [this article]( https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses).  
**Note:**    
Other licenses may be permitted with specific approval.
### Security Concerns
It is imperative to perform due diligence on packages you choose to use. This includes verifying the package name is correct. In 2018 alone, a scan of PyPI resulted in the detection of 11 "typo-squatted" packages which were found to be malicious, as documented [here](https://medium.com/@bertusk/detecting-cyber-attacks-in-the-python-package-index-pypi-61ab2b585c67).
### Docker Image Creation
If you need to create a Docker image, first do due diligence and check the licenses.
### Docker File Repository (Required for Production)
In most cases, if your integration is for public release, you need to push Docker files into the dockerfiles repository located [here](https://github.com/demisto/dockerfiles). Pushing into this repository will add the image (after an approval process) to the Docker hub Demisto organization. See the [README](https://github.com/demisto/dockerfiles/blob/master/README.md) file for instructions.  

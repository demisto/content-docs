---
id: docker
title: Using Docker
---
![](/doc_imgs/integrations/docker-for-beginners.png)
## What is Docker?
Docker is a tool used by developers to package together dependencies into a single container (or image). What this means for *you* is that in order to use your integration, you are not required to "pip install" all of the packages required. They are part of a container that "docks" to the server and contains all of the libraries you need. To learn more about Docker, [visit their site here](https://docs.docker.com/)
## Why Use Docker?
Primarily we use Docker to run Python scripts and integrations in a controlled environment. They run isolated from the server to prevent someone from accidentally damaging the server. By packaging libraries and dependencies together, we can prevent unknown issues from occurring since the environment is all the same.
## Script/Integration Configuration
Specifying which Docker image to use is done in the Cortex XSOAR IDE (Open: Settings -> Docker image name). If you don't specify a Docker image, a default Docker image using Python 2.7 is used. For new scripts and integrations, unless there is a specific reason to use Python 2 (for example: a need to use a library which is not available for Python 3), we require using a Python 3 image.
**Note**: Starting in Demisto 5.0, you can specify in the Cortex XSOAR IDE the Python version (2.7 or 3.x). Once you choose 3.x, the latest Cortex XSOAR Python 3 Docker image will be selected automatically.
The selected Docker image is configured in the script/integration yaml file under the key: `dockerimage`. See: [Yaml File Overview](yaml-file).
## Update Docker Images Automatically via Pull Request
Every integration/script is updated automatically from time to time whenever a newer tag is available.
This happens via an automatic recurring job that updates the Docker image of the content item by a Pull Request in the content Git repository.
Finally, the pack is distributed in the Marketplace.
### Disable Docker Image Automatic Update
You can opt out of the automatic image updates by setting the `autoUpdateDockerImage` key to `false` in the YML file.
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
Palo Alto Networks maintains a large repository of Docker images. All Docker images are available via Docker hub under the Demisto organization: https://hub.docker.com/u/demisto/. The Docker image creation process is managed via the open source project [demisto/dockerfiles](https://github.com/demisto/dockerfiles). Before creating a new Docker image, check if there is one available already. You can search the [dockerfiles-info repository](https://github.com/demisto/dockerfiles-info/blob/master/README.md) which is updated nightly with image metadata and os/python packages used in the images.
**Important:** For security reasons, we cannot accept images which are not part of the Docker hub Palo Alto Networks (Demisto) organization.
If you cannot find an existing image, you can create a Docker image for testing and production use.
### Package Requirements
Before selecting a package to use in your integration, consider the following.
* Does this package have known security issues?
* Is the package licensed?
* If so, what type of license is used?
### Licensing
The Cortex XSOAR content repository is produced with an MIT (Massachusetts Institute of Technology) license, which means that we use only packages whose license is compatible with the MIT license. As a general rule of thumb, we only use `permissive` licenses. For a complete list of OSS licenses and their types see: https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses .
**Note:**  
Other licenses may be permitted with specific approval.
### Security Concerns
It is imperative to perform due diligence on packages we choose to use. This includes verifying the package name is correct. In 2018 alone, a scan of PyPI resulted in the detection of 11 "typo-squatted" packages which were found to be malicious. [[1]](https://medium.com/@bertusk/detecting-cyber-attacks-in-the-python-package-index-pypi-61ab2b585c67)
### Docker Image Creation
If you need to create a Docker image, proceed after having done due diligence and checking the licenses.
### Docker File Repository (Required for Production)
In most cases, if your integration is for public release, you need to push Docker files into the dockerfiles repository [located here](https://github.com/demisto/dockerfiles). Pushing into this repository will add the image (after an approval process) to the Docker hub Demisto organization. See [README.md](https://github.com/demisto/dockerfiles/blob/master/README.md) for instructions.
### Important Note
When modifying an existing Docker image, to ensure the change will not disrupt other integrations that use that same package, all Docker images are created with a unique immutable version tag cannot be overriden.
## Advanced: Server - Container Communication
The Cortex XSOAR server launches a Docker container by running a Python loop script. The server communicates with the Python loop script over stdout and stdin. The server passes the relevant integration/script code to the loop script. The script receives the code, executes it and returns a `completed` response to the server. While the integration/script code is executing, communication is performed over stdout/stdin. The server may then reuse the container to execute additional integrations/scripts that utilize the same Docker container. An simplified example loop script is available for review and testing: [here](https://github.com/demisto/content/blob/master/Utils/_script_docker_python_loop_example.py). For example, to use the example loop script to simulate runnning a simple script which sends a log entry to the server via calling: `demisto.log(...)` run the following:
```sh
echo '{"script": "demisto.log(\"this is an example entry log\")", "integration": false, "native": false}' | \
docker run --rm -i -v `pwd`:/work -w /work demisto/python3:3.8.6.12176 python Utils/_script_docker_python_loop_example.py
```

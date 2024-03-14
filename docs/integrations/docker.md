---
id: docker
title: Using Docker
---

![](/doc_imgs/integrations/docker-for-beginners.png)

## What is Docker?
Docker is a tool used by developers to package together dependencies into a single container (or image). What this means for *you* is that in order to use your integration, you are not required to "pip install" all of the packages required. They are part of a container that "docks" to the server and contains all of the libraries you need. To learn more about docker, [visit their site here](https://docs.docker.com/)

## Why Use Docker?
Primarily we use docker to run python scripts and integrations in a controlled environment. They run isolated from the server to prevent someone from accidentally damaging the server. By packaging libraries and dependencies together, we can prevent unknown issues from occurring since the environment is all the same.

## Script/Integration Configuration
Specifying which docker image to use is done in the Cortex XSOAR IDE (Open: Settings -> Docker image name). If you don't specify a docker image, a default docker image using Python 2.7 is used. For new scripts and integrations, unless there is a specific reason to use Python 2 (for example: a need to use a library which is not available for Python 3), we require using a Python 3 image. 

**Note**: Starting in Demisto 5.0, you can specify in the Cortex XSOAR IDE the Python version (2.7 or 3.x). Once you choose 3.x, the latest Cortex XSOAR Python 3 Docker image will be selected automatically.

The selected docker image is configured in the script/integration yaml file under the key: `dockerimage`. See: [Yaml File Overview](yaml-file).


## Updating Docker Image Automatically via Pull Request
Every integration/script is updated automatically from time to time whenever a newer tag is available.
This happens via an automatic reoccurring job that updates the docker image of the content item by a Pull Request in the content git repository.
Finally, the pack is distributed in the marketplace.

### Disabling Docker Image Automatic Update
If your want to opt out of the automatic image updates, you can do so by setting the `autoUpdateDockerImage`key to `false` in the YML file.
For example, the following will halt updates for the integration `MyIntegration`'s docker image:
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

Palo Alto Networks maintains a large repository of docker images. All docker images are available via docker hub under the Demisto organization: https://hub.docker.com/u/demisto/. Docker image creation process is managed via the open source project [demisto/dockerfiles](https://github.com/demisto/dockerfiles). Before trying to create a new docker image, check if there is one available already. You can search the [dockerfiles-info repository](https://github.com/demisto/dockerfiles-info/blob/master/README.md) which is updated nightly with image metadata and os/python packages used in the images.

**Important:** For security reasons, we cannot accept images which are not part of the docker hub Palo Alto Networks (Demisto) organization. 

If you can not find an existing image, follow through to read below on how to create a docker image for testing and production use.

## Package Requirements
We cannot just choose any package to be used in our integrations and there are many things to consider before we select a package. 
* Does this package have known security issues? 
* Is the package licensed? 
* If so, what type of license is being used?
These are just some of the many things we must take into consideration.

## Licensing
The Cortex XSOAR Content repository is produced with a (Massachusetts Institute of Technology) MIT license which means that we use only packages whose license is compatible with the MIT license. As a general rule of thumb, we only use `permissive` licenses. For a complete list of OSS licenses and their types see: https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses .

**Please Note:** Other licenses may be permitted with specific approval.

## Security Concerns
It is imperative that we perform due diligence on packages we choose to use. This includes verifying the package name is correct. Just in 2018 alone, a scan of PyPI resulted in the detection of 11 "typo-squatted" packages which were found to be malicious. [[1]](https://medium.com/@bertusk/detecting-cyber-attacks-in-the-python-package-index-pypi-61ab2b585c67)

## Docker Image Creation
So we have decided we now need to create a Docker Image. After having done our due diligence, and checked the licenses, we are now ready to proceed.

### Via Command Line (testing only)
To create a Docker Image you may use the Docker Create command in the war room by executing:
```
/docker_image_create
```

The below example shows the process:
 
 ```python
/docker_image_create name=example_name dependencies=mechanize packages=wget
```

This command is creating the docker image called "example_name" and uses the python dependency, Mechanize. You may also specify OS packages. This example requires wget as a package.

When the docker image is created, the following dialog box will appear. Once this has occurred, the docker image is ready to use.

![](/doc_imgs/integrations/docker-image-list-demisto.png)

This command accepts the following arguments:

| Argument  | Use  |
|---|---|
| **name**  | New docker image name, should be lower case only  |
| **dependencies**  |  New docker image dependencies, those are python libs like stix or requests, can have multiple as comma separated: lib1,lib2,lib3 |
| **packages**  |  new docker image packages, those are OS packages like libxslt or wget, can have multiple as comma separated: pkg1,pkg2,pkg3 |
| **base**         |  New docker image base image to use, it must be ubuntu based with python installed, the default will be demisto/python3-deb base image, with python 3.x |


You may need to update a Docker Image. Do this by executing the following:
```
/docker_image_update
```

This command accepts the following arguments:

| Argument | Use |
|---|---|
| **image** | Image name |
| **all** | Pull all images|

If you would like to see all available Docker Images, you may execute the following command:
```
/docker_images
```
This command does not accept any arguments and will list all available Docker Images.

### Via Docker Files (required for production)
In most cases, if your integration is for public release, we will need to push Docker Files into the dockerfiles repository [located here](https://github.com/demisto/dockerfiles). Pushing into this repository will add the image (after an approval process) to the docker hub Demisto organization. See [README.md](https://github.com/demisto/dockerfiles/blob/master/README.md) for instructions. 

## Important Notes
When modifying an existing Docker Image, we need to ensure the change will not disrupt other integrations that may use that same package. Thus, all docker images are created with a unique immutable version tag, which we don't allow overriding. 

## Advanced: Server - Container Communication
The XSOAR Server launches a docker container by running a python loop script. The Server communicates with the python loop script over stdout and stdin. The Server will pass the relevant integration/script code to the loop script. The script receives the code, executes it and returns a `completed` response to the Server. While the integration/script code is executing, communication is performed over stdout/stdin. The Server may then re-use the container to execute additional integrations/scripts that utilize the same docker container. An simplified example loop script is available for review and testing: [here](https://github.com/demisto/content/blob/master/Utils/_script_docker_python_loop_example.py). For example to use the example loop script to simulate runnning a simple script which sends a log entry to the Server via calling: `demisto.log(...)` run the following:
```sh
echo '{"script": "demisto.log(\"this is an example entry log\")", "integration": false, "native": false}' | \
docker run --rm -i -v `pwd`:/work -w /work demisto/python3:3.8.6.12176 python Utils/_script_docker_python_loop_example.py
```

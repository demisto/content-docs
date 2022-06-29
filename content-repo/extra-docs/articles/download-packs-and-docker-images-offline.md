---
id: download-packs-offline
title: Download Content Packs and Docker Images Offline
description: The download_packs_and_docker_images script enables you to download content packs and Docker images to your computer when working offline.
---


The **download_packs_and_docker_images** script enables offline users to download content packs and the content pack's latest Docker images to their computer and upload these packs and images to their Cortex XSOAR environment. 


To run the script, indicate which packs to download by entering the names of the packs exactly as they appear in https://xsoar.pan.dev/marketplace. If you enter an incorrect pack name, the script will display an error message and skip that pack. You can also enter a file that contains the names of the packs. 

The script downloads the content packs you want and the pack's Docker images as zip files to the output path you provide. If you do not provide a an output path, it will download the files to the folder from which you ran the script. You can then upload these packs and images to your Cortex XSOAR environment.


The **download_packs_and_docker_images.py** script is located in the *Utils* folder in the GIT Content repository. If you do not have access to the GIT Content repository, you can download the script from [here](https://raw.githubusercontent.com/demisto/content/master/Utils/download_packs_and_docker_images.py).

*Note: If the provided **download_packs_and_docker_images.py** script does not exactly fit your environment or needs, use the script as an example and edit it as needed.*


The following are the options for running the script:

| Options | Description | Required |
| ----- | ------| ----- |
| -h, --help | Displays a list of options and descriptions. | Optional |
| -p &lt;names of packs&gt;, --packs &lt;names of packs&gt; | Comma-separated list of pack names, or the name of the file that contains the pack names. The pack names must be as they appear in https://xsoar.pan.dev/marketplace. In the file that contains the pack names, each pack name must be on a new line. | Required |
| -o &lt;output path&gt;, --output_path &lt;output path&gt; | The path where the files will be downloaded to. | Optional |
| -sp, --skip_packs | Don't download packs. | Optional |
| -sd, --skip_docker | Don't download Docker images. | Optional |
| --insecure | Skip certificate validation. | Optional |

## Prerequisites
- Python 3.8 or above.
- Python Requests Library installed - Can be installed by running the ***pip install requests*** or ***pip3 install requests*** command.
- Need to have your content repository cloned on your machine.

If downloading Docker images:
- Docker Client installed
- Python Docker Library installed - Can be installed by running the ***pip install docker*** or ***pip3 install docker*** command.

## Download Content Packs and Docker Images

1. Ensure that all prerequisites are met.

2. Run the download script by typing the following with a comma-separated list of names of the packs to download:

   ***python3 &lt;path to the script&gt; -p &lt;name of the packs&gt;***

   For example:
***python3 ./Utils/download_packs_and_docker_images.py -p "AWS - IAM,Cybereason"***

3. Upload the Docker images.
   1. Expand the `docker.zip` file.
   2. Run the following command for each of the docker images:

      ***docker load -i &lt;path to the docker tar file&gt;***
      
      If using podman (Red Hat 8.x) use the following commmand:
      
      ***sudo su -s /bin/bash - demisto -c 'podman load -i &lt;FULL PATH TO YOUR DOCKER FILE&gt;.tar'***
      
      **Note:** make sure the tar file is located in a directory which the `demisto` user has read access both to the dir and file, such as /tmp.
      
      For example:
      
      ***sudo su -s /bin/bash  - demisto -c 'podman load -i /tmp/python3_3.9.8.24399.tar'***
      
4. Upload the content packs to your Cortex XSOAR environment.
   1. In your Cortex XSOAR environment, go to **Marketplace**.
   2. Click the 3 vertical dots and select **Upload Content**.
   3. Select the content zip files to upload.



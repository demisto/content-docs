---
id: tut-setup-env
title: Set Up Your Remote Dev Environment
---

This is a tutorial to set up a fully configured remote environment with VSCode [Dev Containers](https://code.visualstudio.com/docs/remote/containers)

## Requirements

### VSCode

1. Download and install from [here](https://code.visualstudio.com/download).
2. Install the [remote extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).


### Docker

**Windows**: Docker Desktop 2.0+ on Windows 10 Pro/Enterprise. Windows 10 Home (2004+) requires Docker Desktop 2.3+ and the WSL 2 back-end.
**macOS**: Docker Desktop 2.0+.
**Linux**: Docker CE/EE 18.06+ and Docker Compose 1.21+

Follow the instructions [here](https://code.visualstudio.com/docs/remote/containers#_installation) to install **docker** to your Operating System.

## Installation

### Option 1: Clone the GitHub repository locally

*Note*: **Windows** Users: To get improved performance, follow the instruction [here](https://docs.microsoft.com/en-us/windows/wsl/install) to install **WSL**, and clone the repository into the **WSL** filesystem.

In this way you will work on your local GitHub repository, but in a container environment. Every change in the local files will be changed in the container, and every change you make in the container will be changed locally.

#### Clone

You can clone with the terminal, and you can work directly with VSCode.
To work with Github in VSCode you can follow the instructions [here](https://code.visualstudio.com/docs/editor/github#_setting-up-a-repository)

### Open the folder in VSCode

If you cloned the repository with VSCode, you can skip this step.

1. Open VSCode.
2. Go to File -> Open Folder.
3. Select your GitHub repository.

#### Reopen in Container

1. Hit on this button on the bottom left corner.
2. Hit on **Reopen in Container**.
3. Wait for a few minutes until the Dev Container is ready.

### Option 2: Clone the GitHub fork repository a container volume

In this way we will clone the GitHub repository in a repository volume. The files will not be available locally, only from the container. This is the best option for performance.

#### Clone in a container

1. Open VSCode.
2. Hit on this button in the bottom left corner.
3. Hit on **Clone Repository in Container Volume**.
4. Wait for a few minutes until the Dev Container is ready.

## Usage





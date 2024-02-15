---
id: tut-setup-dev-remote
title: Set Up Your Remote Dev Environment
---

This is a tutorial to set up a fully configured remote environment with VSCode [Dev Containers](https://code.visualstudio.com/docs/remote/containers).

## Requirements

### VSCode

1. Download and install from [here](https://code.visualstudio.com/download).
2. Install the [remote extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).


### Docker

* **Windows**: Docker Desktop 2.0+ on Windows 10 Pro/Enterprise. Windows 10 Home (2004+) requires Docker Desktop 2.3+ and the WSL 2 back-end.
* **macOS**: Docker Desktop 2.0+.
* **Linux**: Docker CE/EE 18.06+ and Docker Compose 1.21+

Follow the instructions [here](https://code.visualstudio.com/docs/remote/containers#_installation) to install **Docker** to your operating system.

## Installation

### Windows Users

For better performance, use **WSL**.

* Follow the instructions [here](https://code.visualstudio.com/docs/remote/wsl#_installation) to get started with **WSL**.
* Follow the instructions [here](https://code.visualstudio.com/docs/remote/wsl#_open-a-remote-folder-or-workspace) to open **WSL** in VSCode.
* After installing **WSL**, [enable docker support on it](https://docs.docker.com/desktop/windows/wsl/#enabling-docker-support-in-wsl-2-distros).
* Make sure that `WSL 2` is installed with:
    ```bash
    wsl --list --verbose
    ```
    Make sure that the installed distribution is running `WSL 2`.

    To change versions, use the command:
    ```bash
    wsl --set-version <distro name> 2
    ```
    Replace `<distro name>` with the name of the Linux distribution that you want to update. For example, `wsl --set-version Ubuntu 2` will set your Ubuntu distribution to use `WSL 2`.


### Clone

You can clone the terminal, and you can work directly with VSCode.
To work with Github in VSCode, follow the instructions [here](https://code.visualstudio.com/docs/editor/github#_setting-up-a-repository).

### Open the repository in VSCode

If you cloned the repository with VSCode, you can skip this step.

1. Open VSCode.
2. Go to **File** > **Open Folder**.
3. Select your GitHub repository.

### Open the Dev Container

1. Click this green button:
    ![image](https://code.visualstudio.com/assets/docs/devcontainers/containers/remote-dev-status-bar.png)
2. Click **Reopen in Container**.
3. Wait a few minutes until the Dev Container is ready.

## Usage

The environment contains `demisto-sdk`, `zsh`, `git`, `pyenv`, `poetry`, preinstalled system and python dependencies, and recommended extensions, including [XSOAR VSCode extension](../concepts/vscode-extension.md)

Follow the [XSOAR VSCode extension](../concepts/vscode-extension.md) to get started with our features.

If you are not familiar with using `VSCode`, follow the [Getting Started](https://code.visualstudio.com/docs/introvideos/basics) guide.

## Using with MacOS or native Windows

As `Docker` is not native for **Mac** or in **Windows**, there could be performance issues.
If facing performance issues, try the following:

* If you're in **Windows**, [use WSL2](#windows).
* Update your `Docker`.
* Disable `Autosave` in the `VSCode`.

## Troubleshooting

If there are errors in [opening the dev container](#open-the-dev-container), try the following:

* Update your `Docker`.
* Clean up your `Docker`: 
```bash
  docker system prune -a --volumes
```

---
id: tut-setup-dev-codespace
title: Set Up Your GitHub Codespace Environment
---

This tutorial provides a step-by-step instructions for setting up a personal Codespace for developing Cortex XSOAR content.

## What are GitHub Codespaces?
[GitHub Codespaces](https://github.com/features/codespaces) are cloud-based development environments provided by [GitHub](https://github.com) that allow you to set up remote environments with preinstalled and preconfigured tools and dependencies 
using a [dev container](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).

Your Codespace environment will be hosted on GitHub's servers (attached to your GitHub account),
and will allow you to access your Codespace from any computer, continuing your work from where you left off.

### Cost and Limitations
GitHub offers a free quota for Codespaces (which is higher for GitHub Pro users) that you can utilize for developing Cortex XSOAR content.  

The quota is calculated based on the number of hours your Codespace is actively running.
You can see the free quota plan and additional information [here](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts).  

:::info
Codespaces generated from the Content repository (or a fork of it) are configured to have 4 cores by default.
:::

:::tip
You will receive an automated email notification when you have used 75%, 90%, and 100% of your freely-included quotas.

You can find information about your Codespaces quota usage on the settings under "Billing and plans".  
See the following GitHub article for a step-by-step guide: [Viewing your GitHub Codespaces usage](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/viewing-your-github-codespaces-usage).
:::

If you want to use paid usage once you've reached your free quota, you can find information about the pricing [here](https://docs.github.com/en/billing/managing-billing-for-github-codespaces/about-billing-for-github-codespaces#pricing-for-paid-usage).

## Requirements
A GitHub account (can be created [here](https://github.com/signup)).

## Setup
The following instructions are for an initial setup that needs to be done only once.  
After that, the generated environment will be kept in your GitHub account.

### Create a New Codespace
1. [Log in to your GitHub account](https://github.com/login) (if not already logged in).
2. Enter the [XSOAR Content repository](https://github.com/demisto/content).
3. Fork the repository to your account (see example GIF below):
   1. Click **Fork** at the top right.
   2. Select your account as the owner, and leave the repository name as is.
   3. Keep the **Copy the master branch only** option selected.
   4. Click **Create fork**.
4. Wait a few seconds for the fork to be created. You will be redirected to your forked repository page.
5. Create a new branch on your fork, and give it a meaningful name.
6. Click **Code**, go to the **Codespaces** tab, and click **Create Codespace on \<branch name\>** (see example GIF below).
7. A page saying "This Codespace is requesting additional permissions" might appear.  
    If it does, click **Continue without authorizing**.
8. Click **New Codespace** (this might take a few minutes).

#### Examples
![Creating a new fork](../doc_imgs/contributing/content-new-fork.gif)
*Creating a new fork*

![Creating a new Codespace](../doc_imgs/tutorials/tut-setup-dev-codespace/create-a-new-codespace.gif)
*Creating a new Codespace*


### Connect to Your Codespace
#### Browser-based Visual Studio Code
By default, GitHub provides a browser-based Visual Studio Code editor that's automatically configured, authenticated, and connected to your Codespace, using your GitHub account.  
This IDE should be sufficient for most use cases.

To open it, enter the main forked repository page, click **Code**, go to the **Codespaces** tab,
and click the newly created Codespace (should have a random name).

It can take up to a few minutes for the Codespace to be fully initialized.  
This is a one-time process that's done only at the first time you open a Codespace.

Once the initialization is completed and your Codespace is ready, you will be redirected to the IDE, where you can start your development.

![Connecting to the Codespace (browser)](../doc_imgs/tutorials/tut-setup-dev-codespace/open-codespace-in-browser.gif)
*Connecting to the Codespace (browser)*

#### Visual Studio Code (local)
In order to connect to your Codespace from a local Visual Studio Code editor, you will need to install the official [GitHub Codespaces extension](https://marketplace.visualstudio.com/items?itemName=GitHub.Codespaces).

For a complete installation & configuration tutorial, refer to the official "[Using GitHub Codespaces in your local development environment](https://docs.github.com/en/codespaces/developing-in-codespaces/using-github-codespaces-in-visual-studio-code)" article by GitHub.  
(You can skip the "Creating a Codespace in VS Code" section, as we've already created a Codespace.)

#### Using JetBrains IDEs (PyCharm, IntelliJ IDEA, etc.) (local)
In order to connect to your Codespace from a JetBrains IDE, you will need to install and configure [JetBrains Gateway](https://www.jetbrains.com/remote-development/gateway).

For a complete installation & configuration tutorial, refer to the official "[Using GitHub Codespaces in your JetBrains IDE](https://docs.github.com/en/codespaces/developing-in-codespaces/using-github-codespaces-in-your-jetbrains-ide)" article by GitHub.

## Development
After your IDE is connected to your Codespace, you can start developing your content as you normally would.

The environment comes pre-installed with all the required tools and dependencies for developing Cortex XSOAR content, including.  
Configure SSH keys or any other credentials is also not required, as the Codespace is already authenticated using your GitHub account.

## Additional Resources
For additional documentation about GitHub Codespaces, see the official [GitHub Codespaces documentation](https://docs.github.com/en/codespaces).

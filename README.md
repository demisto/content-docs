![Content logo](demisto_content_logo.png)

[![Netlify Status](https://api.netlify.com/api/v1/badges/7f059c11-2192-4c11-8578-a15b32db377d/deploy-status)](https://app.netlify.com/sites/demisto-content-docs/deploys)
[![Language grade: JavaScript](https://img.shields.io/lgtm/grade/javascript/g/demisto/content-docs.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/demisto/content-docs/context:javascript) 
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/demisto/content-docs.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/demisto/content-docs/context:python)

# Cortex XSOAR Content Developer Docs
This repo holds Cortex XSOAR Content Developer Docs. The Content Developer Docs provide information on how to develop and contribute content to the Cortex XSOAR platform. The actual content is hosted at the following repo: https://github.com/demisto/content. 

This website is built using [Docusaurus 2](https://v2.docusaurus.io/), a modern static website generator.

You can access the generated website at: https://xsoar.pan.dev/ 

## Running the site locally
### Node Setup
We use node 12.x for running the project. It is recommended to use `nvm`. See: https://github.com/nvm-sh/nvm for install instructions. It is recommended to setup `auto use` as specified here: https://github.com/nvm-sh/nvm#calling-nvm-use-automatically-in-a-directory-with-a-nvmrc-file . The root dir of the project contains a proper `.nvmrc` file with the recommended version to use.

### Install and Start
Install all dependencies:
```
npm install
```
Start the development server on: http://localhost:3000
```
npm start
```
Start writing docs...

## Generating Reference Docs
Reference docs are generated from the [Cortex XSOAR Content repository](https://github.com/demisto/content). If you are working on general site docs which are not reference docs from the Content repo, you don't need to run this step to preview your docs.

To generate the docs we use [pipenv](https://github.com/pypa/pipenv). Make sure to install pipenv by running: `pip3 install pipenv`.

When working locally you can generate the reference docs by running:
```
npm run reference-docs
```
This task will checkout the content repository and generate the docs. The generated docs are ignored by `.gitignore` and shouldn't be checked in as they are generated during the build.

When generating the docs the `master` branch of the `content` repo will be used unless there is a matching branch with the same name as the current branch of `content-docs`, that branch will be used. 

If you have the `content` repo checked out locally and you want to use it for generating the reference docs (for example when working on a Content Integration Doc), you can set the path to your `content` repo dir with the environment variable: `CONTENT_REPO_DIR`. For example:
```
 CONTENT_REPO_DIR=~/dev/demisto/content npm run reference-docs
```

### Generation Code
Code used for generating content reference docs is written in Python and resides in the `content-repo` folder. To set up a development environment we use [pipenv](https://github.com/pypa/pipenv). Make sure to install pipenv by running: `pip3 install pipenv`. Setup a proper Python env by running:
```
pipenv install --dev
```
To run linting and unit tests you can use npm:
```
npm run test
```
Linting and unit tests are run on each commit using Github Actions. They are required to pass in-order to merge PRs.

## Build

```
$ npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## Contributing
Contributions are welcome and appreciated. If you find a bug or have suggestions for improvements, feel free to open an [Issue](https://github.com/demisto/content-docs/issues) or (better yet) submit a [Pull Request](https://github.com/demisto/content-docs/pulls). 

Before merging any PRs, we need all contributors to sign a contributor license agreement. By signing a contributor license agreement, we ensure that the community is free to use your contributions.

When you open a new pull request, a bot will evaluate whether you have signed the CLA. If required, the bot will comment on the pull request, including a link to accept the agreement. The CLA document is also available for review as a [PDF](https://github.com/demisto/content/blob/master/docs/cla.pdf).

If the `license/cla` status check remains on *Pending*, even though all contributors have accepted the CLA, you can recheck the CLA status by visiting the following link (replace **[PRID]** with the ID of your PR): https://cla-assistant.io/check/demisto/content-docs?pullRequest=[PRID] .


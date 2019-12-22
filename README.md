![Content logo](demisto_content_logo.png)

# Demisto Content Developer Docs
This repo holds Demisto's Content Developer Docs. The Content Developer Docs provide information on how to develop Content for the Demisto platform. The actual content is hosted at the following repo: https://github.com/demisto/content. 

This website is built using [Docusaurus 2](https://v2.docusaurus.io/), a modern static website generator.

You can access the generated website at: https://demisto.pan.dev/ 

## Running the site locally
### Node Setup
We use node 10.15.x for running the project. It is recommended to use `nvm`. See: https://github.com/nvm-sh/nvm for install instructions. It is recommended to setup `auto use` as specified here: https://github.com/nvm-sh/nvm#calling-nvm-use-automatically-in-a-directory-with-a-nvmrc-file . The root dir of the project contains a proper `.nvmrc` file with the recommended version to use.

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

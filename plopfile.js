const config = (plop) => {
  plop.setGenerator("details", {
    description: "Generate marketplace details page",
    prompts: [
      {
        type: "input",
        name: "id",
        message: "Pack ID",
      },
      {
        type: "input",
        name: "name",
        message: "Pack Name",
      },
      {
        type: "input",
        name: "description",
        message: "Pack Description",
      },
      {
        type: "input",
        name: "author",
        message: "Pack Author",
      },
      {
        type: "input",
        name: "currentVersion",
        message: "Pack Current Version",
      },
      {
        type: "input",
        name: "versionInfo",
        message: "Pack Version Info",
      },
      {
        type: "input",
        name: "authorImage",
        message: "Pack Author Image",
      },
      {
        type: "list",
        name: "videos",
        message: "Pack Videos",
      },
      {
        type: "input",
        name: "readme",
        message: "Pack README",
      },
      {
        type: "input",
        name: "support",
        message: "Pack Support",
      },
      {
        type: "input",
        name: "created",
        message: "Pack created date",
      },
      {
        type: "input",
        name: "updated",
        message: "Pack updated date",
      },
      {
        type: "input",
        name: "certification",
        message: "Pack certification",
      },
      {
        type: "list",
        name: "useCases",
        message: "Pack use cases",
      },
      {
        type: "list",
        name: "integrations",
        message: "Pack integrations",
      },
      {
        type: "list",
        name: "contentItems",
        message: "Pack content items",
      },
      {
        type: "input",
        name: "changeLog",
        message: "Pack changelog",
      },
      {
        type: "input",
        name: "licenseLink",
        message: "Pack license information",
      },
      {
        type: "input",
        name: "premium",
        message: "If Premium Pack",
      },
      {
        type: "list",
        name: "dependencies",
        message: "Pack dependencies",
      },
    ],
    actions: [
      {
        type: "add",
        path: "src/pages/marketplace/details/{{id}}/index.js",
        templateFile: "templates/details.hbs",
        force: true,
      },
    ],
  });
};

module.exports = config;

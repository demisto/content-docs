const fs = require('fs-extra');

const sidebars =  {  
  docs: [
      {
        type: "category",
        label: "Basics",
        items: [
          "getting-started-guide",
          "faq"
        ]
      },
      {
        type: "category",
        label: "Design",
        items: [
          "use-cases",
          "design-best-practices"
        ]
      }, 
      {
        type: "category",
        label: "Tutorials",
        items: [
          "tutorial-setup-dev",
          "tutorial"
        ]
      },           
      {
        type: "category",
        label: "Writing an integration",
        items: [
          "dev-setup",
          "code-conventions",
          "package-dir",
          "docker",          
          "yaml-file",
          "parameter-types",
          "fetching-incidents",
          "fetching-credentials",
          "long-running", 
          "dbot",
          "context-and-outputs",
          "context-standards",
          "dt"
        ]
      },
      {
        type: "category",
        label: "Writing Playbooks",
        items: [
          "playbooks",
          "playbook-conventions",
          "generic-polling"        
        ]
      },         
      {
        type: "category",
        label: "Testing",
        items: [
          "linting",
          "unit-testing",
          "testing",
          "circleci",
          "debugging"
        ]
      }, 
      {
        type: "category",
        label: "Documentation",
        items: [
          "integration-docs",
          "doc-structure",
          "changelog"
        ]
      }
    ]
};

if (fs.existsSync("docs/reference/sidebar.json")) {
  referenceSideBar = fs.readJSONSync("docs/reference/sidebar.json")
  sidebars["reference"] = referenceSideBar
}

module.exports = sidebars;
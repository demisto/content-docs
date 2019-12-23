module.exports = {
  docs: [
    {
      type: "category",
      label: "Development Guide",
      items: [
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
          label: "Basics",
          items: [
            "getting-started-guide",
            "tutorial",
          ]
        },
        {
          type: "category",
          label: "Writing an integration",
          items: [
            "dev-setup",
            "package-dir",
            "yaml-file",
            "parameter-types",
            "code-conventions",   
            "fetching-incidents",
            "fetching-credentials",
            "long-running", 
            "dbot",
            "context-and-outputs",
            "context-standards",
            "dt",
            "docker"
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
    }
  ]
};

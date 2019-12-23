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
          label: "Getting Started",
          items: [
            "dev-guide",
            "faq",
            "why-demisto",
            "tutorial",
            "package-dir"
          ]
        },
        {
          type: "category",
          label: "Writing an integration",
          items: [
            "dev-setup",
            "docker",
            "code-conventions",   
            "parameter-types",
            "fetching-incidents",
            "fetching-credentials",
            "long-running", 
            "context-and-outputs",
            "dbot",
            "dt",
            "context-standards",
            "yaml-file"                        
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
            "testing",
            "unit-testing",        
            "circleci",
            "debugging"
          ]
        }, 
        {
          type: "category",
          label: "Documentation",
          items: [
            "changelog",
            "integration-docs",
            "doc-structure"
          ]
        }
      ]
    }
  ]
};

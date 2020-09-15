const fs = require('fs-extra');

const sidebars = {
  docs:
  [
    {
        type: "doc",
        id: "welcome"
    },
    {
      type: "category",
      label: "Getting Started",
      collapsed: false,
      items: [
        {
          type: "doc",
          id: "integrations/getting-started-guide"    
        },
        {
          type: "doc",
          id: "concepts/concepts"    
        },
        {
          type: "doc",
          id: "concepts/use-cases"
        },
        {
          type: "doc",
          id: "concepts/design-best-practices"
        },
        {
          type: "category",
          label: "Dev Environment",
          collapsed: true,
          items: [
            "integrations/dev-setup",        
            "integrations/xsoar-ide",
            "integrations/pycharm-plugin"
          ]
        },        
        {
          type: "doc",
          id: "concepts/faq"
        },          
      ]
    },
    {
      type: "category",
      label: "Contributing",
      collapsed: true,
      items: [
        "contributing/checklist",
        "contributing/marketplace"
      ]
    },    
     {
      type: "category",
      label: "Content Packs",
      collapsed: true,
      items: [
        "integrations/packs-format",  
        "integrations/pack-docs",
        "integrations/release-notes",
        "integrations/premium_packs"
      ]
    },
    {
      type: "category",
      label: "Integrations & Scripts",
      collapsed: true,
      items: [
        {
          type: "category",
          label: "Integration components",
          collapsed: true,          
          items: [
            "integrations/package-dir",
            "integrations/yaml-file",
            "integrations/parameter-types",
            "integrations/integration-logo"
          ]
        },
        {       
          type: "category",
          label: "Developing",
          collapsed: true,          
          items: [
            "integrations/code-conventions",
            "integrations/fetching-incidents",
            "integrations/context-and-outputs",
            "integrations/context-standards",
            "integrations/dbot"
          ]
        },        
        {       
          type: "category",
          label: "Testing",
          collapsed: true,          
          items: [
            "integrations/linting",
            "integrations/unit-testing",
            "integrations/test-playbooks",
            "integrations/debugging",
          ]
        }, 
        {
          type: "doc",
          id: "integrations/integration-docs"
        },
        {       
          type: "category",
          label: "Advanced Topics",
          collapsed: true,          
          items: [
            "integrations/feeds",
            "integrations/powershell-code",
            "integrations/fetching-credentials",
            "integrations/long-running",
            "integrations/dt",
            "integrations/integration-cache",
            "integrations/mirroring_integration",
            "integrations/openapi-codegen",
            "integrations/docker"      
          ]
        }
      ]
    },
    {
      type: "category",
      label: "Playbooks",
      collapsed: true,
      items: [
        "playbooks/playbooks-overview",
        "playbooks/playbook-contributions",
        "playbooks/playbooks",
        "playbooks/playbook-settings",
        "playbooks/playbook-conventions",
        "playbooks/playbooks-inputs-outputs",
        "playbooks/playbooks-extend-context",
        "playbooks/playbooks-create-playbook-task",
        "playbooks/playbooks-create-conditional-task",
        "playbooks/playbooks-communication-task-concepts",
        "playbooks/playbooks-create-communication-task",
        "playbooks/playbooks-communication-task-customize-message",
        "playbooks/generic-polling",
        "playbooks/playbooks-field-reference"
      ]
    },
    {
      type: "category",
      label: "Incidents, Fields & Layouts",
      collapsed: true,
      items: [
        "incidents/incident-xsoar-incident-lifecycle",
        "incidents/incident-types",
        "incidents/incident-customize-incident-layout",
        "incidents/incident-fields",
        "incidents/incident-jobs",
        "incidents/incident-auto-extract",
        "incidents/incident-classification-mapping",
        "incidents/incident-pre-processing"
      ]
    },
    {
      type: "category",
      label: "Tutorials",
      collapsed: false,
      items: [
            "tutorials/tut-setup-dev",
            "tutorials/tut-integration-ui"            
        ]
    },
    {
      type: "doc",
      id: "privacy"
    },
  ],
  partners:
  [
    {
      type: "category",
      label: "Partners",
      collapsed: false,
      items: [
        "partners/why-xsoar",
        "partners/become-a-tech-partner",
        "partners/marketplace",
        "partners/certification",
        "partners/office-hours",
        "partners/development-partners"
      ],
    },
  ],
};

if (fs.existsSync("docs/reference/sidebar.json")) {
  referenceSideBar = fs.readJSONSync("docs/reference/sidebar.json")
  sidebars["reference"] = referenceSideBar
}

module.exports = sidebars;

module.exports = {
  concepts: 
  [
      {
        type: "doc",
        id: "concepts"
      },
      {
        type: "doc",
        id: "concepts/overview",
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
        type: "doc",
        id: "concepts/faq"
      }, 
  ],
  howtos: [
    {
      type: "doc",
      id: "howtos"
    },{
      type: "category",
      label: "Integrations",
      items: [
        {
          type: "category",
          label: "Coding",
          items: [
            "howtos/code-conventions",
            "howtos/package-dir",
            "howtos/yaml-file",
            "howtos/parameter-types",
            "howtos/fetching-incidents",
            "howtos/fetching-credentials",
            "howtos/long-running", 
            "howtos/dbot",
            "howtos/context-and-outputs",
            "howtos/context-standards",
            "howtos/dt"
          ]
        },
        {
          type: "category",          
          label: "Testing",
          items: [
            "howtos/package-dir",
            "howtos/docker",          
            "howtos/linting",
            "howtos/unit-testing",
            "howtos/testing",
            "howtos/circleci",
            "howtos/debugging"
          ],
        },
        {
          type: "category",          
          label: "Documenting",
          items: [
            "howtos/integration-docs",
            "howtos/doc-structure",
            "howtos/changelog"     
          ],
        }
      ]
    },
    {
      type: "category",
      label: "Playbooks",
      items: [
        "howtos/playbooks",
        "howtos/playbook-conventions",
        "howtos/generic-polling"   
      ]
    },
    {
      type: "category",
      label: "Scripts",
      items: [
        "howtos/code-conventions",
      ]
    },
    {
      type: "category",
      label: "Incidents, Fields & Layouts",
      items: [
        "howtos"
      ]
    },
    {
      type: "category",
      label: "Dashboard and Widgets",
      items: [
        "howtos"
      ]
    },
    {
      type: "category",
      label: "Contribution Process",
      items: [
        "howtos",
      ]
    },
  ],
  tutorials: [
    {
      type: "doc",
      id: "tutorials"
    },
    {
      type: "category",
      label: "Getting Started",
      items: [
        "tutorials/getting-started/tut-setup-dev",
      ]
    },
    {
      type: "category",
      label: "Integrations",
      items: [
        "tutorials/integrations/tut-integration-ui"
      ]
    },  
    {
      type: "category",
      label: "Playbooks",
      items: [
        "tutorials/playbooks/tut-playbooks"
      ]
    },
    {
      type: "category",
      label: "Scripts",
      items: [
        "tutorials/scripts/tut-scripts"
      ]
    },
    {
      type: "category",
      label: "Incidents, Fields & Layouts",
      items: [
        "tutorials/incidents/tut-incidents"      ]
    },
    {
      type: "category",
      label: "Dashboard and Widgets",
      items: [
        "tutorials/dashboards/tut-dashboards"
      ]
    },
  ],
  references: 
  [
    {
      type: "doc",
      id: "reference"
    },
    {
      type: "category",
      label: "Integrations",
      items: [
        "reference/integrations/ref-integrations",
      ]
    },
    {
      type: "category",
      label: "Playbooks",
      items: [
        "reference/playbooks/ref-playbooks",
      ]
    },
    {
      type: "category",
      label: "Scripts",
      items: [
        "reference/scripts/ref-scripts",
      ]
    },  
    {
      type: "category",
      label: "Code",
      items: [
        "reference/code/ref-code",
      ]
    },     
    {
      type: "category",
      label: "Demisto SDK",
      items: [
        "reference/demisto-sdk/ref-demisto-sdk",
      ]
    },     
  ]
};
module.exports = {
  concepts: 
  [
      {
        type: "doc",
        id: "concepts"
      },
      {
        type: "category",
        label: "Overview",
        items: [
          "concepts/concept",
        ]
      },
      {
        type: "category",
        label: "Architecture",
        items: [
          "concepts/concept",
        ]
      },
      {
        type: "category",
        label: "Use Cases",
        items: [
          "concepts/use-cases"
        ]
      },
      {
        type: "category",
        label: "Design",
        items: [
          "concepts/design-best-practices"
        ]
      }, 
      {
        type: "category",
        label: "Dev Environment & SDK",
        items: [
          "concepts/concept",
        ]
      }, 
      {
        type: "category",
        label: "Best Practices",
        items: [
          "concepts/design-best-practices",
        ]
      }
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
        "tutorials/tutorial-setup-dev",
      ]
    },
    {
      type: "category",
      label: "Integrations",
      items: [
        "tutorials/tutorial"
      ]
    },  
    {
      type: "category",
      label: "Playbooks",
      items: [
        "tutorials/tutorial"
      ]
    },
    {
      type: "category",
      label: "Scripts",
      items: [
        "tutorials/tutorial"
      ]
    },
    {
      type: "category",
      label: "Incidents, Fields & Layouts",
      items: [
        "tutorials/tutorial"      ]
    },
    {
      type: "category",
      label: "Dashboard and Widgets",
      items: [
        "tutorials/tutorial"
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
        "reference/faq",
      ]
    },
    {
      type: "category",
      label: "Playbooks",
      items: [
        "reference/faq",
      ]
    },
    {
      type: "category",
      label: "Scripts",
      items: [
        "reference/faq",
      ]
    },  
    {
      type: "category",
      label: "Helper Functions",
      items: [
        "reference/faq",
      ]
    },     
    {
      type: "category",
      label: "Demisto SDK",
      items: [
        "reference/faq",
      ]
    },     
  ]
};
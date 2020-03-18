module.exports = {
  docs:
  [
    {
      type: "doc",
      id: "welcome"
    },
    {
      type: "category",
      label: "Concepts",
      items: [
          {
            type: "doc",
            id: "concepts"
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
    },
    {
      type: "category",
      label: "How-Tos",
      items: [
        {
          type: "doc",
          id: "howtos"
        },
        {
          type: "category",
          label: "Getting Started",
          items: [
            "howtos/integrations/getting-started-guide",
            "howtos/integrations/dev-setup",
            "howtos/integrations/packs-format",
            "howtos/integrations/package-dir",
            "howtos/integrations/docker",
          ]
        },
        {
          type: "category",
          label: "Integrations",
          items: [
            {
              type: "category",
              label: "Developing",
              items: [
                "howtos/integrations/code-conventions",
                "howtos/integrations/yaml-file",
                "howtos/integrations/integration-logo",
                "howtos/integrations/parameter-types",
                "howtos/integrations/fetching-incidents",
                "howtos/integrations/feeds",
                "howtos/integrations/fetching-credentials",
                "howtos/integrations/long-running",
                "howtos/integrations/context-and-outputs",
                "howtos/integrations/context-standards",
                "howtos/integrations/dbot",
                "howtos/integrations/dt",
                "howtos/integrations/integration-cache",
              ]
            },
            {
              type: "category",
              label: "Testing",
              items: [
                "howtos/integrations/linting",
                "howtos/integrations/unit-testing",
                "howtos/integrations/test-playbooks",
                "howtos/integrations/debugging"
              ],
            },
            {
              type: "category",
              label: "Documenting",
              items: [
                "howtos/integrations/integration-docs",
                "howtos/integrations/doc-structure",
                "howtos/integrations/changelog"
              ],
            }
          ]
        },
        {
          type: "category",
          label: "Playbooks",
          items: [
            "howtos/playbooks/playbooks",
            "howtos/playbooks/playbook-conventions",
            "howtos/playbooks/generic-polling"
          ]
        },
        // {
        //   type: "category",
        //   label: "Scripts",
        //   items: [
        //     "howtos/how-scripts",
        //   ]
        // },
        // {
        //   type: "category",
        //   label: "Incidents, Fields & Layouts",
        //   items: [
        //     "howtos/how-incidents"
        //   ]
        // },
        // {
        //   type: "category",
        //   label: "Dashboards & Widgets",
        //   items: [
        //     "howtos/how-dashboards"
        //   ]
        // },
        {
          type: "category",
          label: "Contributing",
          items: [
            "howtos/contributing/circleci",
          ]
        },
      ],
    },
    {
      type: "category",
      label: "Tutorials",
      items: [
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
        // {
        //   type: "category",
        //   label: "Playbooks",
        //   items: [
        //     "tutorials/tut-playbooks"
        //   ]
        // },
        // {
        //   type: "category",
        //   label: "Scripts",
        //   items: [
        //     "tutorials/tut-scripts"
        //   ]
        // },
        // {
        //   type: "category",
        //   label: "Incidents, Fields & Layouts",
        //   items: [
        //     "tutorials/tut-incidents"
        //   ]
        // },
        // {
        //   type: "category",
        //   label: "Dashboard & Widgets",
        //   items: [
        //     "tutorials/tut-dashboards"
        //   ]
        // },
      ],
    }
  ],
  reference:
  [
    {
      type: "doc",
      id: "reference"
    },
    {
      type: "category",
      label: "Integrations",
      items: [
        "reference/ref-integrations",
      ]
    },
    {
      type: "category",
      label: "Playbooks",
      items: [
        "reference/ref-playbooks",
      ]
    },
    {
      type: "category",
      label: "Scripts",
      items: [
        "reference/ref-scripts",
      ]
    },
    {
      type: "category",
      label: "REST API",
      items: [
        "reference/ref-restapi",
      ]
    },
    {
      type: "category",
      label: "Code",
      items: [
        "reference/ref-code",
      ]
    },
    {
      type: "category",
      label: "Demisto SDK",
      items: [
        "reference/ref-demisto-sdk",
      ]
    }
  ],
  partners:
  [
    {
      type: "doc",
      id: "partners/why-demisto"
    },
    {
      type: "doc",
      id: "partners/become-a-tech-partner"
    },
    {
      type: "doc",
      id: "partners/partner-owned-integration"
    },
    {
      type: "doc",
      id: "partners/development-partners"
    },
  ]
};
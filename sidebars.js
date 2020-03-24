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
      label: "Concepts",
      items: [
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
      label: "Getting Started",
      items: [
        "integrations/getting-started-guide",
        "integrations/dev-setup",
        "integrations/packs-format",
        "integrations/package-dir",
        "integrations/docker",
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
            "integrations/code-conventions",
            "integrations/yaml-file",
            "integrations/integration-logo",
            "integrations/parameter-types",
            "integrations/fetching-incidents",
            "integrations/feeds",
            "integrations/fetching-credentials",
            "integrations/long-running",
            "integrations/context-and-outputs",
            "integrations/context-standards",
            "integrations/dbot",
            "integrations/dt",
            "integrations/integration-cache",
          ]
        },
        {
          type: "category",
          label: "Testing",
          items: [
            "integrations/linting",
            "integrations/unit-testing",
            "integrations/test-playbooks",
            "integrations/debugging"
          ],
        },
        {
          type: "category",
          label: "Documenting",
          items: [
            "integrations/integration-docs",
            "integrations/doc-structure",
            "integrations/changelog"
          ],
        }
      ]
    },
    {
      type: "category",
      label: "Playbooks",
      items: [
        "playbooks/playbook-contributions",
        "playbooks/playbooks",
        "playbooks/playbook-conventions",
        "playbooks/generic-polling"
      ]
    },
    {
      type: "category",
      label: "Contributing",
      items: [
        "contributing/circleci",
      ]
    },
    {
      type: "category",
      label: "Tutorials",
      items: [
            "tutorials/tut-setup-dev",
            "tutorials/tut-integration-ui"
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

if (fs.existsSync("docs/reference/sidebar.json")) {
  referenceSideBar = fs.readJSONSync("docs/reference/sidebar.json")
  sidebars["reference"] = referenceSideBar
}

module.exports = sidebars;

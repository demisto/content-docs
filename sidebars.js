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
        "integrations/xsoar-ide",
        "integrations/pycharm-plugin",
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
            "integrations/powershell-code",
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
            "integrations/changelog",
            "integrations/changelog-old-format",
          ],
        }
      ]
    },
    {
      type: "category",
      label: "Playbooks",
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
      items: [
        "incidents/incident-xsoar-incident-lifecycle",
        "incidents/incident-types",
        "incidents/incident-customize-incident-layout",
        "incidents/incident-fields",
        "incidents/incident-jobs",
        "incidents/incident-auto-extract",
        "incidents/incident-classification-mapping",
        "incidents/incident-pre-processing",
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
    },
    {
      type: "doc",
      id: "privacy"
    },
  ],
  partners:
  [
    {
      type: "doc",
      id: "partners/why-xsoar"
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

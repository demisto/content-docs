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
      collapsed: true,
      items: [
        {
          type: "doc",
          id: "concepts/getting-started-guide"
        },
        {
          type: "doc",
          id: "concepts/concepts"
        },
        {
          type: "category",
          label: "Design",
          collapsed: true,
          items: [
            "concepts/design",
            "concepts/use-cases",
            "concepts/design-best-practices"
          ]
        },
        {
          type: "category",
          label: "Developing",
          collapsed: true,
          items: [
            "concepts/xsoar-ide",
            "concepts/pycharm-plugin",
            "concepts/dev-setup",
            "concepts/demisto-sdk"
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
        "contributing/contributing",
        "contributing/contrib-requirements",
        "contributing/checklist",
        "contributing/conventions",
        "contributing/docs-contrib",
        "contributing/marketplace"
      ]
    },
    {
      type: "category",
      label: "Content Packs",
      collapsed: true,
      items: [
        "packs/packs-format",
        "packs/pack-docs-redir",
        "packs/pack-rn-redir",
        "packs/premium_packs"
        ]
    },
    {
      type: "category",
      label: "Integrations & Scripts",
      collapsed: true,
      items: [
        {
          type: "category",
          label: "Components",
          collapsed: true,
          items: [
            "integrations/package-dir",
            "integrations/yaml-file",
            "integrations/parameter-types",
            "integrations/integration-desc-redir",
            "integrations/integration-logo",
            "integrations/integration-doc-redir"
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
            {
              type: "category",
              label: "Context Standards",
              items: [
                "integrations/context-standards-about",
                "integrations/context-standards-mandatory",
                "integrations/context-standards-recommended",
              ]
            },
            {
              type: "category",
              label: "Generic Commands",
              items: [
                "integrations/generic-commands-about",
                "integrations/generic-commands-reputation"
              ]
            },
            "integrations/dbot",
            "integrations/docker"
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
          type: "category",
          label: "Advanced Topics",
          collapsed: true,
          items: [
            "integrations/feeds",
            "integrations/iam-integrations",
            "integrations/powershell-code",
            "integrations/fetching-credentials",
            "integrations/long-running",
            "integrations/dt",
            "integrations/integration-cache",
            "integrations/mirroring_integration",
            "integrations/openapi-codegen",
            "integrations/postman-codegen",
            "integrations/code-generator",
            "integrations/scheduled-commands"
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
        "playbooks/playbooks-field-reference",
        "playbooks/playbooks-generic",
        "playbooks/playbook-doc-redir"
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
      label: "Documentation",
      collapsed: true,
      items: [
        "documentation/documentation_tips",
        "documentation/pack-docs",
        "documentation/release-notes",
        "documentation/readme_file",
        "documentation/integration-description"
        ]
    },
    {
      type: "category",
      label: "Tutorials",
      collapsed: true,
      items: [
            "tutorials/tut-setup-dev",
            "tutorials/tut-design",
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
        "partners/paid-packs",
        "partners/adopt",
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
if (fs.existsSync("docs/reference/articles-sidebar.json")) {
  articlesSideBar = fs.readJSONSync("docs/reference/articles-sidebar.json")
  sidebars["articles"] = articlesSideBar
}
module.exports = sidebars;

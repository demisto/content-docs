---
id: faq
title: Frequently Asked Questions
---

## What IDE should I use?

When it comes to an External IDE, you should stick to what you're comfortable with.

We developed a free [plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm) for [PyCharm](https://www.jetbrains.com/pycharm/) that simplifies/automates a few tasks such as:
- Running unit tests
- Creating a blank integration or automation script
- Uploading/Downloading your integration code to/from Cortex XSOAR
- Running commands directly on Cortex XSOAR

However, if you want to a different IDE (Visual Studio Code, Sublime, vi, emacs, etc.) it's totally fine! It just means that some of those tasks must be performed manually. To automate them, you can use the  [demisto-sdk](https://github.com/demisto/demisto-sdk).

You can also write code directly in the [Cortex XSOAR UI](../concepts/xsoar-ide) but is not recommended if you want to reuse the code. Check [here](getting-started-guide#are-you-planning-to-contribute) for details.

:::note
Please note that IDEs are used only for writing Integrations and Automations, everything else (i.e. Playbooks) should be done in the Cortex XSOAR UI
:::

## Which tools should I use?

You'll need a combination of both the Cortex XSOAR UI and other tools. 

As a general rule of the thumb, we recommend that you use an external IDE and toolchain when:
- Working on your [integration code](../integrations/code-conventions) (YourIntegration.py)
- Working on the [unit test script](../integrations/unit-testing) (YourIntegration_test.py)
- Working on the [release notes](../integrations/release-notes) and README.md documentation files
- Running the [linting](../integrations/linting) and testing

Instead, you should use the Cortex XSOAR UI when:
- Creating the [Test Playbooks](../integrations/test-playbooks)
- Auto-generate the [integration documentation](../integrations/integration-docs)
- Creating [example playbooks](../playbooks/playbooks) to demonstrate your integration
- Working on the properties of your integration (parameters, commands, arguments, outputs, etc.)
- Testing the User Experience


### Which Python version you support?
Cortex XSOAR supports both Python2 and Python3. For new contributions we require Python3 (3.7+).

### Can I develop in JavaScript?
Cortex XSOAR supports JavaScript integrations and scripts. Our preferred development language is Python, and all new integrations and scripts should be developed in Python, which also provides a wider set of capabilities compared to the available JavaScript support. Simple scripts may still be developed in JavaScript.

### Can I develop in PowerShell?
Cortex XSOAR supports PowerShell integrations and scripts. However at the moment the amount of content written in PowerShell is minimal, so we recommend PowerShell only for advanced users as you won't find many examples to look at.

### Which OSs are supported for development?
Our recommended OS for development is either macOS or Linux, as we use bash and docker in some of our validation/testing flows.

If you are working on Windows, you can either work with a Linux VM or use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

### Licensing
Cortex XSOAR content repository has a [MIT License](https://github.com/demisto/content/blob/master/LICENSE).

---
id: faq
title: Frequently Asked Questions
---

### Which IDEs do you support?
- We have [PyCharm plugin](https://plugins.jetbrains.com/plugin/12093-demisto-add-on-for-pycharm)
- You can develop integrations and scripts in Cortex XSOAR
- Playbooks can only be developed in Cortex XSOAR.

### Which Python version you support?
Cortex XSOAR supports both Python2 and Python3. For new contributions we require Python3.

### Can I develop in JavaScript?
Cortex XSOAR supports JavaScript integrations and scripts. Our preferred development language is Python, and all new integrations and scripts should be developed in Python, which also provides a wider set of capabilities compared to the available JavaScript support. Simple scripts may still be developed in JavaScript.

### Which OSs are supported for development?
Our recommended OS for development is either macOS or Linux, as we use bash and docker in some of our validation/testing flows.

If you are working on Windows, you can either work with a Linux VM or utilize [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

### Licensing
Cortex XSOAR content repository has a [MIT License](https://github.com/demisto/content/blob/master/LICENSE).

### CLA is pending even though I signed the agreement
The CLA should be signed by all commiters of the branch. The CLA bot will let you know who are the commiters who have not yet signed the agreement by marking them with a red `X` like this:
![](../docs/doc_imgs/contributing/failed_CLA.png)

If the missing user appears under one of your commits (can be checked by visiting the `Commits` tab in the PR), it probably means that one of your commits was done using this user. Try the following:
1. If you have the credentials for the missing user, try to log-in and sign the CLA, then click the `recheck` button at the bottom of the CLA message. 
2. Try to link your commits: add the email address of the missing user to your GitHub email settings, then click the `recheck` button at the bottom of the CLA message. 
3. If the missing user is not a real user or named `Root` you will need to open a new branch: 
    - In your local environment - manually copy the code you have edited (most of the time you can copy the entire pack) to another locatoin.
    - Checkout the master branch.
    - Create a new branch.
    - Paste the code from beofre into your new branch.
    - Commit and push your new branch.
    - Open a new Pull Request for the new branch. **Don't forget to close the old PR and delete the old branch.**

For further details visit the [Troubleshooting Guide](https://docs.github.com/en/github/committing-changes-to-your-project/why-are-my-commits-linked-to-the-wrong-user) from Github Docs site.



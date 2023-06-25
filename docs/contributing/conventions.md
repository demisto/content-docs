---
id: conventions
title: Pull Request Conventions
---

If you open a GitHub Pull Request (PR) against the Cortex XSOAR [repository](https://github.com/demisto/content), a reviewer from the Content Team will be assigned and will accompany you in the process of getting your contribution released.

We receive lots of contributions and, while our reviewers always stay on top of all the requests, we recommend you to check the PR updates often and, if you think the process is stalled, feel free to "ping" the assigned reviewer by adding a new comment to the PR with a [mention](https://github.blog/2011-03-23-mention-somebody-they-re-notified/) or reach out in the **#demisto-developers** channel on our [Slack Community](https://dfircommunity.slack.com).

We value your contributions and want to make sure that your experience is smooth and easy and to reduce the amount of time and effort required to the minimum: in order to achieve it, we kindly ask for your support in following a few guidelines that will help us.

## Pull Request Best Practices

Please use the following guidelines when working on the changes requested by our reviewers:

- Make sure you always create PRs from your own fork using a dedicated branch (do NOT use the `master`/`main` branch).

- Use clear and brief messages for your commits ([this article](https://chris.beams.io/posts/git-commit/) has good examples).

- Do **NOT** use force pushes (i.e. `git push --force`): if you end up in a situation where you need to force push, it's probably better to reach to us and ask (in the PR itself or via [Slack](https://dfircommunity.slack.com)).

- During the process our reviewers might ask for several changes. Please work through the entire list and commit all the changes.

-  When you push changes to your fork's branch that was used to open the PR, the PR is automatically updated, you don't need to open a new PR. Do **NOT** open a new PR unless absolutely necessary (i.e. unless asked by the reviewer), as it will make it hard for the reviewer to track their comments. 

- The review usually has a *summary* and several *conversations*: make sure you address all the comments, including the ones in the summary:

    ![Pull Request Review Sections](/doc_imgs/contributing/pull_request_review.png)

- When addressing the review's *conversations*, please do **NOT** mark them as resolved: just write "**done**" in a comment, so the reviewer can better keep track of them:

    ![Resolve Conversation](/doc_imgs/contributing/resolve_conversation.png)

- Once you have pushed all requested changes, please ask for a new review by navigating to Reviewers section in the right sidebar in GitHub and click the ![](/doc_imgs/contributing/request-review-icon.png) icon next to the reviewer's name.


- **Recommendation**: If the branch you'll be using as the basis for the Pull Request includes more than 50 of commits, make sure to `squash` all commits into a single commit before creating the Pull Request. It makes the `git` history cleaner and easier for us to review it this way.

    Here's a little snippet to perform a squash merge after consolidating 122 commits into one:

    ```bash
    COMMITS=122
    
    git reset --hard HEAD~$COMMITS

    git merge --squash HEAD@{1}

    git commit -m "squash last $COMMITS into one"
    ```

    Alternatively, you can use a specific commit to squash from:

    ```bash
    COMMIT_HASH=0d1ddfc42
    
    git reset --hard $COMMIT_HASH

    git merge --squash HEAD@{1}

    git commit -m "squash from $COMMIT_HASH into one"
    ```

## The Build Process

The commit hooks of the repository should automatically run several commands locally on your system, such as `demisto-sdk validate`, that will make sure that your content is valid before you actually commit and push the changes to your Pull Request.

We also have CircleCI jobs that run automatically on your Pull Request after every push that validate the changes and run the same tests to make sure the contribution can be merged and become part of the content: you will see a few [GitHub Status Checks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks) that help validate that your pull request is according to our standards.

After you push changes, please come back to the Pull Request and check the status of the build after it's completed. Pay special attention to the following checks:
- ci/circleci: **Run Unit Testing and Lint**
- ci/circleci: **Run Validations**

Everything should be green:

![Build Status Green](/doc_imgs/contributing/doc_status_green.png)

If you have an error on a test, click on the details link to open the CircleCI Build page:

![Build Status Red](/doc_imgs/contributing/doc_status_red.png)

Browse to the failed CircleCI section and try to find the error message (usually in red). It's often something easy to understand and to fix, as in the following screenshot:

![CircleCI Error](/doc_imgs/contributing/circleci_error.png)

If the error is unclear or you are in doubt, add a comment to the PR to ask the reviewer or post a question in the **#demisto-developers** channel on [Slack](https://dfircommunity.slack.com).

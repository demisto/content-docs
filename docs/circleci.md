---
id: circleci
title: CircleCI
---

Lets start with the basics, [CircleCI](https://circleci.com) is the service we use in order to run our tests and to check the integrity of our code.

As you are probably aware, while pushing any code to our repos it will initiate a build within CircleCI, this build will execute several things, or in the Circle language steps.
Lets go over our steps to understand what each of them is doing:
- Prepare Environment:
    - Sets up the testing environment before starting the build. This usually involves provisioning a test server, setting access rules, etc.
- Install dependencies:
    - Here we install our python packages, and give access to the scripts folder. The scripts folder contains all of the scripts we are using for the next steps in Circle.
- Validate Files and Yaml
    - Validates the schema of the yml files you created, and checks to ensure that you haven’t made any changes that may effect backwards compatibility.
    - [You can learn more about the YAML structure here](yaml-file.md)
- Configure Test Filter
    - This step gathers all the relevant tests that Circle should run for the changes done in the given branch. When testing a single integration on a branch other than master, it is not necessary to test unrelated integrations or scripts.
    - A full test of every integration takes on average one hour and 15 minutes. Testing a specific integration, however, will take about 20 to 30 minutes.
    - In Nightly builds we will run all the tests we have
- Build Content Descriptor
    - This step populates the content descriptor with correct dates and assetId's.
- Common Server Documentation
    - This step builds all of the documentation for the server and includes, API documentation, getting started, as well as other documentation.
- Create Content Artifacts
    - These artifacts are the zip files that are uploaded to the server and contain all of the content for Demisto. They are composed of two parts:
        - content_new.zip contains all actual content, playbooks/scripts/integrations
        - content_test.zip contains all the test_playbooks
- Download Artifacts
    - This step retrieves the latest "Green" (or stable) build of the Demisto server.
- Download Configuration
    - Downloads data from content-test-conf, where all the private data is stored. This includes API keys, login details, and other configurations needed to create an instance of an integration.
- Create Instance
    - Create AWS instance for the build
- Setup Instance
    - Sets up Demisto on the AWS instance, as well as copies the content from the branch you are working on to the instance itself.
- Run Tests
    - This step iterates over each of the test playbooks. This involves creating an incident, attaching the test playbook to the incident, running the playbook, and finally awaiting the results.
- Destroy Instances
  - This step destroys the AWS instance in a case of success in the "Run Tests" step.

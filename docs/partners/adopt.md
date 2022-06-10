---
id: adopt 
title: Adopt-a-Pack 
---

The Cortex XSOAR Adopt-a-Pack program provides our technical partners a way to ‘take over’ a pack that was originally written by Demisto or Cortex XSOAR developers. The partner becomes the maintainer and supporter of the pack and receives several benefits as outlined below.

## Benefits for our Partner
Adopting a pack has several advantages for the partner:
- Differentiation: deliver unique solutions, commands, use cases, etc. in the pack.
- Control: Directly set the pack’s roadmap, features and release timing.
- Feedback: Receive direct input from actual users in the form of defects and enhancement requests.
- Visibility: See and review all community updates to that pack as a GitHub Reviewer.

### Marketing with Palo Alto Networks
- Opportunity to place company name and logo on the pack.
- Add detailed description and marketing to the pack (see yellow box, below) including links, images, company overview, etc. 
- Engage in marketing activities with Palo Alto Networks.

![pack example cyren](/docs/doc_imgs/partners/packexample_cyren.png)


## Process

Choose one of the options below and follow the step by step instructions or watch the video tutorials below to learn how to submit your adoption Pull Requests.

### Working on a local clone of Content repository

Choose either one of the methods below to start or complete adoption.

The adoption methods offered below assume that you have already [forked the Content repository](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-2-fork-the-github-repo) and [cloned the fork onto your local machine](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-3-clone-the-github-fork-locally).

<details>
	<summary>Adopt Using Helper Script</summary>
	<br/>
	This script will automatically perform the necessary steps to create an adoption PR.

**Note:** The script is supported for Ubuntu and Mac OS. If you encounter any issues, please report it by [opening an issue](https://github.com/demisto/content/issues).

  

**Requirements:** Before using this automation, make sure you have [`git`](https://git-scm.com/downloads) and [`python3`](https://www.python.org/downloads/) installed and in your `PATH`. This script will install [`demisto-sdk`](https://github.com/demisto/demisto-sdk#installation) Python package if it does not exist in your environment.

Follow the steps below to adopt using the helper script:  

1. Inside your terminal, change your working directory to the root of the Content repository. This is the location where you [cloned the forked `content` repository](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-3-clone-the-github-fork-locally).

2. Look for the pack you want to adopt under the `Packs/` directory. You will use the folder name as the second argument (`<MyPackName>`) to the `adopt_pack.bash` script.

3. Run the following `bash` script:

	```bash
	./Utils/adopt_pack.bash start <MyPackName>
	```

	When the script finishes its execution, it will print a link to GitHub to open a Pull Request with the changes. Click on the link or copy it into your browser and fill out the Pull Request form.

	For example, if we wanted to start adopting the `HelloWorld` Pack, we would run the following command:

	```bash
	./Utils/adopt_pack.bash start HelloWorld

	Initializing Pack Adoption...
	✓ Detected OS 'Mac OS'.
	✓ Dependency 'git' found.
	✓ Dependency 'python3' found.
	✓ Dependency 'demisto-sdk' found.
	✓ All dependencies met.
	✓ Found git repository in  '~/dev/demisto/fork/content'.
	✓ Pack 'HelloWorld' exists.
	✗ Not on master/main branch.
	- No untracked changes done, attempting to checkout to master/main branch...
	- Checking out master branch...
	- Branch 'partner-HelloWorld-adopt-start' exists, will be deleted and recreated...
	- ✓ Branch 'partner-HelloWorld-adopt-start' deleted
	✓ Branch 'partner-HelloWorld-adopt-start' created.
	✓ Pack version bumped to "1.2.12"  in  '~/dev/demisto/fork/content/Packs/HelloWorld/pack_metadata.json'
	✓ Release note created in  'Packs/HelloWorld/ReleaseNotes/1_2_12.md'
	✓ Release note '1_2_12.md' updated.
	✓ Adoption start message added to README.md
	✓ Changes committed.
	✓ Branch pushed upstream.
	  
	All done here!

	Please visit ====> https://github.com/me/content/pull/new/partner-HelloWorld-adopt-start <==== and fill out the Pull Request details to complete the adoption process
	```

<br/>

**After 90 days**

Prepare the following information as you will be prompted to submit those as part of the script execution:

- Your organization/company's name.
- A link to your organization's support site.
- Email address for your organization's support.
- A link to download your [author image](https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng). If no link is supplied, you will be asked to add it manually to `content/packs/<MyPackName>/Author_image.png`.

Once you have all the necessary information, run the script:

```bash
./Utils/adopt_pack.bash complete <MyPackName>
```

For example, if we were to complete the adoption of the `HelloWorld` Pack, we would run:
```bash
./Utils/adopt_pack.bash complete HelloWorld

Initializing Pack Adoption...
✓ Detected OS 'Mac OS'.
✓ Dependency 'git' found.
✓ Dependency 'python3' found.
✓ Dependency 'demisto-sdk' found.
✓ All dependencies met.
✓ Found git repository in  '~/dev/demisto/fork/content/'.
✓ Pack 'HelloWorld' exists.
✗ Not on master/main branch.
- No untracked changes done, attempting to checkout to master/main branch...
- Checking out master branch...
✓ Branch 'partner-HelloWorld-adopt-complete' doesn't exist
✓ Branch 'partner-HelloWorld-adopt-complete' created.
✓ Pack version bumped to "1.2.12" in '~/dev/demisto/fork/content/Packs/HelloWorld/pack_metadata.json'
✓ Release note created in 'Packs/HelloWorld/ReleaseNotes/1_2_12.md'
✓ Release note '1_2_12.md' updated.
✓ Support type 'partner' set in pack_metadata.json.
Enter your organization/company's name: acme
✓ Author set  in pack_metadata.json.
Enter a URL to your support site: https://acme.org
✓ URL field set  in pack_metadata.json.
Enter the email to your support site: support@acme.org
✓ Email field set  in pack_metadata.json.
Enter a URL to download the author image. If you do not have a URL, just press enter and make sure to add it manually according to https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng:

https://static.wikia.nocookie.net/looneytunes/imageshttps://static.wikia.nocookie.net/looneytunes/images/5/56/Comp_2.jpg

Attempting to download image from https://static.wikia.nocookie.net/looneytunes/images/5/56/Comp_2.jpg...
✓ Author image downloaded to '~/dev/demisto/fork/content//Packs/HelloWorld/Author_image.png'
✓ Adoption complete message added to README.md
✓ Changes committed.
✓ Branch pushed upstream.

All done here!

Please visit ====> https://github.com/me/content/pull/new/partner-HelloWorld-adopt-complete <==== and fill out the Pull Request details to complete the adoption process
```
</details>



<br/>

<details>
	<summary>Adopt Using a Text Editor/IDE</summary>
	<br/>
	You can also perform the necessary steps to adopt using any text editor or an IDE of your choice and the command line. 

**Requirements:** To follow along, you'll need to have [Demisto SDK installed on your machine](https://github.com/demisto/demisto-sdk#installation).

Follow the steps below to adopt using the a text editor or IDE. For additional guidance, you can watch how to [perform the steps using Visual Studio Code](https://www.youtube.com/watch?v=9GPkhtRw4Oc).

1. Locate your company's Pack folder and open the `README.md` file. Paste the below text into the file:
	```
	Note: Support for this Pack will be moved to the Partner on MONTH, DAY, YEAR.
	```

	Make sure you change the `MONTH`, `DAY`, and `YEAR` to the appropriate date that is 90 days from your submission date.

	  

2. Next, open the `pack_metadata.json` file and update the following sections:

	-  `support` - must say `partner`
	-  `author` - must say your company name
	-  `url` - must be changed to your company’s support site
	-  `email` - must be your company's support email.

3.  Once everything is updated, save your changes and run the `demisto-sdk update-release-notes -i <path to pack> -f`. The command output will instruct you to open the newly-created release note. Find the file and open it.

4. Replace the `%%RN%%` placeholder with the following text:
	```
	- Started adoption process.
	```

5. Go to _Source Control_ tab and commit the changes. Click on the _Publish Branch_ button. This will open a Pull Request.

6. Fill out the pull request details and create the pull request.

	**After 90 days**

	Please follow the steps below to complete the adoption process:


7. Open the `README.md` file and update the top of the file with the following:
	```
	Note: Support for this Pack moved to the partner on MONTH, DAY, YEAR.
	Please contact the partner directly via the support link on the right.
	```

2.  Open the `pack_metadata.json` file and update the following sections:

	-  `support` - must say “partner”

	-  `author` - must say your company name

	-  `url` - must be changed to your company’s support site

	-  `email` - must be your company's support email

	- Also, update your Author image using the [Author image instructions](https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng).

	3. Repeat step 3 through 6 in the previous section. Replace the `%%RN%%` placeholder with the following text:
	```
	- Completed adoption process.
	```

	Once the Cortex XSOAR engineering team merges your Pull Request, you will have successfully adopted your pack!
</details>


<br/>

### Adopt Using GitHub UI

If you prefer to create the Pull Request directly from GitHub, please follow the instructions below. For additional guidance, watch the [GitHub tutorial](https://www.youtube.com/watch?v=9mInBTuC6AE).

**Requirements:** Make sure you are working on [fork of the Content repository](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-2-fork-the-github-repo) and you are logged in with your GitHub account.
  
<details>
	<summary>Instructions</summary>
	1. Go to the `Packs` folder and find your company’s pack.

2. Find the `README.md` file and then click the ![Pencil_Icon](/docs/doc_imgs/partners/Pencil_Icon.png) on the right side of the screen to edit the file.

3. In the first line of the file, copy and paste the below text to show that the support is moving over:

	```
	Note: Support for this Pack will be moved to the Partner on MONTH, DAY, YEAR.
	```

  

Make sure you change the `MONTH`, `DAY`, and `YEAR` to the appropriate date that is **90 days** from your submission date.

  

While still in the `README.md` file, scroll down to the bottom of the page where select the 'Create a new branch for this commit and start a pull request'. Change the name of the new branch to `partner-COMPANY_NAME-adoption-start` and click on 'Propose changes'.

  

4. At the bottom of the screen, edit the Pull Request title to '`COMPANY_NAME` Pack Adoption' and adjust the description to 'Updating README file for adoption'.

5. Create a new branch named `partner-COMPANY_NAME-adoption-start`.

6. Now, click the green “Commit Changes” button. This will take you to your Pull Request.

7. As your Pull Request is not ready yet, will create an initial draft Pull Request as follows: At the bottom of the page, to the right of the `Create pull request` button there is a small button with an arrow, click and choose the `Draft` option. This will still create the Pull Request but the XSOAR eng team will not review it until it is taken out of draft mode.

Your Pull Request is not ready yet, continue following the instructions below.

8. At the top of your Pull Request, you will see your branch name that you created earlier. Click your branch and it will redirect you back into the main `content` repository. Ensure that the top left corner of the repository has your branch name before continuing.

  

![Branch_name](/docs/doc_imgs/partners/Branch_name.png)

  

9. Now, click into the `Packs` folder and find your company’s folder. Once you are in your company’s folder, click the `pack_metadata.json` file.

  

- Click the pencil to edit this file just as you did previously.

- Next, update the version number in the line titled `currentVersion` - increase the version up one number. For example, if it is “1.2.10” change it to “1.2.11”.

- Once the number is updated, go to the bottom of the page, make sure you have selected “Commit directly to the branch you’ve already created“ and then click the green “Commit changes” button.

- Now this step is completed, onto the next one!

  

10. Go back to your `Packs` folder and click into `ReleaseNotes`.


- Since we updated the version, we need to create a new release notes file. Find the file that has your original release notes number before you changed it. For example, if you changed “1_2_10” to “1_2_11” then you need to click into “1_2_10”.

- Once you find the correct release note, click the edit pencil icon as you did in the previous steps, and copy the last line in the file to keep the same format. Once you have it copied, click cancel changes and go back to the `ReleaseNotes` folder.

![release_note_step](/docs/doc_imgs/partners/release_note_step.png)

- Next, on the top right hand corner of the screen, click “Add file” and “Create new file”. Name your file the new version number you created earlier, which for this example would be `1_2_11.md`.

- Add the following text to the release note under the Pack name:
  	```
	- Started adoption process.
	```

- Name the subject of this to “update release notes”, make sure it is committing to your branch and then click “Commit new file”

  

**Note:** If your Pull Request is still in draft, please commit the changes and remove from draft.

  

Done! You have started the adoption process.

<br/>

**After 90 days**

Follow the below steps to complete the adoption process:

1. In order to complete the second adoption step, first you will need to update your `README.md` file and open a pull request with this text:

	```
	Note: Support for this Pack moved to the partner on MONTH, DAY, YEAR.

	Please contact the partner directly via the support link on the right.
	```

2. Next, go to the `pack_metadata.json` file and update the following sections:

	-  `currentVersion` - update the version. Using the video as our example, we would be updating it to “1.2.12”.
	-  `support` - must say “partner”
	-  `Author` - must say your company name
	-  `url` - must be changed to your company’s support site
	-  `Email` - must be your company's support email

	- Also, update your Author image using the <a  href="https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng">instructions on our site</a>.

3. Repeat step 10 from the previous section. Add the following text to the release note:
  	```
	- Completed adoption process.
	```
</details>



<br/>

Once the Cortex XSOAR engineering team merges your Pull Request, you will have successfully adopted your pack!
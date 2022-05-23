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

![pack example cyren](/doc_imgs/partners/packexample_cyren.png)

## Process
Choose one of the options below and follow the step by step instructions or watch the video tutorials below to learn how to submit your adoption Pull Requests. 

<details><summary><strong>Working on a local clone of Content repo</strong></summary>
<div>

<br/>
These methods assume that you have already [forked the `content` repository](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-2-fork-the-github-repo) and [cloned the fork onto your local machine](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-3-clone-the-github-fork-locally).
Choose either one of the methods below to start or complete adoption.

<br/>
<details><summary><strong>Adopt Using Helper Script</strong></summary>

<br/>

<div>This script will automatically perform the necessary steps to create an adoption PR.

**Note:** The script was only tested on Unix systems, specifically Mac OS and Ubuntu. It might not work correctly on other systems. 

**Requirements:**
Before using this automation, make sure you have [`git`](https://git-scm.com/downloads) and [`python3`](https://www.python.org/downloads/) installed and in your `PATH`. This script will install [`demisto-sdk`](https://github.com/demisto/demisto-sdk#installation) python package if it does not exist in your environment.

Follow the steps below to adopt using the helper script:

1. Change directory to where the `content` repository is located. This is the location where you [cloned the forked `content` repository](https://xsoar.pan.dev/docs/tutorials/tut-setup-dev#step-3-clone-the-github-fork-locally).

2. Look for the Pack you want to adopt in the `content/Packs/` directory. You will use the folder name as the second argument to the `adopt_pack.bash` script. 
For example, if we wanted to start adopting the `HelloWorld` Pack, we would run the following command:

```bash
PACK=HelloWorld
./Utils/adopt_pack.bash start $PACK
```

3. **After 90 days**, run the script below to complete the adoption:

```bash
PACK=HelloWorld
./Utils/adopt_pack.bash complete $PACK
```

You will be prompted for the following information when running this command:

- Your organization/company's name.
- A link to your organization's support site.
- Email address for your organization's support.
- A link to download your [author image](https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng). If no link is supplied, please add this manually to `content/packs/$PACK/Author_image.png`

</div>
</details>

<br/>

<details><summary><strong>Adopt Using Visual Studio Code</strong></summary>
<br/>
<div>
If you are creating the Pull Request from Visual Studio Code, please follow the below steps. For additional guidance, watch the <a href="https://www.youtube.com/watch?v=9GPkhtRw4Oc">Visual Studio video overview</a>.

1. Locate your company's pack folder and open the `README.md` file. Paste the below text into the file:

    ```
    Note: Support for this Pack will be moved to the Partner on MONTH, DAY, YEAR.
    ```
    Make sure you change the `MONTH`, `DAY`, and `YEAR` to the appropriate date that is 90 days from your submission date.

2. Once complete, save these changes and run `demisto-sdk update-release-notes -i <path to pack> -f` to update the release notes. See [documentation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md). After the command has been completed, it will create the new release note Markdown file in the `ReleaseNotes` folder and update the version number in `pack_metadata.json`. Before continuing, you need to add the following text to the release note: 

```
Start of adoption process.
```

3. Now, it's time to save and commit the changes as a GitHub pull request. Once you publish the changes via Visual Studio, GitHub will prompt you to open a pull request. When prompted, click the green button "Compare & pull request".
    - Double check the pull request to ensure all changes are correct.
    - Change the pull request title to 'Company Name Pack Adoption' and adjust the description to _Updating README file for adoption_.
    - When ready, click the green button “Create pull request" on the bottom of the page.
4. The request will now be reviewed, approved and merged by a Cortex XSOAR engineer!

**After the 90 days**, another pull request must be submitted to complete the adoption process. Please follow the below steps if you are submitting the final pull request via Visual Studio:
1. Update the release note just as you did in the first pull request but change the text to the below:
    ```
    Note: Support for this Pack moved to the partner on MONTH, DAY, YEAR.

    Please contact the partner directly via the support link on the right.
    ```
2. Next, go to the pack_metadata.json file and update the following sections:
    - `currentVersion` - update the version. For this example, we would be updating it to 1.2.12
    - `support` - must say `partner`
    - `author` - must say your company name
    - `url` - must be changed to your company’s support site
    - `email` - must be your company's support email.
3. Once everything is updated, save your changes and run the `demisto-sdk update-release-notes -i <path to pack> -f` as you did in the first pull request.

Next, open your pull request in GitHub as you did the first time and the engineers for Cortex XSOAR will review, approve and merge your newly adopted pack!

</div>
</details>

</div>
</details>

<br/>

<details><summary><strong>Adopt Using GitHub UI</strong></summary>
<br/>
<div>
If you prefer to create the Pull Request directly from GitHub, please follow the below step by step instructions. For additional guidance, watch the <a href="https://www.youtube.com/watch?v=9mInBTuC6AE">GitHub video overview</a>. 

**Requirements:** Make sure you have a GitHub account and you are logged in.

1. Go to the `Packs` folder and find your company’s pack.
2. Find the `README.md` file and then click the ![Pencil_Icon](/doc_imgs/partners/Pencil_Icon.png) on the right side of the screen to edit the file. 
3. In the first line of the file, copy and paste the below text to show that the support is moving over to the partner: 
    
    ```
    Note: Support for this Pack will be moved to the Partner on MONTH, DAY, YEAR.
    ```
    
    
    Make sure you change the `MONTH`, `DAY`, and `YEAR` to the appropriate date that is 90 days from your submission date.

4. Once complete, save these changes and run `demisto-sdk update-release-notes -i <path to pack> -f` to update the release notes. See [documentation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md). After the command has been completed, it will create the new release note Markdown file in the `ReleaseNotes` folder and update the version number in `pack_metadata.json`. Before continuing, you need to add the following text to the release note: 

        
        Start of adoption process.
        

5. Edit the Pull Request title to '`COMPANY_NAME` Pack Adoption' and adjust the description to 'Updating README file for adoption'.
6. Create a new branch named `partners-COMPANY_NAME-adoption-start`. 
7. Now, click the green “Commit Changes” button. This will take you to your Pull Request. Scroll down and click the green “Create Pull Request” at the bottom of the screen. 
  
**Note:** If you are not ready to officially submit the pull request for review, you can create a draft pull request instead. To the right of the “Create pull request” button there is a small button with an arrow, click that and choose the Draft option. This will still create the Pull Request but the XSOAR eng team will not review it until it is taken out of draft.
    
Your Pull Request is not ready yet, continue following the instructions below. 
    
8. At the top of your Pull Request, you will see your branch name that you created earlier. Click your branch and it will redirect you back into the main `content` repository. Ensure that the top left corner of the repository has your branch name before continuing. 

![Branch_name](/doc_imgs/partners/Branch_name.png)

9. Now, click into the `Packs` folder and find your company’s folder. Once you are in your company’s folder, click the `pack_metadata.json` file. 

    - Click the pencil to edit this file just as you did previously. 
    - Next, update the version number in the line titled `currentVersion` - increase the version up one number. For example, if it is “1.2.10” change it to “1.2.11”. 
    - Once the number is updated, go to the bottom of the page, make sure you have selected “Commit directly to the branch you’ve already created“ and then click the green “Commit changes” button. 
    - Now this step is completed, onto the next one! 

6. Go back to your `Packs` folder and click into `ReleaseNotes`. 

    - Since we updated the version, we need to create a new release notes file. Find the file that has your original release notes number before you changed it. For example, if you changed “1_2_10” to “1_2_11” then you need to click into “1_2_10”. 
    - Once you find the correct release note, click the edit pencil icon as you did in the previous steps, and copy the last line in the file to keep the same format. Once you have it copied, click cancel changes and go back to the `ReleaseNotes` folder. 
 ![release_note_step](/doc_imgs/partners/release_note_step.png)

   - Next, on the top right hand corner of the screen, click “Add file” and “Create new file”. Name your file the new version number you created earlier, which for this example would be `1_2_11.md`.
   - Now,  paste the text you copied in the previous step. Delete line 2 of the text and write “Start of adoption process, update to readme file” 
   - Name the subject of this to “update release notes”, make sure it is committing to your branch and then click “Commit new file” 

    **Note:** If your Pull Request is still in draft, please commit the changes and remove from draft. 

7. Done! You have started the adoption process. 

**After 90 days**, you will follow the below steps to complete the adoption process:
1. In order to complete the second adoption step, first you will need to update your README file & open a pull request with this text: 
    
    ```
    Note: Support for this Pack moved to the partner on MONTH, DAY, YEAR.
    
    Please contact the partner directly via the support link on the right.
    ```
    
    
2. Next, go to the `pack_metadata.json` file and update the following sections:
    - `currentVersion` - update the version. For this example, we would be updating it to “1.2.12” 
    - `support` - must say “partner” 
    - `Author` - must say your company name
    - `url` - must be changed to your company’s support site
    - `Email` - must be your company's support email 
    - Also, update your Author image using the <a href="https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng">instructions on our site</a>.
3. Lastly, update the release notes as you did in step 6. 

Once the Cortex XSOAR engineering team merges your Pull Request, you will have successfully adopted your pack!

</div>
</details>
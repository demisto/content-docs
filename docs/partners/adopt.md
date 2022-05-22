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
The process to Adopt-a-Pack takes under 5 minutes! Follow the step by step instructions and watch the video tutorials below to learn how to submit your adoption pull requests.  

<strong>Visual Studio Instructions</strong>: If you are creating the pull request from Visual Studio, please follow the below steps. For additional guidance, watch the <a href="https://www.youtube.com/watch?v=9GPkhtRw4Oc">Visual Studio video overview</a>.
<details>
<summary>Click here to see the Visual Studio instructions</summary>

<br/>

Please follow the below steps if you are working on a cloned GitHub repository from an IDE: 

1. Locate your company's pack folder and open the `README.md` file. Paste the below text into the file: 

    ```
    Note: Support for this Pack will be moved to the Partner on MONTH, DAY, YEAR.
    ```
    Make sure you change the `MONTH`, `DAY`, and `YEAR` to the appropriate date that is 90 days from your submittal date.

    - Once complete, save these changes and run `demisto-sdk update-release-notes -i <path to pack> -f` to update the release notes. See [documentation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md). After the command has been completed, it will create the new release note Markdown file in the `ReleaseNotes` folder and update the version number in `pack_metadata.json`. Before continuing, you need to add the following text to the release note: `Start of adoption process, update to readme file`
2. Now, it’s time to save and commit the changes as a GitHub pull request. Once you publish the changes via Visual Studio, GitHub will prompt you to open a pull request. When prompted, click the green button “Compare & pull request” 
    - Double check the pull request to ensure all changes are correct 
    - Change the pull request title to _Company Name Pack Adoption_ and adjust the description to _Updating README file for adoption_.
    - When ready, click the green button “Create pull request” on the bottom of the page 
3. The request will now be reviewed, approved and merged by a Cortex XSOAR engineer!

**After the 90 days, another pull request must be submitted to complete the adoption process. Please follow the below steps if you are submitting the final pull request via Visual Studio:**
1. Update the release note just as you did in the first pull request but change the text to the below:
    
    ```
    Note: Support for this Pack moved to the partner on MONTH, DAY, YEAR.
    
    Please contact the partner directly via the support link on the right.
    ```


2. Next, go to the pack_metadata.json file and update the following sections:
    - currentVersion - update the version. For this example, we would be updating it to 1.2.12
    - support - must say `partner`
    - author - must say your company name
    - url - must be changed to your company’s support site
    - email - must be your company's support email 
    
3. Once everything is updated, save your changes and run the `demisto-sdk update-release-notes -i <path to pack> -f` as you did in the first pull request.

Next, open your pull request in GitHub as you did the first time and the engineers for Cortex XSOAR will review, approve and merge your newly adopted pack! 


</details>
  

<br/>
 
 
  <strong>GitHub Instructions</strong>: If you prefer to create the pull request directly from GitHub, please follow the below step by step instructions. For additional guidance, watch the <a href="https://www.youtube.com/watch?v=9mInBTuC6AE">GitHub video overview</a>. 
<details>
<summary>Click here to see the GitHub instructions</summary>

1. Make sure you have a GitHub account and you are logged in
2. Go to the Packs folder and find your company’s pack 
3. Click the “README.md” file and then click the ![Pencil_Icon](/doc_imgs/partners/Pencil_Icon.png) on the right side of the screen to edit the file. 
  - In line #1 of the file, copy and paste the below text to show that the support is moving over to the partner: 
    
    ```
    Note: Support for this Pack will be moved to the Partner on MONTH, DAY, YEAR.
    ```
    
    
  - Make sure you change the `MONTH`, `DAY`, and `YEAR` to the appropriate date that is 90 days from your submittal date.
    
  - Edit the pull request title to “Company Name Pack Adoption” and adjust the description to “Updating README file for adoption”.
  - You will be creating a new branch, make sure you name the branch something easy to remember & save it like “XSOAR-patch-1” because you will be making other commits to this same branch. 
  - Now, click the green “Commit Changes” button, this will take you to your pull request. Scroll down and click the green “Create pull request” at the        bottom of the screen. 
  - **NOTE:** If you are not ready to officially submit the pull request for review, you can create a draft pull request instead. To the right of the              “Create pull request” button there is a small button with an arrow, click that and choose the Draft option. This will still create the pull request        but the XSOAR eng team will not review it until it is taken out of draft.
    
Your pull request is not ready yet, continue following the instructions below. 
    
4. At the top of your pull request, you will see your branch name that you created. Click your branch and it will redirect you back into the main content repository. Ensure that the top left corner of the repository has your branch name before continuing. 
![Branch_name](/doc_imgs/partners/Branch_name.png)
5. Now, click into the “Packs” folder and find your company’s folder. Once you are in your company’s folder, click the “pack_metadata.json” file. 

    - Click the pencil to edit this file just as you did previously. 
    - Next, update the version number in the line titled `currentVersion` - increase the version up one number. For example, if it is “1.2.10” change it to “1.2.11” . 
    - Once the number is updated, go to the bottom of the page, make sure you have selected “Commit directly to the branch you’ve already created“ and        then click the green “Commit changes” button. 
    - Now this step is completed, onto the next one! 

6. Go back to your `Packs` folder and click into `ReleaseNotes`. 

    - Since we updated the version, we need to create a new release notes file. Find the file that has your original release notes number before you changed      it. For example, if you changed “1_2_10” to “1_2_11” then you need to click into “1_2_10”. 
    - Once you find the correct release note, click the edit pencil icon as you did in the previous steps, and copy the last line in the file to keep the same format. Once you have it copied, click cancel changes and go back to the `ReleaseNotes` folder. 
 ![release_note_step](/doc_imgs/partners/release_note_step.png)
   - Next, on the top right hand corner of the screen, click “Add file” and “Create new file”. Name your file the new version number you created earlier, which for this example would be `1_2_11.md`.
   - Now,  paste the text you copied in the previous step. Delete line 2 of the text and write “Start of adoption process, update to readme file” 
   - Name the subject of this to “update release notes”, make sure it is committing to your branch and then click “Commit new file” 

    NOTE: If your pull request is still in draft, please commit the changes and remove from draft. 
7. Done! You have completed step 1 of the adoption process. 

**After 90 days, you will follow the below steps to complete the adoption process:**
1. In order to complete the second adoption step, first you will need to update your README file & open a pull request with this text: 
    
    ```
    Note: Support for this Pack moved to the partner on MONTH, DAY, YEAR.
    
    Please contact the partner directly via the support link on the right.
    ```
    
    
2. Next, go to the pack_metadata.json file and update the following sections:
    - “currentVersion” - update the version. For this example, we would be updating it to “1.2.12” 
    - “Support” - must say “partner” 
    - “Author” - must say your company name
    - “url” - must be changed to your company’s support site
    - “Email” - must be your company's support email 
    - Also, update your Author image using the <a href="https://xsoar.pan.dev/docs/packs/packs-format#author_imagepng">instructions on our site</a>.
4. Lastly, update the Release Notes as you did in step 1. 

Once the Cortex XSOAR engineering team merges your pull request, you will have successfully adopted your pack!


</details>

</br>
<strong>Command Line Instructions</strong>
<details>
<summary>Click here to see the command line instructions</summary>

From within the `content` directory, run:
```bash
./Utils/adopt_pack.bash
```

</details>
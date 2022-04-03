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

**Visual Studio Instructions**: If you are creating the pull request from Visual Studio, please follow the below steps. For additional guidance, watch the [Visual Studio video overview](https://www.youtube.com/watch?v=9GPkhtRw4Oc). 

<details>
<summary>Click here to see the Visual Studio instructions</summary>

<br/>
  
If work on a cloned Github repository from an IDE, please follow the below steps: 

1. Locate your company's pack folder and open the README.md file. Paste the below text into the file: 
  a. Note: Support for this pack will be moving to the partner around Month, Day, Year.
  b. Make sure you change the month, day, and year to the appropriate date that is 90 days from your submittal date. 
  c. Once complete, save these changes and run `demisto-sdk update-release-notes -i <path to pack> -f` to update the release notes. See [documentation](https://github.com/demisto/demisto-sdk/blob/master/demisto_sdk/commands/update_release_notes/README.md). After the command has been completed, it will create the new release note Markdown file in the `ReleaseNotes` folder and update the version number in `pack_metadata.json`. Before continuing, you need to add the following text to the release note: `_Start of adoption process, update to readme file_`
2. Now, it’s time to save and commit the changes as a Github pull request. Once you publish the changes via Visual Studio, Github will prompt you to open a pull request. When prompted, click the green button “Compare & pull request” 
  a. Double check the pull request to ensure all changes are correct 
  b. Change the pull request title to _Company Name Pack Adoption_ and adjust the description to _Updating README file for adoption_.
  c. When ready, click the green button “Create pull request” on the bottom of the page 
3. The request will now be reviewed, approved and merged by a Cortex XSOAR engineer!

**After the 90 days, another pull request must be submitted to complete the adoption process. Please follow the below steps if you are submitting the final pull request via Visual Studio: **
1. Update the release note just as you did in the first pull request but change the text to the below:
  a. Note: Support for this pack moved to the partner on Month, Day, Year. Please contact the partner directly via the support link on the right.
2. Next, go to the `pack_metadata.json` file and update the following sections:
  a. `currentVersion` - update the version. For this example, we would be updating it to `1.2.12` 
  b. `Support` - must say `partner`
  c. `Author` - must say your company name
  d. `url` - must be changed to your company’s support site
  e. `Email` - must be your company's support email 
3. Once everything is updated, save your changes and run the `demisto-sdk update-release-notes -i <path to pack> -f` as you did in the first pull request.

Next, open your pull request in Github as you did the first time and the engineers for Cortex XSOAR will review, approve and merge your newly adopted pack! 


</details>
  
  
**Github Instructions:** If you prefer to create the pull request directly from Github, please follow the below step by step instructions. For additional guidance, watch [Github video overview](https://www.youtube.com/watch?v=9mInBTuC6AE). 

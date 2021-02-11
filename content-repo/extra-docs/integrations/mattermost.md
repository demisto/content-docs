---
title: Mattermost
description: Send messages and notifications to your Mattermost Team.
---

## Overview


Use the Mattermost integration to send Demisto messages, files, and entries to your Mattermost environment (users, groups, and channels). You can also mirror a Demisto investigation to a Mattermost channel.

For this integration, you will first perform several configuration steps in Mattermost, and then configure the integration in Demisto.

* * *

## Configure Mattermost to Integrate with Demisto

Navigate to your Mattermost environment to perform these integration steps.

1.  In Mattermost - create a new Mattermost user (via Email invitation or an invitation link). Note that this user will act as the integrator between Demisto and Mattermost, so choose an appropriate name (i.e. "Demisto" or "DBot").
2.  In Mattermost - Under "Manage Members", assign the newly created user to the role of "Team Admin".  
    **Note**: You may need to log in as a Mattermost user with admin privileges to do this.
3.  In Mattermost - Enable "Personal Access Tokens" via System Console > Integrations > Custom Integrations.
4.  In Mattermost - Grant the user the permission to generate tokens via System Console > Users, select the newly created user, choose "Manage Roles" and select "Allow this account to generate personal access tokens" and "post:channels", press "Save".
5.  In Mattermost - Log in as the newly created user and generate the token, via "Account Settings > Security > Personal Access Tokens, and choose "Create New Token". You may enter a description (i.e. "Demisto Bot Token") and Press "Save".
6.  Copy the access token from the screen and store it in a secure location. Note that you won't be able to access this token again, if for any case you need to see it again you will need to repeat the process and generate a new token.
7.  For more information on stages 1-6, check out the Mattermost documentation regarding Personal Access Tokens: [https://docs.mattermost.com/developer/personal-access-tokens.html](https://docs.mattermost.com/developer/personal-access-tokens.html)

* * *

## Configure Demisto to Integrate with Mattermost


Navigate to your Demisto environment to perform these integration steps.

1.  Navigate to __Settings > Integrations > Servers & Services__.
    
2.  Locate Mattermost by searching for it using the search box on the top of the page.
    
3.  Click __Add instance__ to create and configure a new integration. You should configure the following settings:  
    **Name**: A textual name for the integration instance.  
    **Mattermost server address**: Your Mattermost server address.  
    **Team name**: Your Mattermost team name, in lowercase with '-' for spaces.  
    **Personal Access Token**: The Personal Access Token for the newly created user (as defined in steps 1-7 in "To set up Mattermost to work with Demisto")  
    **Notifications channel**: The channel to post notifications to, make sure to invite the newly created Demisto Bot user to this channel (in case of a Private channel).  
    **Should anyone be allowed to create incidents by DM** determines whether non-Demisto users are able to open incidents via Mattermost
    
4.  Press the ‘Test’ button to validate that the token is valid and the Mattermost server is responsive.  
    If you are experiencing issues with the service configuration, please contact Demisto support at [support@demisto.com](mailto:support@demisto.com)
5.  After completing the test successfully, press the ‘Done’ button.

* * *

## Integration Use Cases


*   Mirror an ongoing investigation to a Mattermost public channel, all entries will be mirrored, from Demisto to Mattermost and from Mattermost to Demisto, the channel will be automatically deleted when the investigation is closed.  
    Example: `"!mattermost-mirror-investigation type=all autoclose=true direction=Both mirrorTo=channel"`
*   Mirror an ongoing investigation to a Mattermost private channel, only chat entries will be mirrored, only from Mattermost to Demisto (and not vice versa), the channel will not be automatically deleted when the investigation is closed.  
    Example: `"!mattermost-mirror-investigation type=chat autoclose=false direction=ToDemisto mirrorTo=group"`
*   Send the message "hi" from Demisto to a Mattermost User named "john"  
    Example: `"!mattermost-send message=hi to=john"`
*   Send the message "hi" from Demisto to a Mattermost Channel named "incident-123"  
    Example: `"!mattermost-send message=hi channel=incident-123"`
*   Send a file that was previously uploaded to the War Room (with the ID "100@10") to a user named "john"  
    Example: `"!mattermost-send-file file=100@10 to=john"`

* * *

## Mattermost Commands in Demisto


Use the Demisto CLI to execute these actions in your Mattermost environment. After you successfully execute a command, a DBot message appears in the War Room with the command details.

*   [Close a Channel](#close-a-channel)
*   [Send a File to a User](#send-a-file-to-a-user)
*   [Send a File to a Channel](#send-a-file-to-a-channel)
*   [Send a Message to a User](#send-a-message-to-a-user)
*   [Send a Message to a Channel](#send-a-message-to-a-channel)
*   [Mirror an Investigation](#mirror-an-investigation)

### Close a Channel

Closes the mirrored Mattermost channel for investigation.

**Input**

`!mattermost-close-channel channel=_MattermostChannelName_`

**Example**

`!mattermost-close-channel channel=incident-46`

**Raw Output**

>Channel incident-46 was deleted.

### Send a File to a User

Sends a direct message and the specified file, which was uploaded to the War Room, to the specified Mattermost user.

If you specify a username and a channel in a single send file command, the channel overrides the username, and the file is only sent to the channel.

**Input**

`!mattermost-send-file file=_FileId_ to=_MattermostUsername_`

**Example**

`!mattermost-send-file file=Evidence1 to=Analyst123`

**Raw Output**

>Sent to Mattermost successfully.

### Send a File to a Channel

Sends a message and the specified file, which was uploaded to the War Room, to the specified Mattermost channel.

If you specify a channel and a username in a single send file command, the channel overrides the username, and the file is only sent to the channel.

**Input**

`!mattermost-send-file file=_FileId_ channel=_MattermostChannelName_`

**Example**

`!mattermost-send-file file=Evidence1 channel=incident-46`

**Raw Output**

>Sent to Mattermost successfully.

### Send a Message to a User

Sends a direct message to the Mattermost user.

If you specify a username and a channel in a single send message command, the channel overrides the username, and the file is only sent to the channel.

**Input**

`!mattermost-send to="_MattermostUsername"_`

**Example**

`!mattermost-send to="_Analyst123_"`

**Raw Output**

>Message sent to Mattermost successfully.

### Send a Message to a Channel

Sends a message to the specified Mattermost channel.

If you specify a channel and a username in a single send message command, the channel overrides the username, and the file is only sent to the channel.

**Input**

`!mattermost-send channel=_MattermostChannelName_`

**Example**

`!mattermost-send channel=incident-46`

**Raw Output**

>Message sent to Mattermost successfully.

### Mirror an Investigation

Sends a message to the specified Mattermost channel.

If you specify a channel and a username in a single send message command, the channel overrides the username, and the file is only sent to the channel.

**Input**

`!mattermost-send channel=_MattermostChannelName_`

**Example**

`!mattermost-send channel=incident-46`

**Raw Output**

>Message sent to Mattermost successfully.

* * *

## Troubleshooting

*   If you lose your Personal Access Token, generate a new token by repeating the [Configure Mattermost to Integrate
 with Demisto](#configure-mattermost-to-integrate-with-demisto) procedure.
*   Make sure that https requests can be made from your machine.
*   Make sure the newly created Mattermost User has the role "Team Admin" and the permissions "Allow this account to generate personal access tokens" and "post:all"
*   Please note that if you change the name of a mirrored channel from "incident-{ID}" - mirroring will not occur.
*   To send files / messages / notifications to a private channel - please invite the bot user to the channel first.
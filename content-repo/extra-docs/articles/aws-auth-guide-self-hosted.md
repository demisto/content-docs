---
title: AWS Integrations - Authentication - Self-hosted
description: Overview for authenticating to AWS when the Cortex XSOAR server is self-hosted outside the AWS environment in a remote network. 
---

The following provides information for authenticating to AWS when the Cortex XSOAR server is self-hosted outside the AWS environment in a remote network.

*Note: The documentation for a deployment scenario that has a Cortex XSOAR Server (or an Engine) deployed inside the AWS environment can be found [here](https://xsoar.pan.dev/docs/reference/articles/aws-integrations---authentication).*
 
Before you can use the AWS integrations in Cortex XSOAR, you need to perform several configuration steps in your AWS environment to enable Cortex XSOAR to authenticate and have the required permissions. 

## Using STS with AWS Integrations
AWS integrations in Cortex XSOAR use the Amazon Security Token Service (STS) to assume roles that are configured in the AWS IAM service. STS generates temporary credentials, which AWS integrations in Cortex XSOAR can use to assume roles, enabling you to perform various actions on the AWS services. For more information about the AWS services used, see
* [Amazon STS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)
* [AWS IAM Roles documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

## AWS Settings Overview
You will need to create the following resources:
* **An IAM user with programmatic only access** (such as "xsoar.remediation" user used in the example below) **and an Access key, for authentication**. 
   * The user needs to have a Permissions Policy attached that enables the user to assume the "integration roles" (**xsoar.remediation-UserPolicy**).
* **IAM Roles for different AWS - Cortex XSOAR integrations that you need to grant granular and temporary permissions to AWS services** (such as “xsoar.IAM.Integration-Role”).
   * Each role needs to have the IAM user as a Trusted entity, so the user can assume the role (sts:AssumeRole)
   * Each role needs to have a Permissions Policy attached that enables only the permissions required by the corresponding integration. Each integration has the required permissions documented in the integration documentation.
## Configure AWS Settings
### Create the IAM User  
1. Log in to the AWS Management Console and access the IAM console: (https://console.aws.amazon.com/iam/)
2. In the navigation pane, select **Users > Create user**.
   - **User name**: add a username (for e.g., "xsoar.remediation" )
   - **Access type**: select **Programmatic** access and click **Next**.
   - **Set permissions**: no permissions are required. Click **Next**.
   - **Tags** (optional): it is recommended to create a tag to describe the purpose (such us "Description: This user provide programmatic access to AWS - XSOAR integrations for auto-remediation").
3. Finalize the user creation and save the Access key ID and Secret access key (you will need them when configuring the integrations in Cortex XSOAR). 

### Create the IAM Roles for Integrations (Assumed Roles)
You will need to create Roles for your specific AWS - Cortex XSOAR Integrations, similar to the example below.
 
The following steps will exemplify the creation of a role for the [AWS - IAM integration](https://xsoar.pan.dev/docs/reference/integrations/aws---iam), with some granular IAM permissions only: iam:UpdateAccountPasswordPolicy and iam:ListUsers.
1. Create the policy for the role. In the navigation pane, select **IAM > Policies > Create Policy**. 
On the Create Policy page, paste the following code in the **JSON** tab:

       {
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Action": [
                      "iam:UpdateAccountPasswordPolicy",
                      "iam:ListUsers"
                  ],
                  "Resource": "*"
              }
          ]
        }

1. Click **Review Policy** and add a **Name** and a **Description** (for e.g., *Name: xsoar-IAM-Remediation_Policy, Description: The policy enables rights for AWS IAM - XSOAR integration. Used for Prisma Cloud - XSOAR demo*).
1. Go to **IAM > Roles > Create Role**.
   1. Select trusted entity type: **AWS Service**.
   1. **Choose a use case**: for now, select **EC2** (You will be able to replace it with the IAM user after the role is created.)
   1. **Attach permissions policies**: select the policy created earlier (for e.g., *xsoar-IAM-Remediation_Policy*)
   1. **Name**: add a descriptive name for the role (such as "xsoar-IAM.integration-Role")
   1. **Role description**: explain the purpose of the resources (such us "This role allows the xsoar.remediation IAM User to call AWS IAM services on your behalf").
   1. Click **Create Role**.
1. Update the role that you just created to trust the IAM user, so the user will be able to assume this role.
   1. Go to the Role page and select **Trust relationships > Edit trust relationship**. 
   1. For **Principal element**, replace **EC2 service** with the **IAM user** used for the authentication that you created earlier. The trust relationship should look like the following: 

            {
               "Version": "2012-10-17",
               "Statement": [
                   {
                       "Effect": "Allow",
                        "Principal": {
                        "AWS": "arn:aws:iam::<account-no>:user/xsoar.remediation"
                        },
                        "Action": "sts:AssumeRole"
                   }
               ]
            }   
   
You can now add and configure the AWS integrations on Cortex XSOAR. See the documentation for each AWS integration (such as: [AWS - IAM](https://xsoar.pan.dev/docs/reference/integrations/aws---iam)). 
The following steps will exemplify the creation of an IAM integration associated with the role created earlier. 

## Configure the AWS IAM Integration on Cortex XSOAR   
1. Navigate to **Settings > Integrations > Servers & Services**.
1. Search for **AWS - IAM**.
1. Click **Add instance** to create and configure a new integration instance.
   * **Name**: a descriptive name for the integration instance.
   * **Role Arn**: add Role Arn of the role created for this integration (such as: arn:aws:iam::<account-no>:role/xsoar-IAM.integration-Role).
   * **Role Session Name**: add a descriptive session name (such as: xsoar-IAM.integration-Role_SESSION).
   * **Role Session Duration**: add a session duration (default is 900). The XSOAR integration will have the permissions assigned only when the session is initiated and for the defined duration. 
   * **Access Key**: add the Access key that you saved when creating the IAM user.
   * **Secret Key**: add the Secret key that you saved when creating the IAM user.
1. Click **Test** to validate the connection (Keys & Token).

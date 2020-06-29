---
title: AWS Integrations - Authentication
description: AWS Integrations in Cortex XSOAR use Amazon Security Token Service (STS) to assume roles that are configured in AWS IAM service.
---

AWS integrations in Cortex XSOAR use the Amazon Security Token Service (STS) to assume roles that are configured in AWS 
IAM service. STS generates temporary credentials, which AWS integrations in Cortex XSOAR can use to assume roles, 
enabling you to perform various actions on the AWS services. For more information, 
see the [Amazon STS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html).

The first policy grants access to all resources using the `"*"` sign, and the other policies are more strict.

For more information, see the [AWS IAM Roles documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

## Background Information

### Basic Concepts of STS

STS allows a resource to "trade-in" the credentials the resource has attached to it for other credentials.

For your XSOAR instance or engine, the credentials attached are the EC2 Metadata. The metadata is essentially a group 
of environment variables that the instance can use to "trade-in" for another set of credentials. This method of 
credential delegation is much more secure since it does not require _Access Keys_ and _Secret Keys_ to be stored anywhere.

In order to facilitate this "trade-in" process, there needs to be a level of trust between the resources. This is called 
a _Trust Relationship_ and establishes a trusted relationship between two resources.

More information regarding [Trust Relationships can be found here.](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/edit_trust.html)

### How XSOAR uses STS to Authenticate
Your XSOAR Instance assumes a role using the following process flow:

![XSOAR AWS STS Auth Flow](../docs/doc_imgs/integrations/XSOAR_STS_Flow.png)

- Your XSOAR Instance/engine with the role attached to it first makes a request to AWS STS and passes it the details found in the EC2 Metadata.
- The STS service then checks to verify that the role you are requesting is allowed to be assumed by your XSOAR Instance.
- Next the STS service returns new credentials with the allowed permissions to your XSOAR Instance.
- Lastly, using the new credentials, your AWS integration will make a request to the AWS Service and return the response.

When this flow is done, the client making the request has the permissions associated with the acquired role.

### Current Capabilities of AWS Integrations

All XSOAR AWS integrations currently allow for roles to be assumed at the integration instance level and the command 
level. This allows for very granular control over several different roles and regions.

To override the role being assumed at the command level, please set the `roleArn` argument to the new role you wish to use. 
This argument is not required but does allow you to use a different role than the default role that is configured in your AWS integration's instance configuration. 

Please note that every assumed role must have an established trust relationship with your XSOAR instance or the command 
will indicate an *authentication* issue in the CLI.

## Configure AWS Settings

Before you can use the AWS integrations in Cortex XSOAR, you need to perform several configuration steps in your AWS environment.

### Prerequisites

*   You need to attach an instance profile with the required permissions to the Cortex XSOAR server or engine that is running on your AWS environment.
*   Instance profile requires minimum permission: _sts:AssumeRole_.
*   Instance profile requires permission to assume the roles needed by the AWS integrations

* * *

### Create an IAM Role for the Instance Profile

1.  Log in to the AWS Management Console and access the IAM console.  
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/)
2.  In the navigation pane, select **Policies** > **Create Policy**.  
    If a **Get Started** button displays, click the button and then select **Create Policy**.
3.  On the Create Policy page, paste this in the **JSON** tab. There are several optional configurations for the policy.  

```json    
{
    "Version": "2012-10-17",
    "Statement": [{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Resource": "\*"
    }]
}
```

4. The role attached to the server should have the following _Trust Relationship_ :

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
    
### Specify the Roles to Assume

You can specify which roles are allowed to be assumed by putting the role ARN in the _Resource_ section. These roles 
are the role ARNs that you would like your AWS XSOAR integrations to assume.
```json
{
    "Version": "2012-10-17",
    "Statement": [{
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Resource": [
"arn:aws:iam::123123123123:role/UpdateAPP",
"arn:aws:iam::123123123123:role/Admin",
"arn:aws:iam::123123123123:role/Readonly"
    ]
    }]
}
```

### Configuring your Assumed Roles

Now that the XSOAR server has the necessary role to begin assuming your other roles, the roles you would like your 
AWS XSOAR integrations to assume, must be configured. These roles need to be configured to know to _trust_ your XSOAR 
instance. This is done by configuring the following _trust relationship_ in the role you wish to assume.

**Please replace the ARN role with the role attached to your XSOAR Instance (or engine).**

```json
 {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "",
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::111111111111:role/ROLE_ATTACHED_TO_SERVER"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
```

    
### Grant Required Permissions

You can grant all required permissions to the instance profile to avoid the need to use different roles.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

4.  From the left menu, select the **Roles tab** > **Create Role**.
5.  Under **Choose the service that will use this role**, select **EC2**
6.  Click the **Next:Permissions** button.
7.  Select the policy that you created and click **Next:Permissions**.
8.  Enter the role name and description in the required fields, and click **Create Role**.

For more information, see the [Amazon IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_enable-create.html).

### Attach a Role to the Instance Profile

1.  Log in to the AWS Management Console and access the EC2 console.  
    [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/iam/)
2.  Select the Cortex XSOAR Server / Engine Instance.
3.  In the actions menu, select **Instance Settings** > **Attach/Replace IAM Role**.
4.  From the drop-down menu, select the role you created and click **Apply**.

## Configure the Necessary IAM Roles that the AWS Integration Can Assume

Each integration command has the required permissions documented in the integration documentation. For example, if you want to use EC2 integration, you should create a role with EC2FullAccess permissions. You can also configure a role with specific permitted actions, such as ec2:DescribeInstances, ec2:CreateImage, and so on.

## Configure AWS Integrations on Cortex XSOAR

You can now add and configure the AWS integrations on Cortex XSOAR. See the documentation for each AWS integration.
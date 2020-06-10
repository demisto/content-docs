---
title: AWS Integrations - Authentication
description: AWS Integrations in Cortex XSOAR use Amazon Security Token Service (STS) to assume roles that are configured in AWS IAM service.
---

AWS integrations in Cortex XSOAR use Amazon Security Token Service (STS) to assume roles that are configured in AWS IAM service. STS generates temporary credentials, which AWS integrations in Cortex XSOAR can use to assume roles, enabling you to perform various actions on the AWS services. For more information, see the [Amazon STS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html).

Each AWS integration can assume roles at the integration instance level and the command level, enabling maximum flexibility and security.

The first policy grants access to all resources using the `"*"` sign, and the other policies are more strict.

For more information, see the [AWS IAM Roles documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

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
      
    
### Specify the Roles

You can specify which roles are allowed to be assumed by putting the role ARN in the _Resource_ section.
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
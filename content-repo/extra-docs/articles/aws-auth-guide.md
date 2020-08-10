---
title: AWS Integrations - Authentication
description: Overview of authentication methods for AWS Integrations in Cortex XSOAR. 
---

AWS Integrations provide two options for authenticating to AWS:
* **Access Key and Secret Key**: the integration will use a configured Access Key and Secret Key to authenticate to AWS, which are set as part of the integration configuration parameters as can be seen in the following screen shot of the *AWS - S3* Integration:
  
  <img width="410" src="../../../docs/doc_imgs/reference/aws-s3.png" />
* **EC2 Instance Metadata**: the integration will use the EC2 instance metadata service to retrieve security credentials. In this scenario there is no need to configure an Access Key and Secret Key. Credential management is taken care of by the EC2 instance metadata service. The integration will fetch from the metadata service temporary credentials for authenticating to AWS. To configure the instance metadata service you will need to attach an instance profile with the required permissions to the Cortex XSOAR server or engine that is running on your AWS environment. More information at: [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

## Using STS with AWS Integrations
AWS Integrations provide the option of using the AWS Security Token Service (STS) to assume specific least privilege roles. This allows configuring a specific role per Integration instance instead of using the general role provided by the metadata service or the authentication via the Access Key and Secret Key. For more information see:
* [Amazon STS documentation](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html)
* [AWS IAM Roles documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

### Basic Concepts of STS

STS allows a resource to "trade-in" the credentials the resource has attached to it for other credentials.

For your XSOAR instance or engine, the credentials attached are the EC2 Metadata. The metadata is essentially a group 
of environment variables that the instance can use to "trade-in" for another set of credentials. This method of 
credential delegation is much more secure since it does not require _Access Keys_ and _Secret Keys_ to be stored anywhere.

To facilitate this "trade-in" process, there needs to be a level of trust between the resources. This is called 
a _Trust Relationship_ and establishes a trusted relationship between two resources.

More information regarding [Trust Relationships can be found here.](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/edit_trust.html)

### How XSOAR uses STS to Authenticate
Your XSOAR Instance assumes a role using the following process flow:

![XSOAR AWS STS Auth Flow](../../../docs/doc_imgs/integrations/XSOAR_STS_Flow.png)

- Your XSOAR Instance/engine with the role attached to it first makes a request to AWS STS and passes it the details found in the EC2 Metadata.
- The STS service then checks to verify that the role you are requesting is allowed to be assumed by your XSOAR Instance.
- Next, the STS service returns new credentials with the allowed permissions to your XSOAR Instance.
- Lastly, using the new credentials, your AWS integration will make a request to the AWS Service and return the response.

When this flow is done, the client making the request has the permissions associated with the acquired role.

### Current Capabilities of AWS Integrations

All AWS integrations in Cortex XSOAR currently allow for roles to be assumed at the integration-instance level and the command 
level. This allows for very granular control over several different roles and regions.

To override the role being assumed at the command level, set the `roleArn` argument to the new role you want to use. 
This argument is not required but does allow you to use a role other than the default role that is configured in your AWS integration's instance configuration. 

Note that every assumed role must have an established trust relationship with your XSOAR instance or the command 
will indicate an *authentication* issue in the CLI.

## Configure AWS Settings

Before you can use the AWS integrations in Cortex XSOAR, you need to perform several configuration steps in your AWS environment.

### Prerequisites

* Authenticated role (either via the EC2 metadata service or via Access Key and Secret Key) requires minimum permission: _sts:AssumeRole_.
* Authenticated role requires permission to assume the roles needed by the AWS integrations

## Configuration for using the EC2 metadata service (attached role)

### Create a Policy allowing to AssumeRole

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
    "Resource": "*"
    }]
}
```

4. The role attached to the server should have the following _Trust Relationship_:

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

Now that the XSOAR server/engine has the necessary role to begin assuming your other roles, the roles you would like your 
AWS XSOAR integrations to assume must be configured. These roles need to be configured to know to _trust_ your XSOAR 
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

Grant the required permissions to the instance profile. For testing purposes, you can grant all required permissions to the instance profile to simplify the setup.

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

More info available at: [Using an IAM Role to Grant Permissions to Applications Running on Amazon EC2 Instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

## Configure the Necessary IAM Roles that the AWS Integration Can Assume

Each integration command has the required permissions documented in the integration documentation. For example, if you want to use EC2 integration, you should create a role with EC2FullAccess permissions. You can also configure a role with specific permitted actions, such as ec2:DescribeInstances, ec2:CreateImage, and so on.

## Configure AWS Integrations on Cortex XSOAR

You can now add and configure the AWS integrations on Cortex XSOAR. See the documentation for each AWS integration.

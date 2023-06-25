---
id: playbooks-communication-task-customize-message
title: Customize a Communication Task Message
---
You can customize the message HTML and CSS for all communication tasks. You can also customize the header of the survey (the name of the SOC), but cannot customize actual surveys.

## Customize the SOC Name

The default SOC name is Your SOC team. To change the default SOC name: 

1. Navigate to **Settings** -> **About** -> **Troubleshooting** -> **Server Configuration**.

2. Add the key soc.name, and add the display name of your SOC as the value. This name is used in the default message and email of the communication tasks, and the web survey for all communication tasks.

   For example: soc.name: Acme SOC

## Data Collection Task

1. Navigate to **Settings** -> **About** -> **Troubleshooting** -> **Server Configuration**.

2. Add the key `messages.html.formats.externalFormSubmit`, and add the following HTML with your customizations as the value.

```
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
	
	<head>
		<title>
			{{.title}}
		</title>
		<!--[if !mso]><!-- -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<!--<![endif]-->
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<style type="text/css">
		#outlook a {
            padding: 0;
			text-decoration: none !important;
			color: #4da9ff;
			}
			a{
			text-decoration: none !important;
			color: #4da9ff;
			}
			
			.ReadMsgBody {
            width: 100%;
			}
			
			.ExternalClass {
            width: 100%;
			}
			
			.ExternalClass * {
            line-height: 100%;
			}
			
			body {
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
			}
			
			table,
			td {
            border-collapse: collapse;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
			}
			
			img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
            -ms-interpolation-mode: bicubic;
			}
			
			p {
            display: block;
            margin: 13px 0;
			}
		</style>
		<!--[if !mso]><!-->
		<style type="text/css">
			@media only screen and (max-width:480px) {
            @-ms-viewport {
			width: 320px;
            }
            @viewport {
			width: 320px;
            }
			}
		</style>
		<!--<![endif]-->
		<!--[if mso]>
			<xml>
			<o:OfficeDocumentSettings>
			<o:AllowPNG/>
			<o:PixelsPerInch>96</o:PixelsPerInch>
			</o:OfficeDocumentSettings>
			</xml>
		<![endif]-->
		<!--[if lte mso 11]>
			<style type="text/css">
			.outlook-group-fix { width:100% !important; }
			</style>
		<![endif]-->
		
		
		<style type="text/css">
			@media only screen and (min-width:480px) {
            .mj-column-per-100 {
			width: 100% !important;
            }
			}
		</style>
		
		
		<style type="text/css">
		</style>
		<style type="text/css">
			div {
			margin: 0 auto;
			}
			
			td {
            padding: 0;
			}
			
			p {
            padding: 0;
            margin: 0;
			}
		</style>
	</head>
	
	<body>
<div style="background-color: #f9f9fb;width: 100%; height: 100%; font-family: Helvetica, 'Trebuchet MS', Verdana, Geneva, Century Gothic, Arial, sans-serif;">
<table style="background-color: #00eb9a; width: 100%; height: 80px; vertical-align: middle;">
<tbody>
<tr>
<td style="width: 70%;">
<h2 style="margin: 0 10px;">Message From {{.title}}</h2>
</td>
<td style="width: 30%; text-align: center;"><img style="margin: 0 10px; width: auto; max-height:100%;" src="{{.logo}}" alt="Logo" /></td>
</tr>
</tbody>
</table>
<h3 style="text-align: center;">{{.subject}}</h3>
<div style="margin: 20px; background-color: white; padding: 20px;">
<p style="word-break: break-all;">{{.body}}</p>
<br />
<p style="word-break: break-all;"><a href="{{.link}}">{{.link}}</a></p>
</div>
</div>
</body>
</html>
```

## Ask Task

1. Navigate to **Settings** -> **About** -> **Troubleshooting** -> **Server Configuration**.

2. Add the key `messages.html.formats.externalAskSubmit`, and add the following HTML with your customizations as the value.

   ```
   <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
	
	<head>
		<title>
			{{.title}}
		</title>
		<!--[if !mso]><!-- -->
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<!--<![endif]-->
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<style type="text/css">
		#outlook a {
            padding: 0;
			text-decoration: none !important;
			color: #4da9ff;
			}
			a{
			text-decoration: none !important;
			color: #4da9ff;
			}
			
			.ReadMsgBody {
            width: 100%;
			}
			
			.ExternalClass {
            width: 100%;
			}
			
			.ExternalClass * {
            line-height: 100%;
			}
			
			body {
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
			}
			
			table,
			td {
            border-collapse: collapse;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
			}
			
			img {
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
            -ms-interpolation-mode: bicubic;
			}
			
			p {
            display: block;
            margin: 13px 0;
			}
		</style>
		<!--[if !mso]><!-->
		<style type="text/css">
			@media only screen and (max-width:480px) {
            @-ms-viewport {
			width: 320px;
            }
            @viewport {
			width: 320px;
            }
			}
		</style>
		<!--<![endif]-->
		<!--[if mso]>
			<xml>
			<o:OfficeDocumentSettings>
			<o:AllowPNG/>
			<o:PixelsPerInch>96</o:PixelsPerInch>
			</o:OfficeDocumentSettings>
			</xml>
		<![endif]-->
		<!--[if lte mso 11]>
			<style type="text/css">
			.outlook-group-fix { width:100% !important; }
			</style>
		<![endif]-->
		
		
		<style type="text/css">
			@media only screen and (min-width:480px) {
            .mj-column-per-100 {
			width: 100% !important;
            }
			}
		</style>
		
		
		<style type="text/css">
		</style>
		<style type="text/css">
			div {
			margin: 0 auto;
			}
			
			td {
            padding: 0;
			}
			
			p {
            padding: 0;
            margin: 0;
			}
		</style>
	</head>
	
	<body>
	<div style="background-color: #f9f9fb;width: 100%; height: 100%; font-family: Helvetica, 'Trebuchet MS', Verdana, Geneva, Century Gothic, Arial, sans-serif;">
	<table style="background-color: #00eb9a; width: 100%; height: 80px; vertical-align: middle;">
	<tbody>
	<tr>
	<td style="width: 70%;">
	<h2 style="margin: 0 10px;">Message From {{.title}}</h2>
	</td>
	<td style="width: 30%; text-align: center;"><img style="margin: 0 10px; width: auto; max-height:100%;" src="{{.logo}}" alt="Logo" /></td>
	</tr>
	</tbody>
	</table>
	<h3 style="text-align: center;">{{.subject}}</h3>
	<div style="margin: 20px; background-color: white; padding: 20px;">
	<p style="word-break: break-all;">{{.body}}</p>
	<br />
	{{.links}}
	</div>
	</div>
	</body>
	</html>

```

For more information about customized messages for communciation tasks, see the [Cortex XSOAR Administrator's Guide](https://docs.paloaltonetworks.com/cortex/cortex-xsoar/6-8/cortex-xsoar-admin/playbooks/playbook-tasks/communication-tasks).
# Python Email Automation Script

## Introduction
A python script that can read and send emails from the command line, while also being able to download attachments directly onto the device. The script uses Google's Gmail API and the Ezgmail module to access Gmail accounts without having to log in everytime.

## Disclaimer
The repository is not complete for a reason. To use the Gmail API and access your account without logging in, two JSON files are required in the working directory. Since those JSON files give access to your email account, I'm not going to include it here. 

## Gmail API
Before the Gmail API can used, it has to activated [here](https://developers.google.com/gmail/api/quickstart/python/). Once it is activated, it will give you access to a *credentials.json* file that will allow you to access Gmail features. To use the Ezgmail library, pip install ezgmail and user `ezgmail.init()` in the interactive shell to activate it. This will add a *tokens.json* file. 

## Features
* Can send emails with/without attachments
* Can read the most recent unread emails, and display sender, subject line, and body 
* Can download attachments from email directly onto the device

## Next Steps
These are some future additions that can be made to the application. 
* Implement a GUI
* Optimize code by reducing variable inputs


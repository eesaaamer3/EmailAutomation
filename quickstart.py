import ezgmail
import argparse
"""
Eesa Aamer
Date Created: 11/04/20
Last Modified: 13/04/20

A python script that can read and send emails, while also being
able to download attachments directly onto the device.

"""
parser = argparse.ArgumentParser(description="Enter valid email information")
parser.add_argument('Email', type=str, help='Receiver email address')
parser.add_argument('SubjectLine', type=str, help='Subject Line of Email')
parser.add_argument('Body', type=str, help='Body of Email')

args = parser.parse_args()




class SendWithNoAttachment:
    """ Sends emails without attachments """ 
    def __init__(self, email, subjectLine, body):
        self.email = email
        self.subjectLine = subjectLine
        self.body = body 
    
    def sender(self):
        ezgmail.send(self.email, self.subjectLine, self.body)
        

class SendWithAttachments(SendWithNoAttachment):
    """ Sends emails with variable amount of attachments"""
    def __init__(self, email, subjectLine, body, attachments):
        super().__init__(email, subjectLine, body) # Inherits from SendWithNoAttachment class
        self.attachments = attachments

    def senderWithAttach(self):
        ezgmail.send(self.email, self.subjectLine, self.body, self.attachments) # Command to send email

class Reader:
    """ Reads most recent unread emails """
    def __init__(self):
        unreadThreads = ezgmail.unread() # Collects unread email into lsit
        print("You have {} new emails".format(len(unreadThreads)))
        ezgmail.summary(unreadThreads) # Command that provides name, subject line, and body of unread emails
        

class Downloader:
    """ Downloads attachments from select emails """
    def __init__(self, subjectLine):
        self.subjectLine = subjectLine
    
    def mailFinder(self):
        mail = ezgmail.search(self.subjectLine) # Collects emails that have a certain subject line
        return mail

    def downloadOneAttachment(self, files):
        filename = input("What is the name of the file?: ")
        files[0].messages[0].downloadAttachment(filename) # Command to download a specific attachment

    def downloadAllAttachments(self, files):
        files[0].messages[0].downloadAllAttachments() # Command to download all attachments


class Introduction:
    """ Initial user interface """
    def __init__(self):
        pass
    def start(self):
        # Takes in user choice
        print("Welcome to the automated email system!")
        print(args.Email)
        print(args.Body)
        print(args.SubjectLine)
        initialResp = input("[S]end without attachments, [W]ith attachments, [R]ead?, or [D]ownload?: ")
        return initialResp


if __name__ == "__main__":
    begin = Introduction() # Introduction object acts as starting screen
    initial = begin.start()
    if initial == "S": # User wants to send an email
        newSenderWithNone = SendWithNoAttachment(args.Email, args.SubjectLine, args.Body).sender()
    elif initial == "W": # User wants to send email with attachments
        emails = input("Email Address?: ")
        subject = input("Subject Line?: ")
        bodyText = input("Body text?: ")
        print("For attachments, please list all attachments seperated with a space")
        attaches = input("Attachments?: ")
        new_list = [attach for attach in attaches.split(" ")]
        newSenderWithSome = SendWithAttachments(emails, subject, bodyText, new_list).senderWithAttach()
    elif initial == "R": # User wants to view recent unread emails
        newRead = Reader()
    elif initial == "D": # User wants to download attachments from file
        desiredEmail = input("What is the subject line?: ")
        newDownload = Downloader(desiredEmail)
        user_choice = input("[O]ne file or [A]ll?: ")
        if user_choice == "O":
            newDownload.downloadOneAttachment(newDownload.mailFinder())
        elif user_choice == "A":
            newDownload.downloadAllAttachments(newDownload.mailFinder())



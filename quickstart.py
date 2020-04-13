import ezgmail


class sendWithNoAttachment:
    def __init__(self, email, subjectLine, body):
        self.email = email
        self.subjectLine = subjectLine
        self.body = body 
    
    def sender(self):
        ezgmail.send(self.email, self.subjectLine, self.body)
        

class sendWithAttachments(sendWithNoAttachment):
    def __init__(self, email, subjectLine, body, *attachments):
        super().__init__(email, subjectLine, body)
        attachmentsList = [attachment for attachment in attachments]

    def senderWithAttach(self):
        ezgmail.send(self.email, self.subjectLine, self.body, self.attachmentsList)
        

class Introduction:
    def __init__(self):
        pass
    
    def start(self):
        print("Welcome to the automated email system!")
        initialResp = input("[S]end without attachments or [W]ith attachments?: ")
        if initialResp == "S" or initialResp == "W":
            return initialResp



if __name__ == "__main__":
    begin = Introduction()
    if begin.start() == "S":
        emails = input("Email Address?: ")
        subject = input("Subject Line?: ")
        bodyText = input("Body text?: ")
        newSenderWithNone = sendWithNoAttachment(emails, subject, bodyText).sender()
    elif begin.start() == "W":
        emails = input("Email Address?: ")
        subject = input("Subject Line?: ")
        bodyText = input("Body text?: ")
        print("For attachments, please list all attachments seperated with a space")
        attaches = input("Attachments?: ")

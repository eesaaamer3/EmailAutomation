import ezgmail


class SendWithNoAttachment:
    def __init__(self, email, subjectLine, body):
        self.email = email
        self.subjectLine = subjectLine
        self.body = body 
    
    def sender(self):
        ezgmail.send(self.email, self.subjectLine, self.body)
        

class SendWithAttachments(SendWithNoAttachment):
    def __init__(self, email, subjectLine, body, attachments):
        super().__init__(email, subjectLine, body)
        self.attachments = attachments

    def senderWithAttach(self):
        ezgmail.send(self.email, self.subjectLine, self.body, self.attachments)

class Reader:
    def __init__(self):
        unreadThreads = ezgmail.unread()
        print("You have {} new emails".format(len(unreadThreads)))
        ezgmail.summary(unreadThreads)
        

class Downloader:
    def __init__(self, subjectLine):
        self.subjectLine = subjectLine
    
    def mailFinder(self):
        mail = ezgmail.search(self.subjectLine)
        return mail

    def downloadOneAttachment(self, files):
        filename = input("What is the name of the file?: ")
        files[0].messages[0].downloadAttachment(filename)

    def downloadAllAttachments(self, files):
        files[0].messages[0].downloadAllAttachments()


class Introduction:
    def __init__(self):
        pass
    def start(self):
        print("Welcome to the automated email system!")
        initialResp = input("[S]end without attachments, [W]ith attachments, [R]ead?, or [D]ownload?: ")
        return initialResp


if __name__ == "__main__":
    begin = Introduction()
    initial = begin.start()
    if initial == "S":
        emails = input("Email Address?: ")
        subject = input("Subject Line?: ")
        bodyText = input("Body text?: ")
        newSenderWithNone = SendWithNoAttachment(emails, subject, bodyText).sender()
    elif initial == "W":
        emails = input("Email Address?: ")
        subject = input("Subject Line?: ")
        bodyText = input("Body text?: ")
        print("For attachments, please list all attachments seperated with a space")
        attaches = input("Attachments?: ")
        new_list = [attach for attach in attaches.split(" ")]
        newSenderWithSome = SendWithAttachments(emails, subject, bodyText, new_list).senderWithAttach()
    elif initial == "R":
        newRead = Reader()
    elif initial == "D":
        desiredEmail = input("What is the subject line?: ")
        newDownload = Downloader(desiredEmail)
        user_choice = input("[O]ne file or [A]ll?: ")
        if user_choice == "O":
            newDownload.downloadOneAttachment(newDownload.mailFinder())
        elif user_choice == "A":
            newDownload.downloadAllAttachments(newDownload.mailFinder())



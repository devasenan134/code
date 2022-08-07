import smtplib
from os.path import basename
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import sleep
import csv



# sender_email = os.environ.get("my_email")
# sender_passwd = os.environ.get("my_passwd")
# print(sender_email, sender_passwd)
sender_email = "bharathipriya.cs@ieee.org"
sender_passwd = "ieee2022"

def create_content():
    subject = "MAKERFAIR -IEEE YESIST 2022 ABSTRACT SUBMISSION REG"
    content = """\
    Good Day Specialists,

    “The secret of getting ahead is getting started”

    The end of something leads to a new beginning and yes it was smashing begging. 
    Congratulations on your successful submission of abstracts. 
    The abstracts has been in the progress of reviewing. 
    Much thanks for submitting it in the stipulated format. 
    Upon successful reviewing, the further protocols will be enclosed.

    Remarks: The prototype is not evident, practical difficulties may be there during implementation. 
        It will be useful for smart home.



    Link for registration: https://ieeeyesist12.org/registration/
    The Registration closes on August 20th
    
    Thanks&Regards,
    C.Bharathi Priya,
    Chair-Maker Fair
    """

    return subject, content

    



def process_csv(path):
    email = []
    with open(path) as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            if int(i[0]) in [654, 673, 688, 689, 691, 700, 699, 710, 712, 718, 722, 723]:
                email.append(i[1:8])

    filter_none = lambda mail: filter(None, mail)
    email = [list(filter_none(mail))for mail in email]
    return email


def create_msg(email, cc_mail, name=None):
    subject, content = create_content()
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["Subject"] = subject
    body = MIMEText(content, "plain")
    msg.attach(body)

    # file = "MF-Abstract-Template.pptx"
    # with open(file, "rb") as f:
    #     attachment = MIMEApplication(f.read(), Name=basename(file))
    #     attachment["Content-Disposition"] = 'attachment; filename="{}"'.format(basename(file))
    # msg.attach(attachment)
    msg["To"] = email
    msg["CC"] = cc_mail
    return msg


def send_mail(receivers):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_passwd)
        for email in receivers[:-1]:
            msg = create_msg(email, receivers[-1])
            server.send_message(msg)
            print("sent to " + email)




receivers = process_csv("email_list.csv")
print(receivers)


send_mail(receivers[9])

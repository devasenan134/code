import smtplib
from os.path import basename
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from time import sleep
import csv

from numpy import rec


# sender_email = os.environ.get("my_email")
# sender_passwd = os.environ.get("my_passwd")
# print(sender_email, sender_passwd)
sender_email = "bharathipriya.cs@ieee.org"
sender_passwd = "ieee2022"

def create_content():
    subject = "MAKERFAIR -IEEE YESIST 2022 ABSTRACT SUBMISSION REG"
    content = """\
    Dear All,
    
    A kind reminder, regarding the abstract submission.

    Please take a note that your abstract is not in the stipulated template. 
    Kindly modify the abstract according to the template and upload the same in the drive link given below within tomorrow(05/08/22) for further review process. 
    Attached is the drive link and the sample template for your attention.
    
    Link to submit Revised Abstract: https://drive.google.com/drive/folders/1kctpKsuB-NvIKIQ0xqkyUchq9rwOUkGW?usp=sharing

    Treat this as high priority and send us the revised template
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
            if int(i[0]) in [699, 700, 689, 691, 710, 712, 718, 722, 654, 673, 688, 723]:
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

for team in receivers:
    # send_mail(team)

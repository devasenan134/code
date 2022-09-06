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

def create_content(content):
    subject = "MAKERFAIR -IEEE YESIST 2022 ABSTRACT SUBMISSION REG"
    content = """\
Good day Infotechs,

“The only way to discover the limits of the possible is to go beyond the impossible”

Yup, the wait is over and the Makers Fair is all set to happen on Sep 10,11 at Sri Venkateshwara College of Engineering, Bangalore. 

The presentations are set to happen on Sep 10th.
You have to present (presentation and demo) for a time of 10-12 minutes and Q&A by jury will be for 3 minutes after the presentation.
Attached is your allotted time slot for the presentation. 

Slot - {0} IST

Kindly present the project in the stipulated template and it is advisable to follow up on the comments of the reviewers. 
The prototype should be demonstrated for hardware solution and simulation is required for software solution. Any queries if, kindly revert back to us.

We have attached the template to be followed in your presentation. Kindly stick on to it.

Suit up for the big day!

Thanks & Regards,
Team YESIST’12 2022
""".format(content)

    return subject, content

    



def process_csv(path):
    mentors = []
    slots = []
    participants = []
    
    mentor = ""
    time = ""
    email = []

    with open(path) as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            if i[0] != '':
                slots.append(time)
                mentors.append(mentor)
                participants.append(email)
                email = []

                time = i[1] 
                mentor = i[13]
                email.append(i[7])
            else:
                email.append(i[7])
            
        slots.append(time)
        mentors.append(mentor)
        participants.append(email)

    # filter_none = lambda mail: filter(None, mail)
    # email = [list(filter_none(mail))for mail in email]
    return mentors, slots, participants


def create_msg(email, time, cc_mail=None):
    subject, content = create_content(time)

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["Subject"] = subject
    body = MIMEText(content, "plain")
    msg.attach(body)

    file = "Finale-PPT-Template.pptx"
    with open(file, "rb") as f:
        attachment = MIMEApplication(f.read(), Name=basename(file))
        attachment["Content-Disposition"] = 'attachment; filename="{}"'.format(basename(file))
    msg.attach(attachment)


    msg["To"] = email
    msg["CC"] = cc_mail
    return msg


def send_mail(mentors, slots, participants):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_passwd)
        for i in range(1, len(slots)):
            team = participants[i]
            # team.append(mentors[i])
            
            print(team)
            for mail in team:
                msg = create_msg(mail, slots[i])
                server.send_message(msg)
            
            print("sent to", team)



def test_mail(email, time):
    msg = create_msg(email, time)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_passwd)
            server.send_message(msg) 


mentors, slots, participants = process_csv("MFFinale-Registration.csv")
print(slots, len(slots))


# test_mail("devasenan.murugan@gmail.com", "2.00 PM")
send_mail(mentors, slots, participants)
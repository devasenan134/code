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

def create_content(content=None):
    subject = "MAKERFAIR -IEEE YESIST 2022 ABSTRACT SUBMISSION REG"
    content = """\
Dear all, 
Greetings of the day!

At the outset, I take this opportunity to Thank all the participants and mentors for your constant support and cooperation in participating the IEEE YESIST 22-MakerFair and Grand Finale. 

In continuation to the Maker Fair event, we are planning to propose the list of projects which focuses on Sustainable Development Goal-12(SDG-12): 
Responsible Production and Consumption to Bangalore Humanitarian Technology Conclave (B-HTC 2022), Oct 1,2,2022

About the B-HTC 2022: 
The IEEE B-HTC 2022 is a flagship event of IEEE Bangalore Section.
It is held annually as part of the Humanitarian outreach program of the Section where technologists, innovators, entrepreneurs, and thought leaders share their passion in addressing the pressing problems, and share vision on futuristic technologies that will/may disrupt/impact our way of working and living.
This edition's focus of IEEE B-HTC on the theme of SDG-12 is meant to ensure good use of resources, improving energy efficiency, creating sustainable infrastructure, and providing access to basic services, as well as, green anddecent jobs and ensuring a better quality of life for all. 

The conference specifically focuses on: Sustainable management and use of natural resources.
                                        Responsible management of chemicals and food waste.
                                        Substantial reduction in waste generation.

If your abstract/Project falls under this category, Please send a 2 line Justification/description on How your project related/addresses to SDG-12 by 17.9.2022 before 5.00PM 

Thanks & Regards
C.BharathiPriya
(MakerFair Chair)
""".format()

    return subject, content

    



def process_csv(path):
    mentors = []
    participants = []
    
    mentor = ""
    email = []

    with open(path) as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            if i[0] != '':
                mentors.append(mentor)
                participants.append(email)
                email = []

                mentor = i[13]
                email.append(i[7])
            else:
                email.append(i[7])
            
        mentors.append(mentor)
        participants.append(email)

    # filter_none = lambda mail: filter(None, mail)
    # email = [list(filter_none(mail))for mail in email]
    return mentors, participants


def create_msg(email, cc_mail=None):
    subject, content = create_content()

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["Subject"] = subject
    body = MIMEText(content, "plain")
    msg.attach(body)

    # file = "Finale-PPT-Template.pptx"
    # with open(file, "rb") as f:
    #     attachment = MIMEApplication(f.read(), Name=basename(file))
    #     attachment["Content-Disposition"] = 'attachment; filename="{}"'.format(basename(file))
    # msg.attach(attachment)


    msg["To"] = email
    msg["CC"] = cc_mail
    return msg


def send_mail(mentors, participants):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_passwd)
        for i in range(1, len(mentors)):
            team = participants[i]
            team.append(mentors[i])
            print(team)
            for mail in team:
                msg = create_msg(mail)
                server.send_message(msg)
            
            print("sent to", team)



def test_mail(email):
    msg = create_msg(email)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_passwd)
            server.send_message(msg) 


mentors, participants = process_csv("MFFinale-Registration.csv")
# print(participants)


# test_mail("devasenan.murugan@gmail.com")
send_mail(mentors, participants)

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
Dear YESIST’12 Mentor,

Greetings of the Day!!
Thanks for your active guidance throughout the journey of YESIST’12 2022 for all the budding innovators. Your valuable support to the participants, allowed them to successfully submit their abstracts and projects. This added more value to YESIST’12 with quality submissions. 

We would like to invite you the Grand Finale of YESIST’12 and see your students perform against the innovators from various countries.   
Why attend the Grand Finale?

Opportunity to connect in person with the Keynote speakers and other international guests. 
Networking with fellow pilots, committee members and mentors. 
Opportunity to know about the innovation from other countries and interacting with the teams.

For mentors attending the event physically: Please register through the registration link: https://ieeeyesist12.org/pilot-finale-registration/
A registration fee of Rs.500 is to be paid for mentor attendance. The registration fee includes lunch and refreshments on both days of the event and dinner on 10th. No travel or accommodation will be provided by the organisers. 

The details of the Grand Finale of YESIST’12 2022 are mentioned below.
Venue: Sri Venkateshwara College of Engineering, Bengaluru, India.
Dates: September 10,11, 2022.

(Applicable for the mentors who are interested in joining the event in physical mode)

Thanks & Regards,
Team YESIST’12 2022
"""

    return subject, content

    



def process_csv(path):
    email = []
    with open(path) as file:
        reader = csv.reader(file)
        next(reader)
        for i in reader:
            if int(i[0]) in [699, 700, 689, 723, 654, 673, 688, 691, 710, 712, 718, 722, 727, 686, 701, 713, 693, 702, 717, 714, 715, 726, 731, 743]:
                email.append(i[7])

    # filter_none = lambda mail: filter(None, mail)
    # email = [list(filter_none(mail))for mail in email]
    return email


def create_msg(email, cc_mail=None, name=None):
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
        for email in receivers:
            msg = create_msg(email)
            server.send_message(msg)
            print("sent to " + email)






receivers = process_csv("email_list.csv")
print(receivers, len(receivers))


send_mail(receivers)

import os
import smtplib
import imghdr
from email.message import EmailMessage

import csv


# sender_email = os.environ.get("my_email")
# sender_passwd = os.environ.get("my_passwd")
# print(sender_email, sender_passwd)
sender_email = "deva134gaming@gmail.com"
sender_passwd = "gamingdeva134"


def parse_body_content(name):
    text = f"""\
Good day Innovators,

“The key is not spending time, but in investing it.”
          - Stephen R.Covey

Get ready to upgrade your innovative ideas into a working prototype..!

Pin your calendar for an interesting webinar on “Idea to product: A Reasearch Pathway for Students” which is delivered by profound enthusiast, Mr. Ramneek Kalra(IEEE Impact Creator)

Date: 1 June 2022
Time: 7.00 PM to 8.00 PM(IST)
Platform: MS TEAMS

Expecting your presence on June 1!

Cheers and Regards
Team YESIST22-Maker Fair
"""
    
    html = f"""\
<!DOCTYPE html>
<html>
    <body style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif">
        <div style="padding:10px 30px; background-color: rgb(191, 236, 191); text-align:center;">
            <h1 style="color:rgb(76, 94, 155);">IEEE YESIST12</h1>
        </div>
        
        <div style="margin: 10px 20%;">
            <div style="text-align:center;">
                <h1 style="display:inline;">Hi, </h1><h1 style="display:inline; text-transform:capitalize;">{ name }</h1>
                <h1 style="font-style:italic; font-weight:normal;">Wanna Kill Time Productively!</h1>
                </h4>
            </div>
            <hr>
            <div>
                <h3 style="color: rgb(90, 90, 218);">LIVE WEBINAR + Q&A</h3>
                <h1>Idea to Product</h1>
                <h2>A Research Pathway for Students</h2>
            </div>
            <br>
            <div>
                <h3>Get ready to upgrade your innovative ideas into a working prototype..! </h3>
                <h4 style="font-weight: normal">
                    Pin your calendar for an interesting webinar on “Idea to product: A Reasearch Pathway for Students” which is delivered
                    by profound enthusiast, Mr. Ramneek Kalra(IEEE Impact Creator)
                </h4>
            </div>

            <br>
            <div style="line-height: 0.2; ">
                <h4>Date: 1 June 2022</h4>
                <h4>Time: 7.00 PM to 8.00 PM(IST)</h4>
                <h4>Platform: MS TEAMS</h4>
                <br>
                <h3>Expecting your presence on June 1!</h3>
            </div>
            <hr>
            <br>
            <div style="line-height: 0.3; ">
                <h3>Cheers and Regards</h3>
                <h3>Team YESIST22-Maker Fair</h3>
            </div>
        </div>
    </body>
</html>
"""
    return html, text


def create_msg(email, name):
    msg = EmailMessage()
    msg["Subject"] = "Test subject"
    msg["From"] = sender_email
    msg["To"] = email
            
    html, text = parse_body_content(name)
    msg.set_content(text)
    msg.add_alternative(html, subtype="html")
           
    with open("poster.jpg", "rb") as file:
        file_data = file.read()
        file_type = imghdr.what(file.name)
        file_name = file.name
    msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)

    return msg



def send_mail():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_passwd)
        file = open("participants.csv", "r")
        reader = csv.reader(file)
        next(reader)

        for email, name in reader:
            msg = create_msg(email, name)
            server.send_message(msg)


if __name__ == "__main__":
    send_mail()

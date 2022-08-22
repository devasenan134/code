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
Dear {name},
Greetings of the Day!!!!
On behalf of IEEE YESIST12 Maker Fair Track, we are organizing a Webinar on an interesting topic " Idea to Product: A Research Pathway for Students" . The session is delivered by eminent and enthusiastic resource person, Mr. Ramneek Kalra,Chair, IEngage Track (IEEE YESIST12) | IEEE Impact Creator. 
 Date & Time: June 1,2022 | 7.00PM to 8.00 PM(IST)
Registration link:  http://shorturl.at/ktG28

Insights about the Webinar:
This webinar includes the following agenda & discussion points:
1. Introduction to Project-Based Learning
2. Finding a Problem Statement & Solution
3. Choosing the Right Team & Technology
4. In-Depth Research Survey
5. Prototype Development
6. Securing your Idea


About the Speaker:
	Mr.Ramneek is a Computer Science Engineer 
	 Proactive Volunteer at numerous organizations namely IEEE, Youth for Sustainability, Atal Innovation Mission (NITI Aayog, Govt. of India), Human Circle (Young India Challenge). He is an IEEE Young Professional who is an influencer. 
	Holding responsibilities of IEEE Impact Creator, Chair of History & Research Subcommittee under IEEE CS DVP Initiative, Chair of IEngage Track at IEEE YESIST12-2022.
	Author at IEEE USA E-Books, Member of “Universal Access to Technology” Technical Committee of IEEE SSIT
Kindly, pass this information to your student & young professional group and join to acquire knowledge on converting your innovative ideas to prototype 
Thanks & Regards,
Ms.C. Bharathi Priya,
Chair-Maker Fair, IEEE YESIST12
"""
    
    html = f"""\
<!DOCTYPE html>
<html>
    <body>
        <div>
        <h4>
            Dear { name } <br>
            Greetings of the Day!!!!
        </h4>
        <h5>
            On behalf of IEEE YESIST12 Maker Fair Track,<br>
            We are organizing a Webinar on an interesting topic <br>
            "Idea to Product: A Research Pathway for Students". <br>
            The session is delivered by eminent and enthusiastic resource person, Mr. Ramneek
            Kalra,Chair, IEngage Track (IEEE YESIST12) | IEEE Impact Creator. <br>
            Date & Time: June 1,2022 | 7.00PM to 8.00 PM(IST)
            <br><br><a href="http://shorturl.at/ktG28"><button class="btn btn-info">Click me to register</button></a>
        </h5>
        </div>
        
        <div style="background-color: grey; border-radius: 3px; padding:20px; margin:20px;">
            <h3>
                Insights about the Webinar:
            </h3>
            <h4>
                This webinar includes the following agenda & discussion points:<br>
                1. Introduction to Project-Based Learning<br>
                2. Finding a Problem Statement & Solution<br>
                3. Choosing the Right Team & Technology<br>
                4. In-Depth Research Survey<br>
                5. Prototype Development<br>
                6. Securing your Idea<br>
            </h4>
        </div>

        <div style="background-color: grey; border-radius: 3px; padding:20px; margin:20px;">
            <h3>
                About the Speaker:
            </h3>
            <h4>
                 Mr.Ramneek is a Computer Science Engineer
                 Proactive Volunteer at numerous organizations namely IEEE, Youth for Sustainability, Atal Innovation Mission (NITI
                Aayog, Govt. of India), Human Circle (Young India Challenge). He is an IEEE Young Professional who is an influencer.
                 Holding responsibilities of IEEE Impact Creator, Chair of History & Research Subcommittee under IEEE CS DVP
                Initiative, Chair of IEngage Track at IEEE YESIST12-2022.
                 Author at IEEE USA E-Books, Member of “Universal Access to Technology” Technical Committee of IEEE SSIT
            </h4>
            <h2>
                Kindly, pass this information to your student & young professional group and join to acquire knowledge on converting
                your innovative ideas to prototype
                Thanks & Regards,
                Ms.C. Bharathi Priya,
                Chair-Maker Fair, IEEE YESIST12
            </h2>
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

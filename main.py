##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

# 1. Update the birthdays.csv
data = pandas.read_csv(filepath_or_buffer="birthdays.csv")
data_dict = data.to_dict(orient="records")
# 2. Check if today matches a birthday in the birthdays.csv
time = dt.datetime.now()
month = time.month
day = time.day
for human in data_dict:
    if human["month"] == month and human["day"] == day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(file=f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
            letter = file.read()
            letter_with_name = letter.replace("[NAME]", human["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        sender = "YOUR MAIL HERE"
        password = "YOUR PASSWORD HERE"
        receiver = ["RECEIVER MAIL HERE"]
        subject = "Happy birthday!!!"
        text = "letter_with_name"
        print(text)
        message = """\
        From: %s
        To: %s
        Subject: %s
        
        
        %s
        """ % (sender, ", ".join(receiver), subject, text)
        print(message)
        try:
            with smtplib.SMTP("YOUR MAIL DOMAIN HERE", 587) as connection:
                connection.starttls()
                connection.login(user=sender, password=password)
                connection.sendmail(sender, receiver, message)
                print("Successfully sent email")
                # connection.close() wymagane gdy nie otwieramy przez with
        except smtplib.SMTPException:
            print("Error: unable to send email")

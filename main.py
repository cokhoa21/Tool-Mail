import pandas
import datetime
import smtplib
import random

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
random_number_letter = random.randint(1, 3)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"./letter_templates/letter_{random_number_letter}.txt") as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    my_email = "huykhoa21@gmail.com"
    my_password = "hsfoubjjrafygkks"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")




import pandas
import random
import smtplib
import datetime as dt
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
MY_EMAIL = "bobdylan9822@gmail.com"
PASSWORD = "orspmuroiowjdzsx"

# 2. Check if today matches a birthday in the birthdays.csv
today_date = dt.datetime.now()
today_day = today_date.day
today_month = today_date.month

birthdays = pandas.read_csv("birthdays.csv")
birthdays_list = birthdays.to_numpy().tolist()
birthdays_dict = birthdays.to_dict(orient="records")
print(birthdays_dict)
#sending letters function
def send_letter(letter,birthday):
    send_email = birthday[1]
    print(send_email)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=send_email, msg=f"Subject:Happy Birthday {birthday[0]}!\n\n"
                                                                        f"{letter}")

#birthday letter generator
def get_letter(birthday):
    #choose random letter
    num = random.randint(1,3)
    with open(f"../day-32-birthday-wisher/letter_templates/letter_{num}.txt", "r") as data_letter:
        letter = data_letter.readlines()
        letter[0] = letter[0].replace("[NAME]", f"{birthday[0]}")
        print(letter)

    with open(f"../day-32-birthday-wisher/letter_templates/letter_for_{birthday[0]}.txt", "w") as parent_letter:
        new_letter = parent_letter.writelines(letter)

    with open(f"../day-32-birthday-wisher/letter_templates/letter_for_{birthday[0]}.txt", "r") as final_letter:
        letter_to_send = final_letter.read()
        print(letter_to_send)
        return letter_to_send



for birthday in birthdays_list:
    #checks if a birthday in csv matches todays date
    if birthday[3] == today_month and birthday[4] == today_day:
        gen_letter = get_letter(birthday)
        send_letter(gen_letter, birthday)
        print(birthday)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





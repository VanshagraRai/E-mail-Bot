import os
import smtplib
import requests
import pyttsx3
from email.message import EmailMessage
from dotenv import load_dotenv

# Loading the environment Variables from .env file and Initializing python TTS library
load_dotenv()
engine = pyttsx3.init()

# Text-Speech Function
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Quote Generator Function
def quote_generator():
    try:
		# Making the get request
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
			# Extracting the core data
            json_data = response.json()
            data = json_data["data"]

			# Getting the quote from the data
            return data[0]["quoteText"]
        else:
            print("Error while getting quote")
    except:
        print("Something went wrong! Try Again!")




# Sending Our email Function
def send_email(receiver, subject, message):
    email_address = os.environ["email_address"]
    password = os.environ["password"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    
    # Logging into our E-mail account
    server.login(email_address, password)

    email = EmailMessage()
    email["From"] = "Sender_Email"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    "first": "abcd@gmail.com",
    "second":"efgh@gmail.com"
}

# Taking all the E-mail info from the user
def get_email_info():
    talk("Do you want to send a Quote or your own text?")
    choice = input()
    talk("To Whom you want to send email")
    name = input()
    try:
        receiver = email_list[name.lower()]
        print(receiver)
    except:
        talk("Looks like the user is not on the list please input the email address")
        receiver = input()
    
    talk("What is the subject of your email?")
    subject = input()
    if choice.lower() == "quote":
        quote = quote_generator()
        send_email(receiver,subject,quote)

    else:
         talk("Tell me the text in your email")
         message = input()
         send_email(receiver, subject, message)


    # Checking if the user wants to Send Any more E-mails
    print("Email sent successfully!")
    talk("Hey! Your email has been sent successfully!")
    talk("Do you want to send more email?")
    send_more = input()
    if send_more.lower() == "yes":
        get_email_info()
    else:
        talk("Thanks for using our email")


get_email_info()
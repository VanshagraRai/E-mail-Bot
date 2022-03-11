# E-mail Bot

It is a simple bot which basically sends e-mail to whomever the user wants to.
It also has a Text-To-Speech feature.

## Packages Necessary

```import os
import smtplib
import requests
import pyttsx3
from email.message import EmailMessage
from dotenv import load_dotenv
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) 

## Important!
DO MAKE A .env FILE TO SAVE YOUR PASSWORDS AND OTHER SENSITIVE INFO.

[Link for more info](https://www.twilio.com/blog/environment-variables-python).
(Read the section "Using .env files")
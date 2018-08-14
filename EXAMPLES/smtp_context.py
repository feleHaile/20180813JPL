#!/usr/bin/env python
import smtplib # <1>
from smtpopener import SMTPOpener

SMTP_HOST = 'smtpcorp.com'
SMTP_PORT = 2525
SMTP_USER = 'jstrickpython'
SMTP_PASSWORD = 'python(monty)'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']

MESSAGE = '''Subject: SMTP example
Hello hello?
Testing email from Python
'''

with SMTPOpener(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, True) as so:  # <6>
        so.sendmail(
            SENDER,
            RECIPIENTS,
            MESSAGE
        )
# <7>

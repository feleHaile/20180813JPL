#!/usr/bin/env python
import smtplib # <1>

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

class SMTPOpener():  # <1>

    def __init__(self, host, port, username, password, debug=False):  # <2>
        self._smtpserver = smtplib.SMTP(host, port)
        self._smtpserver.login(username, password)
        self._smtpserver.set_debuglevel(debug)

    def __enter__(self):  # <3>
        return self._smtpserver

    def __exit__(self, exc_type, exc_value, tb):  # <4>
        self._smtpserver.quit()  # <5>

with SMTPOpener(SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, True) as so:  # <6>
        so.sendmail(
            SENDER,
            RECIPIENTS,
            MESSAGE
        )
# <7>

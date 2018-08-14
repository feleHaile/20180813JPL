#!/usr/bin/env python
class SMTPOpener():  # <1>

    def __init__(self, host, port, username, password, debug=False):  # <2>
        self._smtpserver = smtplib.SMTP(host, port)
        self._smtpserver.login(username, password)
        self._smtpserver.set_debuglevel(debug)

    def __enter__(self):  # <3>
        return self._smtpserver

    def __exit__(self, exc_type, exc_value, tb):  # <4>
        self._smtpserver.quit()  # <5>



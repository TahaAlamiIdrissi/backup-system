# coding: utf-8
import smtplib

import conF


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(conF.smtpConf.get("mail"), conF.smtpConf.get("password"))
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("ouafine@gmail.com",conF.smtpConf.get("mail"), message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


""" subject = conF.smtpConf.get("subject")
msg = conF.smtpConf.get("content") """


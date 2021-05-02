from tkinter import *
import smtplib

app = Tk()
app.title("Email")
app.geometry("900x380")
app.resizable(0, 0)

emailaddressvalue = StringVar()
passwordvalue = StringVar()
recipientvalue = StringVar()
subjectvalue = StringVar()
bodyvalue = StringVar()

def sendtooutlook(recipient, mail):
    emailaddress = emailaddressvalue.get()
    password = passwordvalue.get()
    subject = subjectvalue.get()

    message = 'Subject: {}\n\n{}'.format(subject, mail)

    server = smtplib.SMTP('smtp-mail.outlook.com', 465)
    server.starttls()
    server.login(emailaddress, password)
    server.sendmail(emailaddress, recipient, message)
    server.quit()

def sendtogmail(recipient, mail):
    emailaddress = emailaddressvalue.get()
    password = passwordvalue.get()
    subject = subjectvalue.get()

    message = 'Subject: {}\n\n{}'.format(subject, mail)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(emailaddress, password)
    server.sendmail(emailaddress, recipient, message)
    server.quit()

def composeoutlookmessage():
    newWindow = Toplevel(app)
    newWindow.title("Compose Message")
    newWindow.geometry("400x400")
    newWindow.resizable(0, 0)

    to = Label(newWindow, text="To:", font=('Times New Roman', 20)).grid(row=1, column=0)
    recipientfield = Entry(newWindow, textvariable=recipientvalue)
    recipientfield.grid(row=1, column=1)

    subject = Label(newWindow, text="Subject:", font=('Times New Roman', 20)).grid(row=4,column=0)
    subjectfield = Entry(newWindow, textvariable=subjectvalue)
    subjectfield.grid(row=4, column=1)

    body = Text(newWindow, height=16, width=32)
    body.grid(row=6, column=1)

    sendbutton = Button(newWindow, text='Send', font=('Arial', 12, 'bold'), command=lambda: sendtooutlook(recipientfield.get(), body.get("1.0", END)), fg='white', bg='dodger blue').grid(row=7, column=0)

def composegmailmessage():
    newWindow = Toplevel(app)
    newWindow.title("Compose Message")
    newWindow.geometry("400x400")
    newWindow.resizable(0, 0)

    to = Label(newWindow, text="To:", font=('Times New Roman', 20)).grid(row=1, column=0)
    recipientfield = Entry(newWindow, font=('Times New Roman', 20), textvariable=recipientvalue)
    recipientfield.grid(row=1, column=1)

    subject = Label(newWindow, text="Subject:", font=('Times New Roman', 20)).grid(row=4,column=0)
    subjectfield = Entry(newWindow, font=('Times New Roman', 20), textvariable=subjectvalue)
    subjectfield.grid(row=4, column=1)

    body = Text(newWindow, height=16, width=32)
    body.grid(row=6, column=1)

    sendbutton = Button(newWindow, text='Send', font=('Arial', 12, 'bold'), command=lambda: sendtogmail(recipientfield.get(), body.get("1.0", END)), fg='white', bg='dodger blue').grid(row=7, column=0)

def outlooklogin():
    newWindow = Toplevel(app)
    newWindow.title("Sign in to Outlook")
    newWindow.geometry("400x470")
    newWindow.resizable(0, 0)

    outlookpic = PhotoImage(file="outlook.png")
    outlooklogo = outlookpic.subsample(3, 3)
    outlook = Label(newWindow, image=outlooklogo)
    outlook.image = outlooklogo
    outlook.pack()

    Label(newWindow, text="").pack()

    Label(newWindow, text="Email:", font=('Times New Roman', 20)).pack()
    emailfield = Entry(newWindow, font=('Times New Roman', 20), textvariable=emailaddressvalue).pack()
    Label(newWindow, text="").pack()
    Label(newWindow, text="Password:", font=('Times New Roman', 20)).pack()
    passwordfield = Entry(newWindow, show="*", font=('Times New Roman', 20), textvariable=passwordvalue).pack()
    Label(newWindow, text="").pack()
    signin = Button(newWindow, text='Sign in', font=('Arial', 12, 'bold'), command=composeoutlookmessage, height=1, width=10, fg='white', bg='dodger blue').pack()

def gmaillogin():
    newWindow = Toplevel(app)
    newWindow.title("Sign in to Gmail")
    newWindow.geometry("420x400")
    newWindow.resizable(0, 0)

    googlepic = PhotoImage(file="google.png")
    googlelogo = googlepic.subsample(4, 4)
    google = Label(newWindow, image=googlelogo)
    google.image = googlelogo
    google.pack()

    Label(newWindow, text="").pack()

    Label(newWindow, text="Email:", font=('Times New Roman', 20)).pack()
    emailfield = Entry(newWindow, font=('Times New Roman', 20), textvariable=emailaddressvalue).pack()
    Label(newWindow, text="").pack()
    Label(newWindow, text="Password:", font=('Times New Roman', 20)).pack()
    passwordfield = Entry(newWindow, show="*", font=('Times New Roman', 20), textvariable=passwordvalue).pack()
    Label(newWindow, text="").pack()
    signin = Button(newWindow, text='Sign in', font=('Arial', 12, 'bold'), command=composegmailmessage, height=1, width=10, fg='white', bg='dodger blue').pack()

text = Label(app, text="To log in to an email service, click on its corresponding logo below", font=('Futura', 20, 'bold'), fg='deep sky blue').grid(row=1)

gmailpic = PhotoImage(file="gmail.png")
gmaillogo = gmailpic.subsample(3, 3)
gmail = Button(app, image=gmaillogo, command=gmaillogin).grid(row=2)
outlookpic = PhotoImage(file="outlook.png")
outlooklogo = outlookpic.subsample(3, 3)
outlook = Button(app, image=outlooklogo, command=outlooklogin).grid(row=3)

app.mainloop()

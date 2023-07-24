#import tkinter
from tkinter import *
#create gui window
covid_contact_tracing_app = Tk()
covid_contact_tracing_app.title("COVID-19 CONTACT TRACING APP Version 1.0")
covid_contact_tracing_app.geometry("720x720")
#make gui for user input
def covid_gui():
    gui_label=Label(covid_contact_tracing_app, text='COVID-19 CONTACT TRACING APP', font =( 'Arial', 15))
    gui_label.pack(padx = 10, pady =10)
    #user's last name
    userlastname = Label(covid_contact_tracing_app,text = "Last Name : ")
    userlastname.place(x=25, y=50)
    userlastname_entry = Entry(covid_contact_tracing_app)
    userlastname_entry.place(x=105, y=50)
    #user's first name
    userfirstname = Label(covid_contact_tracing_app,text = "First Name : ")
    userfirstname.place(x=275, y=50)
    userfirstname_entry = Entry(covid_contact_tracing_app)
    userfirstname_entry.place(x=350, y=50)
    #user's middle name
    usermiddlename = Label(covid_contact_tracing_app,text = "Middle Name : ")
    usermiddlename.place(x=500, y=50)
    usermiddlename_entry = Entry(covid_contact_tracing_app)
    usermiddlename_entry.place(x=585, y=50)
#make database



covid_gui()
covid_contact_tracing_app.mainloop()
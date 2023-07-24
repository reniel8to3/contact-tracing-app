#import tkinter
from tkinter import *
#create gui window
covid_contact_tracing_app = Tk()
covid_contact_tracing_app.title("COVID-19 CONTACT TRACING APP Version 1.0")
covid_contact_tracing_app.geometry("720x720")
#make gui for user input
def covid_gui():
    gui_label=covid_contact_tracing_app.Label(covid_contact_tracing_app, text='COVID-19 CONTACT TRACING APP', font =( 'Arial', 18))
    gui_label.pack(padx = 10, pady =10)
    #user's last name
    userlastname = Label(covid_contact_tracing_app,text = "Last Name : ")
    covid_contact_tracing_app.grid(row = 0, column = 0,pady=10,padx=5) 
    e1 = Entry(covid_contact_tracing_app)
    e1.grid(row = 0, column = 1)
    #user's first name
    userfirstname = Label(covid_contact_tracing_app,text = "First Name : ") 
    covid_contact_tracing_app.grid(row = 0, column = 1,pady=10,padx=5)
    e2 = Entry(covid_contact_tracing_app)
    e2.grid(row = 0, column = 1)
    #user's middle name
    usermiddlename = Label(covid_contact_tracing_app,text = "Middle Name : ") 
    covid_contact_tracing_app.grid(row = 0, column = 2,pady=10,padx=5)
    e3 = Entry(covid_contact_tracing_app)
    e3.grid(row = 0, column = 2)
    #user's age
    #user's phone number
    #user's email
    #user's address
    #vaccination status
    #symptoms status
    #contact person details
    btn = Button(covid_contact_tracing_app, text = "Submit") 
    btn.grid(row = 3, column = 1)
#make database
covid_contact_tracing_app.mainloop()
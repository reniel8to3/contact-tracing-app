#import tkinter
from tkinter import *
from tkinter import ttk
#create gui window
covid_contact_tracing_app = Tk()
covid_contact_tracing_app.title("COVID-19 CONTACT TRACING APP Version 1.0")
covid_contact_tracing_app.geometry("720x720")
#make gui for user input
def covid_gui():
    gui_label=Label(covid_contact_tracing_app, text='COVID-19 CONTACT TRACING APP', font =( 'Arial', 15, 'bold'))
    gui_label.pack(padx = 10, pady =10)
    gui_instruction=Label(covid_contact_tracing_app, text='Please fill up all the required details needed by contact tracing app.', font =( 'Arial', 10))
    gui_instruction.place(x=160, y=50)
    #banner
    personalinfo=Label(covid_contact_tracing_app, text='Respondent Details', font =( 'Arial', 10, 'bold', 'italic'))
    personalinfo.place(x=10, y=80)
    #user's last name
    userlastname = Label(covid_contact_tracing_app,text = "Last Name : ")
    userlastname.place(x=25, y=110)
    userlastname_entry = Entry(covid_contact_tracing_app)
    userlastname_entry.place(width = 120, x=105, y=110)
    #user's first name
    userfirstname = Label(covid_contact_tracing_app,text = "First Name : ")
    userfirstname.place(x=275, y=110)
    userfirstname_entry = Entry(covid_contact_tracing_app)
    userfirstname_entry.place(width= 120, x=350, y=110)
    #user's middle name
    usermiddlename = Label(covid_contact_tracing_app,text = "Middle Name : ")
    usermiddlename.place(x=500, y=110)
    usermiddlename_entry = Entry(covid_contact_tracing_app)
    usermiddlename_entry.place(width =120, x=585, y=110)
    #user's age
    userage = Label(covid_contact_tracing_app,text = "Age : ")
    userage.place(x=60, y=145)
    userage_entry = Entry(covid_contact_tracing_app)
    userage_entry.place(width=60, x=105, y=145)
    #user's gender
    usergender = Label(covid_contact_tracing_app,text = "Gender : ")
    usergender.place(x=275, y=145)
    usergender_entry=Entry(covid_contact_tracing_app,text = "Gender :")
    usergender_entry.place = ttk.Combobox(values=["Male", "Female", "Prefer not to say"])
    #user's contact
    usernumber=Label(covid_contact_tracing_app, text = "Contact No. : ")
    usernumber.place(x=500, y=145)
    usernumber_entry = Entry(covid_contact_tracing_app)
    usernumber_entry.place(width=120, x=585, y=145)
    #user's vaccination status
    uservacc=Label(covid_contact_tracing_app, text= 'Status :')
    uservacc.place(x=50, y=175)
    radio=IntVar()
    uservac1 = Radiobutton(covid_contact_tracing_app, text="First Dose",variable=radio,value="1") 
    uservac1.place(x=105, y=175)
    uservac2 = Radiobutton(covid_contact_tracing_app, text="Second Dose",variable=radio,value="2")
    uservac2.place(x=205, y=175)
    uservac3 = Radiobutton(covid_contact_tracing_app, text="First Booster",variable=radio,value="3") 
    uservac3.place(x=305, y=175)
    uservac4=Radiobutton(covid_contact_tracing_app, text ='Second Booster',variable=radio,value='4')
    uservac4.place(x=405, y=175)
    uservac5=Radiobutton(covid_contact_tracing_app, text ='Not Yet Vaccinated',variable=radio,value='5')
    uservac5.place(x=525, y=175)
    


#make database



covid_gui()
covid_contact_tracing_app.mainloop()
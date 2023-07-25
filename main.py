#import tkinter
from tkinter import *
from tkinter import ttk
#create gui window
covid_contact_tracing_app = Tk()
covid_contact_tracing_app.title("COVID-19 CONTACT TRACING APP Version 1.0")
covid_contact_tracing_app.geometry("720x560")
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
    usergender.place(x=290, y=145)
    usergender_entry = ttk.Combobox(
    state="readonly",
    values=["Male", "Female", "Other", "Prefer not to say"]
)
    usergender_entry.place(width= 120, x=350, y=145)
    #user's contact
    usernumber=Label(covid_contact_tracing_app, text = "Contact No. : ")
    usernumber.place(x=500, y=145)
    usernumber_entry = Entry(covid_contact_tracing_app)
    usernumber_entry.place(width=120, x=585, y=145)
    #user's address
    userlot=Label(covid_contact_tracing_app, text = "House/Lot # : ")
    userlot.place(x=20, y=180)
    userlot_entry = Entry(covid_contact_tracing_app)
    userlot_entry.place(width=120, x=105, y=180)
    userbrgy=Label(covid_contact_tracing_app, text = "Baranggay : ")
    userbrgy.place(x=270, y=180)
    userbrgy_entry = Entry(covid_contact_tracing_app)
    userbrgy_entry.place(width=120, x=350, y=180)
    usercity=Label(covid_contact_tracing_app, text = "City/Town : ")
    usercity.place(x=500, y=180)
    usercity_entry = Entry(covid_contact_tracing_app)
    usercity_entry.place(width=120, x=585, y=180)
    userprovince=Label(covid_contact_tracing_app, text = "Province : ")
    userprovince.place(x=35, y=215)
    userprovince_entry = Entry(covid_contact_tracing_app)
    userprovince_entry.place(width=120, x=105, y=215)
    userregion = Label(covid_contact_tracing_app, text = "Region : ")
    userregion.place(width=120, x=470, y=215)
    userregion_entry = Entry(covid_contact_tracing_app)
    userregion_entry.place(width=120, x=585, y=215)
    #user's vaccination status
    uservacc=Label(covid_contact_tracing_app, text= 'Status :')
    uservacc.place(x=50, y=245)
    radio=IntVar()
    uservac1 = Radiobutton(covid_contact_tracing_app, text="First Dose",variable=radio,value="1") 
    uservac1.place(x=105, y=245)
    uservac2 = Radiobutton(covid_contact_tracing_app, text="Second Dose",variable=radio,value="2")
    uservac2.place(x=205, y=245)
    uservac3 = Radiobutton(covid_contact_tracing_app, text="First Booster",variable=radio,value="3") 
    uservac3.place(x=305, y=245)
    uservac4=Radiobutton(covid_contact_tracing_app, text ='Second Booster',variable=radio,value='4')
    uservac4.place(x=405, y=245)
    uservac5=Radiobutton(covid_contact_tracing_app, text ='Not Yet Vaccinated',variable=radio,value='5')
    uservac5.place(x=525, y=245)
    #user's symptoms
    usersymptoms = Label(covid_contact_tracing_app,text = "Symptoms experienced  : ")
    usersymptoms.place(x=20, y=280)
    usersymptoms_entry = ttk.Combobox(
    state="readonly",
    values=["Cough", "Fever", "Chills", "Sore throat", "Diarrhea", "Headache", "Shortness of breath", "Loss of smell or taste", "Others", "None of the above"]
)
    usersymptoms_entry.place(width= 200, x=170, y=280)
    #user's covid exposure
    userexposure = Label(covid_contact_tracing_app,text = "Recent exposure  : ")
    userexposure.place(x=400, y=280)
    userexposure_entry = ttk.Combobox(
    state="readonly",
    values=["Yes", "No", "Uncertain"]
)
    userexposure_entry.place(width= 200, x=500, y=280)
    
    #banner
    personalinfo=Label(covid_contact_tracing_app, text='Contact Person Details', font =( 'Arial', 10, 'bold', 'italic'))
    personalinfo.place(x=10, y=310)
    #contact's last name
    contactlastname = Label(covid_contact_tracing_app,text = "Last Name : ")
    contactlastname.place(x=25, y=340)
    contactlastname_entry = Entry(covid_contact_tracing_app)
    contactlastname_entry.place(width = 120, x=105, y=340)
    #contact's first name
    contactfirstname = Label(covid_contact_tracing_app,text = "First Name : ")
    contactfirstname.place(x=275, y=340)
    contactfirstname_entry = Entry(covid_contact_tracing_app)
    contactfirstname_entry.place(width= 120, x=350, y=340)
    #contact's middle name
    contactmiddlename = Label(covid_contact_tracing_app,text = "Middle Name : ")
    contactmiddlename.place(x=500, y=340)
    contactmiddlename_entry = Entry(covid_contact_tracing_app)
    contactmiddlename_entry.place(width =120, x=585, y=340)

#make database



covid_gui()
covid_contact_tracing_app.mainloop()
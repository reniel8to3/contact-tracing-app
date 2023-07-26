#create class for gui
#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class user_contact_info:
    def __init__(self):
        #create gui window
        #make gui for user input
        self.covid_contact_tracing_app = Tk()
        self.covid_contact_tracing_app.title("COVID-19 CONTACT TRACING APP Version 1.0")
        self.covid_contact_tracing_app.geometry("720x560")
        self.gui_label=Label(self.covid_contact_tracing_app, text='COVID-19 CONTACT TRACING APP', font =( 'Arial', 15, 'bold'))
        self.gui_label.pack(padx = 10, pady =10)
        self.gui_instruction=Label(self.covid_contact_tracing_app, text='Please fill up all the required details needed by contact tracing app.', font =( 'Arial', 10))
        self.gui_instruction.place(x=160, y=50)
        #banner
        self.personalinfo=Label(self.covid_contact_tracing_app, text='Respondent Details', font =( 'Arial', 10, 'bold', 'italic'))
        self.personalinfo.place(x=10, y=80)
        #user's last name
        userlastname = Label(self.covid_contact_tracing_app,text = "Last Name : ")
        userlastname.place(x=25, y=110)
        self.userlastname_entry = Entry(self.covid_contact_tracing_app)
        self.userlastname_entry.place(width = 120, x=105, y=110)
        #user's first name
        userfirstname = Label(self.covid_contact_tracing_app,text = "First Name : ")
        userfirstname.place(x=275, y=110)
        self.userfirstname_entry = Entry(self.covid_contact_tracing_app)
        self.userfirstname_entry.place(width= 120, x=350, y=110)
        #user's middle name
        usermiddlename = Label(self.covid_contact_tracing_app,text = "Middle Name : ")
        usermiddlename.place(x=500, y=110)
        self.usermiddlename_entry = Entry(self.covid_contact_tracing_app)
        self.usermiddlename_entry.place(width =120, x=585, y=110)
        #user's age
        userage = Label(self.covid_contact_tracing_app,text = "Age : ")
        userage.place(x=60, y=145)
        self.userage_entry = Entry(self.covid_contact_tracing_app)
        self.userage_entry.place(width=60, x=105, y=145)
        #user's gender
        usergender = Label(self.covid_contact_tracing_app,text = "Gender : ")
        usergender.place(x=290, y=145)
        self.usergender_entry = ttk.Combobox(
        state="readonly",
        values=["Male", "Female", "Other", "Prefer not to say"]
        )
        self.usergender_entry.place(width= 120, x=350, y=145)
        #user's contact
        usernumber=Label(self.covid_contact_tracing_app, text = "Contact No. : ")
        usernumber.place(x=500, y=145)
        self.usernumber_entry = Entry(self.covid_contact_tracing_app)
        self.usernumber_entry.place(width=120, x=585, y=145)
        #user's address
        userlot=Label(self.covid_contact_tracing_app, text = "House/Lot # : ")
        userlot.place(x=20, y=180)
        self.userlot_entry = Entry(self.covid_contact_tracing_app)
        self.userlot_entry.place(width=120, x=105, y=180)
        userbrgy=Label(self.covid_contact_tracing_app, text = "Baranggay : ")
        userbrgy.place(x=270, y=180)
        self.userbrgy_entry = Entry(self.covid_contact_tracing_app)
        self.userbrgy_entry.place(width=120, x=350, y=180)
        usercity=Label(self.covid_contact_tracing_app, text = "City/Town : ")
        usercity.place(x=500, y=180)
        self.usercity_entry = Entry(self.covid_contact_tracing_app)
        self.usercity_entry.place(width=120, x=585, y=180)
        userprovince=Label(self.covid_contact_tracing_app, text = "Province : ")
        userprovince.place(x=35, y=215)
        self.userprovince_entry = Entry(self.covid_contact_tracing_app)
        self.userprovince_entry.place(width=120, x=105, y=215)
        userregion = Label(self.covid_contact_tracing_app, text = "Region : ")
        userregion.place(width=120, x=470, y=215)
        self.userregion_entry = Entry(self.covid_contact_tracing_app)
        self.userregion_entry.place(width=120, x=585, y=215)
        #user's vaccination status
        uservacc=Label(self.covid_contact_tracing_app, text= 'Status :')
        uservacc.place(x=50, y=245)
        radio=IntVar()
        uservac1 = Radiobutton(self.covid_contact_tracing_app, text="First Dose",variable=radio,value="1") 
        uservac1.place(x=105, y=245)
        uservac2 = Radiobutton(self.covid_contact_tracing_app, text="Second Dose",variable=radio,value="2")
        uservac2.place(x=205, y=245)
        uservac3 = Radiobutton(self.covid_contact_tracing_app, text="First Booster",variable=radio,value="3") 
        uservac3.place(x=305, y=245)
        uservac4=Radiobutton(self.covid_contact_tracing_app, text ='Second Booster',variable=radio,value='4')
        uservac4.place(x=405, y=245)
        uservac5=Radiobutton(self.covid_contact_tracing_app, text ='Not Yet Vaccinated',variable=radio,value='5')
        uservac5.place(x=525, y=245)
        #user's symptoms
        usersymptoms = Label(self.covid_contact_tracing_app,text = "Symptoms experienced  : ")
        usersymptoms.place(x=20, y=280)
        usersymptoms_entry = ttk.Combobox(
        state="readonly",
        values=["Cough", "Fever", "Chills", "Sore throat", "Diarrhea", "Headache", "Shortness of breath", "Loss of smell or taste", "Others", "None of the above"]
        )
        usersymptoms_entry.place(width= 200, x=170, y=280)
        #user's covid exposure
        userexposure = Label(self.covid_contact_tracing_app,text = "Recent exposure  : ")
        userexposure.place(x=400, y=280)
        userexposure_entry = ttk.Combobox(
        state="readonly",
        values=["Yes", "No", "Uncertain"]
        )
        userexposure_entry.place(width= 200, x=500, y=280)

        #banner
        personalinfo=Label(self.covid_contact_tracing_app, text='Contact Person Details', font =( 'Arial', 10, 'bold', 'italic'))
        personalinfo.place(x=10, y=310)
        #contact's last name
        contactlastname = Label(self.covid_contact_tracing_app,text = "Last Name : ")
        contactlastname.place(x=25, y=340)
        contactlastname_entry = Entry(self.covid_contact_tracing_app)
        contactlastname_entry.place(width = 120, x=105, y=340)
        #contact's first name
        contactfirstname = Label(self.covid_contact_tracing_app,text = "First Name : ")
        contactfirstname.place(x=275, y=340)
        contactfirstname_entry = Entry(self.covid_contact_tracing_app)
        contactfirstname_entry.place(width= 120, x=350, y=340)
        #contact's middle name
        contactmiddlename = Label(self.covid_contact_tracing_app,text = "Middle Name : ")
        contactmiddlename.place(x=500, y=340)
        contactmiddlename_entry = Entry(self.covid_contact_tracing_app)
        contactmiddlename_entry.place(width =120, x=585, y=340)
        #contacts's age
        contactage = Label(self.covid_contact_tracing_app,text = "Age : ")
        contactage.place(x=60, y=370)
        contactage_entry = Entry(self.covid_contact_tracing_app)
        contactage_entry.place(width=60, x=105, y=370)
        #contact's gender
        contactgender = Label(self.covid_contact_tracing_app,text = "Gender : ")
        contactgender.place(x=290, y=370)
        contactgender_entry = ttk.Combobox(
        state="readonly",
        values=["Male", "Female", "Other", "Prefer not to say"]
        )
        contactgender_entry.place(width= 120, x=350, y=370)
        #contact's number
        contactnumber=Label(self.covid_contact_tracing_app, text = "Contact No. : ")
        contactnumber.place(x=500, y=370)
        contactnumber_entry = Entry(self.covid_contact_tracing_app)
        contactnumber_entry.place(width=120, x=585, y=370)
        #contacts's address
        contactlot=Label(self.covid_contact_tracing_app, text = "House/Lot # : ")
        contactlot.place(x=20, y=410)
        contactlot_entry = Entry(self.covid_contact_tracing_app)
        contactlot_entry.place(width=120, x=105, y=410)
        contactbrgy=Label(self.covid_contact_tracing_app, text = "Baranggay : ")
        contactbrgy.place(x=270, y=410)
        contactbrgy_entry = Entry(self.covid_contact_tracing_app)
        contactbrgy_entry.place(width=120, x=350, y=410)
        contactcity=Label(self.covid_contact_tracing_app, text = "City/Town : ")
        contactcity.place(x=500, y=410)
        contactcity_entry = Entry(self.covid_contact_tracing_app)
        contactcity_entry.place(width=120, x=585, y=410)
        contactprovince=Label(self.covid_contact_tracing_app, text = "Province : ")
        contactprovince.place(x=35, y=440)
        contactprovince_entry = Entry(self.covid_contact_tracing_app)
        contactprovince_entry.place(width=120, x=105, y=440)
        contactregion = Label(self.covid_contact_tracing_app, text = "Region : ")
        contactregion.place(width=120, x=190, y=440)
        contactregion_entry = Entry(self.covid_contact_tracing_app)
        contactregion_entry.place(width=120, x=280, y=440)
        #contact person relation
        contactrelation = Label(self.covid_contact_tracing_app, text = "Relation to contact person : ")
        contactrelation.place(x=430, y=440)
        contactrelation_entry = Entry(self.covid_contact_tracing_app)
        contactrelation_entry.place(width=120, x=585, y=440)
        #submit button
        submit_btn = Button(self.covid_contact_tracing_app, text="Submit", width="10")#extra function
        submit_btn.place(x=300, y=480)
        #search button
        search_field=Label(self.covid_contact_tracing_app,text='Search entries: ')
        search_field.place(x=180, y=520)
        search_field_entry=Entry(self.covid_contact_tracing_app)
        search_field_entry.place(width=120, x=280, y=520)
        #search button
        search_field_bttn=Button(self.covid_contact_tracing_app, text = 'Search') #extra function missing
        search_field_bttn.place(x=420, y=520)

    #def mainloop
    def mainloop(self):
        user_contact_info.mainloop()

    #register function
    def submit_records(self):
        last_name = self.userlastname_entry.get()
        first_name = self.userfirstname_entry.get()

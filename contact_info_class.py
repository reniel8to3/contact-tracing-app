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
        userregion.place(width=120, x=250, y=215)
        self.userregion_entry = Entry(self.covid_contact_tracing_app)
        self.userregion_entry.place(width=120, x=350, y=215)
        #user's vaccination status
        uservacc=Label(self.covid_contact_tracing_app, text= 'Status :')
        uservacc.place(x=515, y=215)
        self.uservacc_entry = ttk.Combobox(
        state="readonly",
        values=["First Dose", "Second Dose", "First Booster", "Second Booster", "Not Yet Vaccinated"]
        )
        self.uservacc_entry.place(width= 120, x=585, y=215)
        #user's symptoms
        usersymptoms = Label(self.covid_contact_tracing_app,text = "Symptoms experienced  : ")
        usersymptoms.place(x=20, y=245)
        self.usersymptoms_entry = ttk.Combobox(
        state="readonly",
        values=["Cough", "Fever", "Chills", "Sore throat", "Diarrhea", "Headache", "Shortness of breath", "Loss of smell or taste", "Others", "None of the above"]
        )
        self.usersymptoms_entry.place(width= 200, x=170, y=245)
        #user's covid exposure
        self.userexposure = Label(self.covid_contact_tracing_app,text = "Recent exposure  : ")
        self.userexposure.place(x=400, y=245)
        self.userexposure_entry = ttk.Combobox(
        state="readonly",
        values=["Yes", "No", "Uncertain"]
        )
        self.userexposure_entry.place(width= 200, x=500, y=245)

        #banner
        self.personalinfo=Label(self.covid_contact_tracing_app, text='Contact Person Details', font =( 'Arial', 10, 'bold', 'italic'))
        self.personalinfo.place(x=10, y=275)
        #contact's last name
        contactlastname = Label(self.covid_contact_tracing_app,text = "Last Name : ")
        contactlastname.place(x=25, y=305)
        self.contactlastname_entry = Entry(self.covid_contact_tracing_app)
        self.contactlastname_entry.place(width = 120, x=105, y=305)
        #contact's first name
        contactfirstname = Label(self.covid_contact_tracing_app,text = "First Name : ")
        contactfirstname.place(x=275, y=305)
        self.contactfirstname_entry = Entry(self.covid_contact_tracing_app)
        self.contactfirstname_entry.place(width= 120, x=350, y=305)
        #contact's middle name
        contactmiddlename = Label(self.covid_contact_tracing_app,text = "Middle Name : ")
        contactmiddlename.place(x=500, y=305)
        self.contactmiddlename_entry = Entry(self.covid_contact_tracing_app)
        self.contactmiddlename_entry.place(width =120, x=585, y=305)
        #contacts's age
        contactage = Label(self.covid_contact_tracing_app,text = "Age : ")
        contactage.place(x=60, y=345)
        self.contactage_entry = Entry(self.covid_contact_tracing_app)
        self.contactage_entry.place(width=60, x=105, y=345)
        #contact's gender
        contactgender = Label(self.covid_contact_tracing_app,text = "Gender : ")
        contactgender.place(x=290, y=345)
        self.contactgender_entry = ttk.Combobox(
        state="readonly",
        values=["Male", "Female", "Other", "Prefer not to say"]
        )
        self.contactgender_entry.place(width= 120, x=350, y=345)
        #contact's number
        contactnumber=Label(self.covid_contact_tracing_app, text = "Contact No. : ")
        contactnumber.place(x=500, y=345)
        self.contactnumber_entry = Entry(self.covid_contact_tracing_app)
        self.contactnumber_entry.place(width=120, x=585, y=345)
        #contacts's address
        contactlot=Label(self.covid_contact_tracing_app, text = "House/Lot # : ")
        contactlot.place(x=20, y=375)
        self.contactlot_entry = Entry(self.covid_contact_tracing_app)
        self.contactlot_entry.place(width=120, x=105, y=375)
        contactbrgy=Label(self.covid_contact_tracing_app, text = "Baranggay : ")
        contactbrgy.place(x=270, y=375)
        self.contactbrgy_entry = Entry(self.covid_contact_tracing_app)
        self.contactbrgy_entry.place(width=120, x=350, y=375)
        contactcity=Label(self.covid_contact_tracing_app, text = "City/Town : ")
        contactcity.place(x=500, y=375)
        self.contactcity_entry = Entry(self.covid_contact_tracing_app)
        self.contactcity_entry.place(width=120, x=585, y=375)
        contactprovince=Label(self.covid_contact_tracing_app, text = "Province : ")
        contactprovince.place(x=35, y=405)
        self.contactprovince_entry = Entry(self.covid_contact_tracing_app)
        self.contactprovince_entry.place(width=120, x=105, y=405)
        contactregion = Label(self.covid_contact_tracing_app, text = "Region : ")
        contactregion.place(width=120, x=190, y=405)
        self.contactregion_entry = Entry(self.covid_contact_tracing_app)
        self.contactregion_entry.place(width=120, x=280, y=405)
        #contact person relation
        contactrelation = Label(self.covid_contact_tracing_app, text = "Relation to contact person : ")
        contactrelation.place(x=430, y=405)
        self.contactrelation_entry = Entry(self.covid_contact_tracing_app)
        self.contactrelation_entry.place(width=120, x=585, y=405)
        #submit button
        self.submit_btn = Button(self.covid_contact_tracing_app, text="Submit", width="10")#extra function
        self.submit_btn.place(x=300, y=445)
        #search button
        search_field=Label(self.covid_contact_tracing_app,text='Search entries: ')
        search_field.place(x=180, y=485)
        self.search_field_entry=Entry(self.covid_contact_tracing_app)
        self.search_field_entry.place(width=120, x=280, y=485)
        #search button
        self.search_field_bttn=Button(self.covid_contact_tracing_app, text = 'Search') #extra function missing
        self.search_field_bttn.place(x=420, y=485)

    #def mainloop
    def mainloop(self):
        user_contact_info.mainloop()

    #register function
    def submit_records(self):
        user_last_name = self.userlastname_entry.get()
        user_first_name = self.userfirstname_entry.get()
        user_middle_name=self.usermiddlename_entry.get()
        user_age=self.userage_entry.get()
        user_gender=self.usergender_entry.get()
        user_contact_number=self.usernumber_entry.get()
        user_lot=self.userlot_entry.get()
        user_barangay=self.userbrgy_entry.get()
        user_city=self.usercity_entry.get()
        user_province=self.userprovince_entry.get()
        user_region=self.userregion_entry.get()
        user_vaccination=self.uservacc_entry.get()
        user_symptoms=self.usersymptoms_entry.get()
        user_exposure=self.userexposure_entry.get()
        contact_last_name=self.contactlastname_entry.get()
        contact_first_name=self.contactfirstname_entry.get()
        contact_middle_name=self.contactmiddlename_entry.get()
        contact_age=self.contactage_entry.get()
        contact_gender=self.contactgender_entry.get()
        contact_number=self.contactnumber_entry.get()
        contact_lot=self.contactlot_entry.get()
        contact_barangay=self.contactbrgy_entry.get()
        contact_city=self.contactcity_entry.get()
        contact_province=self.contactprovince_entry.get()
        contact_region=self.contactregion_entry.get()
        contact_relation=self.contactrelation_entry.get()
    


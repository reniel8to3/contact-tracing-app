#import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#make database
def covid_contact_tracing(info):
    with open("user_info.txt", "a") as entry_file:
        for key, value in info.items():
            entry_file.write(f"{key}: {value}\n")
        entry_file.write(str(info) + "\n")

#read and store data
def submit_records():
    user_data = {
        "User Last Name": userlastname_entry.get(),
        "User First Name": userfirstname_entry.get(),
        "User Middle Name": usermiddlename_entry.get(),
        "User Age": userage_entry.get(),
        "User Gender": usergender_entry.get(),
        "User Contact #": usernumber_entry.get(),
        "User Lot Address": userlot_entry.get(),
        "User Barangay Address": userbrgy_entry.get(),
        "User Town Address": usercity_entry.get(),
        "User Province Address": userprovince_entry.get(),
        "User Region Address": userregion_entry.get(),
        "User Vaccination Status": uservacc.get(),
        "User Symptoms": usersymptoms_entry.get(),
        "User COVID Exposure": userexposure_entry.get(),

        "Contact Last Name": contactlastname_entry.get(),
        "Contact First Name": contactfirstname_entry.get(),
        "Contact Middle Name": contactmiddlename_entry.get(),
        "Contact Age": contactage_entry.get(),
        "Contact Gender": contactgender_entry.get(),
        "Contact Contact #": contactnumber_entry.get(),
        "Contact Lot Address": contactlot.get(),
        "Contact Barangay Address": contactbrgy_entry.get(),
        "Contact Town Address": contactcity_entry.get(),
        "Contact Province Address": contactprovince_entry.get(),
        "Contact Region Address": contactregion_entry.get(),
        "Contact Relation": contactrelation_entry.get()
        
    }
    covid_contact_tracing(user_data)
    #ask user if data is correct
    response = messagebox.askyesno("Data Collection Complete!", "Do you want to save the data?")

    if response:
        covid_contact_tracing.destroy()

#create gui window
#make gui for user input
covid_contact_tracing_app = Tk()
covid_contact_tracing_app.title("COVID-19 CONTACT TRACING APP Version 1.0")
covid_contact_tracing_app.geometry("720x560")
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
userregion.place(width=120, x=250, y=215)
userregion_entry = Entry(covid_contact_tracing_app)
userregion_entry.place(width=120, x=350, y=215)
#user's vaccination status
uservacc=Label(covid_contact_tracing_app, text= 'Status :')
uservacc.place(x=515, y=215)
uservacc_entry = ttk.Combobox(
state="readonly",
values=["First Dose", "Second Dose", "First Booster", "Second Booster", "Not Yet Vaccinated"]
)
uservacc_entry.place(width= 120, x=585, y=215)
#user's symptoms
usersymptoms = Label(covid_contact_tracing_app,text = "Symptoms experienced  : ")
usersymptoms.place(x=20, y=245)
usersymptoms_entry = ttk.Combobox(
state="readonly",
values=["Cough", "Fever", "Chills", "Sore throat", "Diarrhea", "Headache", "Shortness of breath", "Loss of smell or taste", "Others", "None of the above"]
)
usersymptoms_entry.place(width= 200, x=170, y=245)
#user's covid exposure
userexposure = Label(covid_contact_tracing_app,text = "Recent exposure  : ")
userexposure.place(x=400, y=245)
userexposure_entry = ttk.Combobox(
state="readonly",
values=["Yes", "No", "Uncertain"]
)
userexposure_entry.place(width= 200, x=500, y=245)

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
#contacts's age
contactage = Label(covid_contact_tracing_app,text = "Age : ")
contactage.place(x=60, y=370)
contactage_entry = Entry(covid_contact_tracing_app)
contactage_entry.place(width=60, x=105, y=370)
#contact's gender
contactgender = Label(covid_contact_tracing_app,text = "Gender : ")
contactgender.place(x=290, y=370)
contactgender_entry = ttk.Combobox(
state="readonly",
values=["Male", "Female", "Other", "Prefer not to say"]
)
contactgender_entry.place(width= 120, x=350, y=370)
#contact's number
contactnumber=Label(covid_contact_tracing_app, text = "Contact No. : ")
contactnumber.place(x=500, y=370)
contactnumber_entry = Entry(covid_contact_tracing_app)
contactnumber_entry.place(width=120, x=585, y=370)
#contacts's address
contactlot=Label(covid_contact_tracing_app, text = "House/Lot # : ")
contactlot.place(x=20, y=410)
contactlot_entry = Entry(covid_contact_tracing_app)
contactlot_entry.place(width=120, x=105, y=410)
contactbrgy=Label(covid_contact_tracing_app, text = "Baranggay : ")
contactbrgy.place(x=270, y=410)
contactbrgy_entry = Entry(covid_contact_tracing_app)
contactbrgy_entry.place(width=120, x=350, y=410)
contactcity=Label(covid_contact_tracing_app, text = "City/Town : ")
contactcity.place(x=500, y=410)
contactcity_entry = Entry(covid_contact_tracing_app)
contactcity_entry.place(width=120, x=585, y=410)
contactprovince=Label(covid_contact_tracing_app, text = "Province : ")
contactprovince.place(x=35, y=440)
contactprovince_entry = Entry(covid_contact_tracing_app)
contactprovince_entry.place(width=120, x=105, y=440)
contactregion = Label(covid_contact_tracing_app, text = "Region : ")
contactregion.place(width=120, x=190, y=440)
contactregion_entry = Entry(covid_contact_tracing_app)
contactregion_entry.place(width=120, x=280, y=440)
#contact person relation
contactrelation = Label(covid_contact_tracing_app, text = "Relation to contact person : ")
contactrelation.place(x=430, y=440)
contactrelation_entry = Entry(covid_contact_tracing_app)
contactrelation_entry.place(width=120, x=585, y=440)
#submit button
submit_btn = Button(covid_contact_tracing_app, text="Submit", width="10")#extra function
submit_btn.place(x=300, y=480)
#search button
search_field=Label(covid_contact_tracing_app,text='Search entries: ')
search_field.place(x=180, y=520)
search_field_entry=Entry(covid_contact_tracing_app)
search_field_entry.place(width=120, x=280, y=520)
#search button
search_field_bttn=Button(covid_contact_tracing_app, text = 'Search') #extra function missing
search_field_bttn.place(x=420, y=520)



covid_contact_tracing_app.mainloop()
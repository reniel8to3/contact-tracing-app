#import modules
import tkinter
from tkinter import *

#import class
from contact_info_class import user_contact_info
from search_class import search
#create the gui for the main menu
class main:
    def __init__(self):
        #main window gui
        self.main = tkinter.Tk()
        self.main.title("COVID-19 CONTACT TRACING APP Version 1.0")
        self.main.geometry("480x360")
        self.gui_label=Label(self.main, text='COVID-19 CONTACT TRACING APP', font =( 'Arial', 15, 'bold'))
        self.gui_label.pack(padx = 10, pady =10)
        
        #register button
        register_button = Button(self.main, text="Register", font = (20), command=self.contact_info)
        register_button.place(width=100, height=30, x=180, y=120)
        #search button
        search_button = Button(self.main, text="Search", font = (20), command=self.search)
        search_button.place(width=100, height=30, x=180, y=200)
                
    def contact_info(self):
        open=user_contact_info()
        open.run()
    
    def search(self):
        open=search()
        open.run()

    # runs main menu
    def runMain(self):
        self.main.mainloop()

start=main()
start.runMain()
#import modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#import class
from contact_info_class import user_contact_info
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
        register_button = Button(self.main, text="Register", font = (30), command=self.contact_info)
        register_button.place(width=100, height=50, x=200, y=120)
    def contact_info(self):
        open=user_contact_info()
        open.run()
    # runs main menu
    def runMain(self):
        self.main.mainloop()

start=main()
start.runMain()
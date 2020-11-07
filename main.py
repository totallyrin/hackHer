"""
Code for QWIC hackHer 2020.

07/11/2020
"""

import tkinter as tk
from tkinter import messagebox

class Test():

    def go_to_study(self):
        current_focus = self.focus_entry.get()
        print(current_focus)
        self.next_button.pack_forget()
        self.focus_entry.pack_forget()
        self.text("")

    def get_focus_info(self):
        session_length = self.time_entry.get()
        print(session_length)
        self.text.set("How focused are you right now?")
        self.focus_entry.pack()
        self.get_survey_button.pack_forget()
        self.time_entry.pack_forget()
        self.next_button = tk.Button(text="Enter",
                                width=25,
                                height=5,
                                bg="cyan",
                                command=self.go_to_study)
        self.next_button.pack()


    def get_timer_info(self):
        self.text.set("Please enter the length of your study"+
         " session in minutes")
        self.time_entry.pack()
        self.start_button.pack_forget()
        self.get_survey_button = tk.Button(text="Enter",
                                width=25,
                                height=5,
                                bg="cyan",
                                command=self.get_focus_info)
        self.get_survey_button.pack()


    def __init__(self):
        self.window = tk.Tk()
        # set window size, width x height in pixels
        self.window.geometry("800x400")
        self.window.title("hackHer")
        self.text = tk.StringVar()
        self.text.set("hackHer")
        self.title = tk.Label(self.window, textvariable=self.text)
        self.title.pack()
        self.start_button = tk.Button(text="Click to start your study session!",
                           width=25,
                           height=5,
                           bg="cyan",
                           command=self.get_timer_info)
        self.start_button.pack()
        self.time_entry = tk.Entry(self.window)
        self.focus_entry = tk.Entry(self.window)

        #  GUI code goes before window.mainloop()
        self.window.mainloop()



app=Test()

"""
window = tk.Tk()
# set window size, width x height in pixels
window.geometry("800x400")
window.title("hackHer")
title = tk.Label(window, text = "hackHer2020")
title.pack()
button = tk.Button(text= "Click to start your study session!",
                   width = 25,
                   height = 5,
                   bg = "blue",
                   command = get_timer_info)
button.pack()



"""

"""
Code for QWIC hackHer 2020.

07/11/2020
"""

import tkinter as tk
import time
from threading import Thread
from tkinter import messagebox

session_length, current_focus, f1, f2 = 0.0, None, None, None


class Test:

    def timer(self):
        global session_length
        while float(session_length) / 60 > 0:
            hours, minutes = divmod(float(session_length), 60)
            minutes, seconds = divmod(minutes * 60, 60)
            hours, minutes, seconds = int(hours), int(minutes), int(seconds)
            timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.text.set("Time remaining: " + timer)
            print("time remaining" + timer)
            time.sleep(1)
            session_length = (float(session_length) * 60 - 1) / 60

    def clear_screen_objects(self):
        self.start_button.pack_forget()
        self.next_button.pack_forget()
        self.f1.pack_forget()
        self.f2.pack_forget()
        #  self.focus_entry.pack_forget()
        self.get_survey_button.pack_forget()
        self.time_entry.pack_forget()

    def go_to_study(self):
        """
        print(self.current_focus)
        self.clear_screen_objects()
        self.text.set("You are starting a study session that is" + str(
            self.session_length) +
                  " that will have *num* *length* sessions and *num* breaks." +
                  "Click Start Studying when you are ready!")
        # put below text as part of button press
        self.text.set("Time remaining in study session:")
        timer_thread = Thread(target=self.timer)
        timer_thread.start()"""
        # current_focus = self.focus_entry.get()
        print(current_focus)
        self.next_button.pack_forget()
        #self.focus_entry.pack_forget()
        self.text.set("Time remaining in study session:")
        timer_thread = Thread(target=self.timer)
        timer_thread.start()

    def set_focus(self):
        if self.f1:
            self.current_focus = self.f1
        else:
            self.current_focus = self.f2

    def get_focus_info(self):
        global session_length
        try:
            session_length = float(self.time_entry.get())
            if session_length < 1:
                self.get_timer_info()
            else:
                print(session_length)
                self.clear_screen_objects()
                self.text.set("How focused are you right now?")
                self.f1.pack()
                self.f2.pack()
                #  self.focus_entry.pack()
                self.next_button.pack()
        except:
            self.get_timer_info()

    def get_timer_info(self):
        self.clear_screen_objects()

        self.text.set("Please enter the length of your study" +
                      " session in minutes")
        self.time_entry.pack()
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

        self.start_button = tk.Button(
            text="Click to start your study session!",
            width=25,
            height=5,
            bg="cyan",
            command=self.get_timer_info)
        self.next_button = tk.Button(text="Enter",
                                     width=25,
                                     height=5,
                                     bg="cyan",
                                     command=self.go_to_study)
        self.get_survey_button = tk.Button(text="Enter",
                                           width=25,
                                           height=5,
                                           bg="cyan",
                                           command=self.get_focus_info)
        self.start_button.pack()

        self.time_entry = tk.Entry(self.window)
        #  self.focus_entry = tk.Entry(self.window)

        self.focus1 = tk.IntVar()
        self.f1 = tk.Checkbutton(self.window, text="very focused",
                                 variable=self.focus1,
                                 onvalue=1, offvalue=0,
                                 command=self.set_focus)
        self.focus2 = tk.IntVar()
        self.f2 = tk.Checkbutton(self.window, text="not focused",
                                 variable=self.focus2,
                                 onvalue=1, offvalue=0,
                                 command=self.set_focus)

        #  GUI code goes before window.mainloop()
        self.window.mainloop()


app = Test()

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

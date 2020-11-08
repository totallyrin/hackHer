"""
Code for QWIC hackHer 2020.

07/11/2020
"""

import tkinter as tk
import time
from threading import Thread
import tkinter.font as font

session_length, selection = 0.0, 0


class Test:

    def calc_breaks(self):
        """Calculate number of breaks and length of breaks given that
        session_length is a multiple of 15 or 20 """
        global session_length, selection
        numbreaks = 0
        break_interval = 0
        if not session_length < 30:
            if selection == 1:
                if session_length % 20 == 0:
                    numbreaks = divmod(session_length, 20)[0]
                    break_interval = 20
                elif session_length % 30 == 0:
                    numbreaks = divmod(session_length, 30)[0]
                    break_interval = 30
                elif session_length % 15 == 0:
                    numbreaks = divmod(session_length, 15)[0]
                    break_interval = 15
            elif selection == 2:
                if session_length % 20 == 0:
                    numbreaks = divmod(session_length, 20)[0]
                    break_interval = 20
                elif session_length % 15 == 0:
                    numbreaks = divmod(session_length, 15)[0]
                    break_interval = 15
        print(f"{numbreaks} breaks at {break_interval} mins each")
        return numbreaks, break_interval

    def timer(self):
        global session_length
        time_elapsed = 0
        num_breaks, break_interval = self.calc_breaks()
        while float(session_length) / 60 > 0:
            hours, minutes = divmod(float(session_length), 60)
            minutes, seconds = divmod(minutes * 60, 60)
            hours, minutes, seconds = int(hours), int(minutes), int(seconds)
            timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.text.set("Time remaining: " + timer)
            print("time remaining" + timer)
            time.sleep(1)
            if break_interval > 0 and num_breaks > 0:
                if divmod(time_elapsed, 60)[0] != 0 and divmod(time_elapsed,
                                                               60)[0] % \
                        break_interval == 0 and 0 < time_elapsed < session_length * 60:
                    # take a break!!
                    for second in range(1, 5 * 60):
                        break_timer = "{:02d}:{:02d}".format(divmod(5 * 60 -
                                                                    second,
                                                                    60)[0],
                                                             divmod(5 * 60 -
                                                                    second,
                                                                    60)[1])
                        self.text.set(
                            "Take a break! Break remaining: " + break_timer)
                        time.sleep(1)
            time_elapsed += 1
            session_length = (float(session_length) * 60 - 1) / 60
        print("timer finished")
        self.text.set("Session complete! Well done!")

    def clear_screen_objects(self):
        """This hides all of the graphic interfaces, such as buttons,
        when not in use """
        self.start_button.pack_forget()
        self.next_button.pack_forget()
        self.f1.pack_forget()
        self.f2.pack_forget()
        self.get_survey_button.pack_forget()
        self.time_entry.pack_forget()
        self.next_button.pack_forget()
        self.f1.pack_forget()
        self.f2.pack_forget()
        self.start_timer_button.pack_forget()

    def go_to_study(self):
        """This clears the screen after the user begins studying"""
        self.clear_screen_objects()
        timer_thread = Thread(target=self.timer)
        timer_thread.start()

    def are_you_ready(self):
        """This tells the user what their study session is going to look like in
        terms of how their time will be broken up"""
        global session_length, selection
        selection = self.focus.get()
        if selection == 0:
            self.get_focus_info()
        self.clear_screen_objects()
        if int(self.calc_breaks()[0]) == 0:
            self.text.set(
                f"You are starting a study session that is "
                f"{int(session_length)} minutes long and \n"
                f"will have no breaks. You can do this!\n"
                f"Click Start Studying when you are ready!")
        else:
            self.text.set(
                f"You are starting a study session that is a total of "
                f"{int(session_length) + 5 * int(self.calc_breaks()[0])} "
                f"minutes "
                f"long and\n "
                f"will have a total of {int(self.calc_breaks()[0])} break(s), "
                f"with a break every "
                f"{self.calc_breaks()[1]} "
                f"minutes.\n "
                f"Click Start Studying when you are ready!")
        self.start_timer_button.pack()

    def get_focus_info(self):
        """This determines if the user input a valid study length that is
        also correctly divisable by our chosen study time lengths. If yes,
        it asks the user to choose how focused they are which will determin
        how long their study lengths will be/how many breaks they will have.
        If not, it will make them enter their length again. """
        global session_length
        try:
            session_length = float(self.time_entry.get())
            if session_length < 15:
                self.get_timer_info()
            elif (int(round(session_length)) % 15 != 0 and int(
                    round(session_length)) % 20 != 0):
                self.get_timer_info()
            else:
                print(session_length)
                self.clear_screen_objects()
                self.text.set("How focused are you right now?")
                self.f1.pack()
                self.f2.pack()
                self.next_button.pack()
        except:
            self.get_timer_info()

    def get_timer_info(self):
        self.clear_screen_objects()

        self.text.set(
            "Please enter the total amount of time you wish \n to spend "
            "studying in minutes.Your time "
            "should \nbe divisable by either 15 or 20.")
        self.time_entry.pack()
        self.get_survey_button.pack()

    def __init__(self):
        """This sets up the GUI and creates all interacable objects used,
        such as buttons. """
        self.window = tk.Tk()
        # set window size, width x height in pixels, colour, window name
        self.window.geometry("800x350")
        self.window.configure(bg="#ffffff")
        self.window.title("hackHer 2020 - Chip Wright & Lucy Woloszczuk")

        # change fonts and creates text
        self.my_font = font.Font(family="Gill Sans MT", size=20)
        self.my_button_font = font.Font(family="Gill Sans MT", size=15)
        self.text = tk.StringVar()
        self.text.set("Welcome to the Pomodoro Technique Study Timer!")
        self.title = tk.Label(self.window, textvariable=self.text,
                              font=self.my_font, bg="#ffffff")
        self.title.pack()

        # creates the buttons
        self.start_button = tk.Button(
            text="Click to start your study session!",
            width=25,
            height=5,
            bg="#99aab5",
            command=self.get_timer_info)
        self.start_button['font'] = self.my_button_font
        self.next_button = tk.Button(text="Enter", width=25, height=5,
                                     bg="#99aab5",
                                     command=self.are_you_ready)
        self.next_button['font'] = self.my_button_font
        self.get_survey_button = tk.Button(text="Enter",
                                           width=25,
                                           height=5,
                                           bg="#99aab5",
                                           command=self.get_focus_info)
        self.get_survey_button['font'] = self.my_button_font
        self.start_timer_button = tk.Button(text="Start Studying",
                                            width=25,
                                            height=5,
                                            bg="#99aab5",
                                            command=self.go_to_study)
        self.start_timer_button['font'] = self.my_button_font
        self.start_button.pack()

        self.time_entry = tk.Entry(self.window)
        self.focus = tk.IntVar()
        self.focus.set(0)
        self.f1 = tk.Radiobutton(self.window, text="very focused",
                                 variable=self.focus, value=1, bg="#ffffff")
        self.f2 = tk.Radiobutton(self.window, text="not focused",
                                 variable=self.focus, value=2, bg="#ffffff")

        #  GUI code goes before window.mainloop()
        self.window.mainloop()


app = Test()

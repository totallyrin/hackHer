"""
Code for QWIC hackHer 2020.

07/11/2020
"""

import tkinter as tk
import tkinter.font as font
import time
from threading import Thread

session_length, current_focus, selection = 0.0, None, 0


def calc_breaks():
    """Calculate number of breaks and length of breaks given that
    session_length is a multiple of 15 or 20 """
    global session_length, selection
    num_breaks = 0
    break_interval = 0
    if not session_length < 30:
        if selection == 1:
            if session_length % 20 == 0:
                num_breaks = divmod(session_length, 20)[0]
                break_interval = 20
            elif session_length % 30 == 0:
                num_breaks = divmod(session_length, 30)[0]
                break_interval = 30
            elif session_length % 15 == 0:
                num_breaks = divmod(session_length, 15)[0]
                break_interval = 15
        elif selection == 2:
            if session_length % 20 == 0:
                num_breaks = divmod(session_length, 20)[0]
                break_interval = 20
            elif session_length % 15 == 0:
                num_breaks = divmod(session_length, 15)[0]
                break_interval = 15
    print(f"{num_breaks} breaks at {break_interval} mins each")
    return num_breaks, break_interval


class Test:

    def timer(self):
        global session_length
        time_elapsed = 0
        num_breaks, break_interval = calc_breaks()
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
                        break_interval == 0 and 0 < time_elapsed < \
                        session_length * 60:
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
        self.clear_screen_objects()
        self.text.set("Time remaining in study session:")
        timer_thread = Thread(target=self.timer)
        timer_thread.start()

    def are_you_ready(self):
        global session_length, selection
        selection = self.focus.get()

        if selection == 0:
            self.get_focus_info()

            self.clear_screen_objects()

            self.text.set(
                f"You are starting a study session that is {session_length} "
                f"minutes long and that "
                f"will have a total of {int(calc_breaks()[0])} break(s), "
                f"with a break every "
                f"{calc_breaks()[1]} "
                f"minutes.\n "
                f"Click Start Studying when you are ready!")
            self.start_timer_button.pack()

    def get_focus_info(self):
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
            "Please enter the length of your study session in minutes.\n "
            "Your time "
            "should be divisible by either 15 or 20")
        self.time_entry.pack()
        self.get_survey_button.pack()

    def __init__(self):

        self.window = tk.Tk()
        # set window size, width x height in pixels
        self.window.geometry("500x200")
        self.my_font = font.Font(family="Gill Sans MT", size=16, )
        self.my_button_font = font.Font(family="Gill Sans MT", size=20)
        self.window.title("hackHer 2020 - Chip Wright & Lucy Woloszczuk")
        self.text = tk.StringVar()
        self.text.set("Welcome to the Pomodoro technique \nwork timer!")
        self.title = tk.Label(self.window, textvariable=self.text,
                              font=self.my_font)
        self.title.pack()

        self.start_button = tk.Button(
            text="Click to start your study session!",
            width=25,
            height=5,
            bg="#99aab5",
            command=self.get_timer_info)
        self.next_button = tk.Button(text="Enter", width=25, height=5,
                                     bg="#99aab5", command=self.are_you_ready)
        self.get_survey_button = tk.Button(text="Enter",
                                           width=25,
                                           height=5,
                                           bg="#99aab5",
                                           command=self.get_focus_info)
        self.start_timer_button = tk.Button(text="Start Studying",
                                            width=25,
                                            height=5,
                                            bg="#99aab5",
                                            command=self.go_to_study)
        self.start_button.pack()

        self.time_entry = tk.Entry(self.window)
        #  self.focus_entry = tk.Entry(self.window)
        self.focus = tk.IntVar()
        self.focus.set(0)
        self.f1 = tk.Radiobutton(self.window, text="very focused",
                                 variable=self.focus, value=1)
        self.f2 = tk.Radiobutton(self.window, text="not focused",
                                 variable=self.focus, value=2)

        #  GUI code goes before window.mainloop()
        self.window.mainloop()


app = Test()

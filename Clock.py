from tkinter import *
from threading import*
import time
import datetime
import winsound

root = Tk()
root.title('Clock')
root.geometry("350x400")

"""
--------------------------------
Alarm Clock
--------------------------------
"""
def alarm_feature():
    newWindow = Toplevel(root)
    newWindow.title("Alarm Clock")
    newWindow.geometry("300x180")

    def thread():
        t1 = Thread(target=alarm)
        t1.start()

    def alarm():
        while True:
            set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"

            time.sleep(1)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            alarm_time = datetime.datetime.now().strftime("%H:%M")
            print(current_time, set_alarm)

            if current_time == set_alarm:
                global wakeup
                wakeup = Toplevel(root)
                wakeup.title("Alarm Clock")
                wakeup.geometry("400x180")
                wakeup.resizable(0, 0)

                Label(wakeup, text=alarm_time, font=('Times New Roman', 30, 'bold')).pack()
                Button(wakeup, text='Dismiss', font=('Times New Roman', 20, 'bold'), command=dismiss).pack(pady=15)

                winsound.PlaySound("igotyoubabe.wav", winsound.SND_ASYNC)

    def dismiss():
        wakeup.destroy()
        winsound.PlaySound(None, winsound.SND_FILENAME)

    frame = Frame(newWindow)
    frame.pack()

    hour = StringVar(newWindow)
    hours = (
    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
    '20', '21', '22', '23', '24')
    hour.set('-')
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    minute = StringVar(newWindow)
    minutes = (
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
    '19', '20', '21',
    '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
    '41', '42', '43',
    '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
    minute.set('-')
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    second = StringVar(newWindow)
    second.set('00')

    Button(newWindow, text="Set Alarm", font=("Times New Roman", 20, 'bold'), command=thread, bg = 'goldenrod').pack(pady=15)
"""
--------------------------------
Timer
--------------------------------
"""
def timer_feature():
    newWindow = Toplevel(root)
    newWindow.title("Timer")
    newWindow.geometry("300x180")

    hours = StringVar()
    hours.set("00")
    minutes = StringVar()
    minutes.set("00")
    seconds = StringVar()
    seconds.set("00")

    timer = Frame(newWindow)
    hourtimer = Entry(timer, font=("Times New Roman", 25, "bold"), textvariable=hours, width=2)
    colon1 = Label(timer, font=("Times New Roman", 25, "bold"), text=":")
    minutetimer = Entry(timer, font=("Times New Roman", 25, "bold"), textvariable=minutes, width=2)
    colon2 = Label(timer, font=("Times New Roman", 25, "bold"), text=":")
    secondtimer = Entry(timer, font=("Times New Roman", 25, "bold"), textvariable=seconds, width=2)

    hourtimer.pack(side='left')
    colon1.pack(side='left')
    minutetimer.pack(side='left')
    colon2.pack(side='left')
    secondtimer.pack(side='left')
    timer.pack(pady=20)

    def display_timer():
        try:
            input = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
        except:
            print("Invalid input")
        while input > -1:
            mins, secs = divmod(input, 60)
            hrs = 0

            if mins > 60:
                hrs, mins = divmod(mins, 60)

            hours.set(str(hrs).zfill(2))
            minutes.set(str(mins).zfill(2))
            seconds.set(str(secs).zfill(2))

            newWindow.update()
            time.sleep(1)

            if (input == 0):
                winsound.PlaySound("timerbeep.wav", winsound.SND_ASYNC)
            input -= 1

    start_button = Button(newWindow, text="START", font=("Times New Roman", 14, "bold"), command=display_timer,
                          bg='goldenrod')
    start_button.pack(pady=20)
"""
--------------------------------
Stopwatch
--------------------------------
"""

hours = 0
minutes = 0
seconds = 0
time1 = 0
time2 = 0

def stopwatch_feature():

    newWindow = Toplevel(root)
    newWindow.title("Stopwatch")
    newWindow.geometry("500x180")

    def start():
        start_button.place_forget()
        stop_button.pack()
        global hours, minutes, seconds, time1, run, time2
        time2 = int(time.time())
        if time2 != time1:
            time1 = time2

            if seconds < 59:
                seconds += 1
                stopwatch.config(text=(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)))
            else:
                seconds = 0

                if minutes < 59:
                    minutes += 1
                    stopwatch.config(
                        text=(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)))
                else:
                    minutes = 0

                    if hours >= 24:
                        seconds = 0
                        minutes = 0
                        hours = 0

                    else:
                        hours += 1
                        stopwatch.config(
                            text=(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2)))

        run = newWindow.after(1000, start)

    def stop():
        global run
        if run is not None:
            newWindow.after_cancel(run)
            run = None
        stop_button.place_forget()
        resume_button.pack()

    def reset():
        global hours, minutes, seconds, time1, run, time2
        try:
            stop()
        except:
            start()
            stop()

        stopwatch.config(text='00:00:00')
        hours = 0
        minutes = 0
        seconds = 0
        time1 = 0
        time2 = 0

        show_button = newWindow.winfo_children()
        for i in show_button:
            i.place_forget()
            resume_button.place_forget()

        buttons = Frame(root)
        stopwatch.pack()
        start_button.pack(side='left')
        reset_button.pack(side='left')
        buttons.pack()

    buttons = Frame(newWindow)
    stopwatch = Label(buttons, text='00:00:00', font=("Times New Roman", 35, "bold"))
    start_button = Button(buttons, text='Start', font=("Times New Roman", 25, "bold"), command=start, bg = 'goldenrod')
    resume_button = Button(buttons, text='Resume', font=("Times New Roman", 25, "bold"), command=start, bg = 'goldenrod')
    stop_button = Button(buttons, text='Stop', font=("Times New Roman", 25, "bold"), command=stop, bg = 'goldenrod')
    reset_button = Button(buttons, text='Reset', font=("Times New Roman", 25, "bold"), command=reset, bg = 'goldenrod')

    stopwatch.pack(pady=20)

    start_button.pack(side='left')
    stop_button.pack(side='left')
    resume_button.pack(side='left')
    reset_button.pack(side='left')
    buttons.pack(pady=20)

"""
--------------------------------
Main
--------------------------------
"""
alarm = PhotoImage(file="alarmclock.png")
alarm_icon = alarm.subsample(9, 9)
alarm_clock = Button(root, text = "Alarm Clock ", image = alarm_icon, font=("Times New Roman", 25, "bold"), command = alarm_feature, compound = "right")
alarm_clock.pack(pady = 20)
hourglass = PhotoImage(file="hourglass.png")
hourglass_icon = hourglass.subsample(9, 9)
timer = Button(root, text = "Timer", image = hourglass_icon, font=("Times New Roman", 25, "bold"), command = timer_feature, compound = "right")
timer.pack(pady = 20)
stopwatch_pic = PhotoImage(file="stopwatch.png")
stopwatch_icon = stopwatch_pic.subsample(10, 10)
stopwatch = Button(root, text = " Stopwatch", image = stopwatch_icon, font=("Times New Roman", 25, "bold"), command = stopwatch_feature, compound = "left")
stopwatch.pack(pady = 20)

root.mainloop()

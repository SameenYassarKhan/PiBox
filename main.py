from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import random


"""
--------------------------------
Main Window Specifications
--------------------------------
"""
root = Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')
root.resizable(False, False)
p1 = PhotoImage(file='MyComputer/Login/Untitled_Artwork-1.PNG')
root.iconbitmap(p1)
root.iconphoto(False, p1)

"""
--------------------------------
New Wallpaper
--------------------------------
"""
wallpaper_list = [
        "MyComputer/BackgroundImage/legendaryGreen.jpg",
        "MyComputer/BackgroundImage/legendaryGreenCracked.jpg",
        "MyComputer/BackgroundImage/legendaryGreenFood.jpg",
        "MyComputer/BackgroundImage/legendaryGreenPsyDuck.png",
        "MyComputer/BackgroundImage/legendaryGreenThanos.jpg",
        "MyComputer/BackgroundImage/legendaryGreenWeird.jpg",
        "MyComputer/BackgroundImage/legendaryGreenWicked.png",
        "MyComputer/BackgroundImage/legendaryGreenWubuffet.png",
        "MyComputer/BackgroundImage/legendaryGreenZelda.png"
    ]
random_num = random.randint(0, len(wallpaper_list)-1)
img_wallpaper = ImageTk.PhotoImage(
    Image.open(wallpaper_list[random_num]).resize((
        root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS))
lbl_wallpaper = Label(root, image=img_wallpaper)
lbl_wallpaper.pack()

"""
--------------------------------
Application Tray
--------------------------------
"""
lf_appTray = LabelFrame(root, text="Application Tray")
lf_appTray.place(in_=root, relx=1, rely=0.5, anchor=SE)

btn_notepad = Button(lf_appTray, text="Notepad--")
btn_notepad.pack()

btn_grapher = Button(lf_appTray, text="Grapher")
btn_grapher.pack()

btn_drawing = Button(lf_appTray, text="Drawing")
btn_drawing.pack()

btn_calculator = Button(lf_appTray, text="Calculator")
btn_calculator.pack()

btn_drawing = Button(lf_appTray, text="Quit", command=root.quit)
btn_drawing.pack()

# New Window Format
# new_label = LabelFrame(root)
# new_label.place(in_=lbl_wallpaper, relx=0.5, rely=0.5, anchor=CENTER)
# button2 = Button(new_label, text="I am inside the label frame")
# button2.pack()

# To run a file in shortcut
# os.startfile("C:\\Windows||System32\\notepad.exe")
mainloop()

from tkinter import *
from tkinter import filedialog
from tkinter.font import Font
from tkinter.ttk import *
from PIL import ImageTk, Image
import random
from bs4 import BeautifulSoup
import requests
from tkinter import ttk, colorchooser
import time


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
    "MyComputer/BackgroundImage/legendaryGreenFood.jpg",
    "MyComputer/BackgroundImage/legendaryGreenPsyDuck.png",
    "MyComputer/BackgroundImage/legendaryGreenThanos.jpg",
    "MyComputer/BackgroundImage/legendaryGreenWeird.jpg",
    "MyComputer/BackgroundImage/legendaryGreenWicked.png",
    "MyComputer/BackgroundImage/legendaryGreenWubuffet.png",
    "MyComputer/BackgroundImage/legendaryGreenZelda.png"
]
random_num = random.randint(0, len(wallpaper_list) - 1)
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
font_default = Font(
    family="Comic Sans MS",
    size=20,
    weight="bold",
    slant="roman",
    underline=0,
    overstrike=0
)

"""
--------------------------------
Notepad--
--------------------------------
"""


def open_notepad_frame():
    global open_status_name
    open_status_name = False

    def save_as_file():
        text_file = filedialog.asksaveasfilename(
            defaultextension=".*",
            initialdir="MyComputer/Notepad--",
            title="Save File",
            filetypes=(("Text Files", "*.txt"),
                       ("HTML Files", "*.html"),
                       ("Python Files", "*.py"),
                       ("All Files", "*.*")))
        if text_file:
            name = text_file
            splitted_list = name.split("/")
            status_bar.config(text=f'Saved: {name}        ')

            # Save file
            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))
            text_file.close()
            status_bar.config(text=f"Saved: {open_status_name}")
        else:
            save_as_file()

    # Save File
    def save_file():
        global open_status_name
        if open_status_name:
            text_file = open(open_status_name, 'w')
            text_file.write(my_text.get(1.0, END))
            text_file.close()

            status_bar.config(text=f'Saved: {open_status_name}')
        else:
            save_as_file()

    def new_file():
        my_text.delete("1.0", END)
        # Update Status Bars
        status_bar.config(text="New File        ")
        global open_status_name
        open_status_name = False

    def open_file():
        # Delete previous Text
        my_text.delete("1.0", END)
        # Grab Filename
        text_file = filedialog.askopenfilename(
            initialdir="MyComputer/Notepad--",
            title="Open File",
            filetypes=(("Text Files", "*.txt"),
                       ("HTML Files", "*.html"),
                       ("Python Files", "*.py"),
                       ("All Files", "*.*")))
        # Check to see if there is a file name
        if text_file:
            # Store the filename for later use
            global open_status_name
            open_status_name = text_file
        # Update Status Bars
        name = text_file
        splitted_list = name.split("/")
        status_bar.config(text=f'{name}        ')

        # Open the file
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        # Add file to textbox
        my_text.insert(END, stuff)
        # Close the opened file
        text_file.close()

    lf_notepad_frame = LabelFrame(root, text="Notepad--")
    lf_notepad_frame.place_configure(in_=root, relx=0.5, rely=0.1, height=570, width=900, anchor=N)
    # Create Main Frame
    my_frame = Frame(lf_notepad_frame)
    my_frame.pack(pady=5)
    # Create a scrollbar for the text box
    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)
    # Create Text Box
    my_text = Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow",
                   selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    my_text.pack()
    # Configure our scrollbar
    text_scroll.config(command=my_text.yview)
    status_bar = Label(lf_notepad_frame, text="Ready        ", anchor=E)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)

    btn_new = Button(lf_notepad_frame, width=10, text="New", command=new_file)
    btn_new.pack(side=LEFT)

    btn_open = Button(lf_notepad_frame, width=10, text="Open", command=open_file)
    btn_open.pack(side=LEFT)

    btn_save = Button(lf_notepad_frame, width=10, text="Save", command=save_file)
    btn_save.pack(side=LEFT)

    btn_save_as = Button(lf_notepad_frame, width=10, text="Save As", command=save_as_file)
    btn_save_as.pack(side=LEFT)

    btn_exit = Button(lf_notepad_frame, width=10, text="Exit", command=lf_notepad_frame.destroy)
    btn_exit.pack(side=LEFT)


"""
--------------------------------
Web Browser
--------------------------------
"""


def open_browsing_frame():
    lf_browsing_frame = LabelFrame(root, text="Park")
    lf_browsing_frame.place_configure(in_=root, relx=0.5, rely=0.1, height=510, width=900, anchor=N)

    btn_exit = Button(lf_browsing_frame, width=10, text="Exit", command=lf_browsing_frame.destroy)
    btn_exit.place(x=45, y=0)

    # # https://google.com/search?q=<Query>
    entry_web_input_field = Entry(lf_browsing_frame, justify='center', width=50)
    entry_web_input_field.pack()
    # keyword = entry_web_input_field.get()
    #
    text_scroll = Scrollbar(lf_browsing_frame)
    text_scroll.pack(side=RIGHT, fill=Y)
    text_search_results_frame = Text(lf_browsing_frame, width=97, height=25, font=("Helvetica", 16),
                                     selectbackground="yellow",
                                     selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
    text_search_results_frame.pack()
    # # Configure our scrollbar
    text_scroll.config(command=text_search_results_frame.yview)
    # # Main Webscraping Process
    stored_keyword = False

    def web_request():
        text_search_results_frame.delete("1.0", END)
        searched_keyword = entry_web_input_field.get()
        url = f"https://google.com/search?q={searched_keyword}"
        stored_keyword = searched_keyword
        entry_web_input_field.delete(0, END)
        entry_web_input_field.insert(END, url)
        #     url = "".join(['https://google.com/search?q=', str(keyword)])
        #     print(keyword)
        #     print(url)
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        #    text_search_results_frame.insert(END, soup)
        heading_object = soup.find_all('h3')
        # linking_object = soup.find_all('cite')
        # print(linking_object)
        #   text_search_results_frame.insert(END, heading_object)
        #
        #     # Iterate through the object
        #     # and print it as a string.
        text_search_results_frame.insert(END, "------------------\nHEADLINES\n------------------\n")
        count = 1
        for info in heading_object:
            text_search_results_frame.insert(END, (str(count) + ") "))
            text_search_results_frame.insert(END, info.getText())
            text_search_results_frame.insert(END, "\n")
            count += 1

        text_search_results_frame.insert(END, "\n----------\nLINKS\n----------\n")
        count = 1
        special_links = soup.select("div a")
        for i in special_links:
            # if i.contains("/url?1="):
            strings_special = str(i.get('href'))
            if strings_special.find("/url?q=") >= 0:
                text_search_results_frame.insert(END, "\n" + str(count) + ") ")
                text_search_results_frame.insert(END, strings_special[7:])
                text_search_results_frame.insert(END, "\n")
                count += 1
            # text_search_results_frame.insert(END, "\n")

    #         print(info.getText())
    #         print("------")

    def inspect_element():
        text_search_results_frame.delete("1.0", END)
        url = f"https://google.com/search?q={stored_keyword}"
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        text_search_results_frame.insert(END, soup)

    btn_search = Button(lf_browsing_frame, width=10, text="Search", command=web_request)
    btn_search.place(x=720, y=0)

    btn_inspect = Button(lf_browsing_frame, width=1.1, text="{?}", command=inspect_element)
    btn_inspect.place(x=168, y=0)


"""
--------------------------------
Graphing Application
--------------------------------
"""


def open_grapher_frame():
    lf_grapher_frame = LabelFrame(root, text="Grapher")
    lf_grapher_frame.place_configure(in_=root, relx=0.5, rely=0.1, height=510, width=900, anchor=N)


"""
--------------------------------
Drawing Application
--------------------------------
"""


def open_drawing_frame():
    lf_drawing_frame = LabelFrame(root, text="Paint")
    lf_drawing_frame.place_configure(in_=root, relx=0.5, rely=0.1, height=600, width=900, anchor=N)

    lf_button_tray = LabelFrame(lf_drawing_frame, text="____________\n      TOOLS\n____________")
    lf_button_tray.pack(side=RIGHT, fill=Y)

    class main:
        def __init__(self, master):
            self.master = master
            self.color_fg = 'black'
            self.color_bg = 'white'
            self.old_x = None
            self.old_y = None
            self.penwidth = 5
            self.drawWidgets()
            self.c.bind('<B1-Motion>', self.paint)  # drwaing the line
            self.c.bind('<ButtonRelease-1>', self.reset)

        def paint(self, e):
            if self.old_x and self.old_y:
                self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                                   capstyle=ROUND, smooth=True)

            self.old_x = e.x
            self.old_y = e.y

        def reset(self, e):  # reseting or cleaning the canvas
            self.old_x = None
            self.old_y = None

        def changeW(self, e):  # change Width of pen through slider
            self.penwidth = e

        def clear(self):
            self.c.delete(ALL)

        def change_fg(self):  # changing the pen color
            self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

        def change_bg(self):  # changing the background color canvas
            self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]
            self.c['bg'] = self.color_bg

        def drawWidgets(self):
            self.controls = Frame(self.master)
            Label(self.controls, text='Pen Width:', font=('arial 18')).grid(row=0, column=0)
            self.slider = ttk.Scale(self.controls, from_=5, to=100, command=self.changeW, orient=HORIZONTAL)
            self.slider.set(self.penwidth)
            self.slider.grid(row=0, column=1, ipadx=30)
            self.controls.pack(side=LEFT)

            self.c = Canvas(self.master, width=500, height=500, bg=self.color_bg, )
            self.c.pack(fill=BOTH, expand=True)

            btn_brush_color = Button(lf_button_tray, width=10, text="Brush Color", command=self.change_fg)
            btn_brush_color.pack()

            btn_bg_color = Button(lf_button_tray, width=10, text="BG Color", command=self.change_bg)
            btn_bg_color.pack()

            btn_clear = Button(lf_button_tray, width=10, text="Clear Canvas", command=self.clear)
            btn_clear.pack()

            btn_exit = Button(lf_button_tray, width=10, text="Exit", command=lf_drawing_frame.destroy)
            btn_exit.pack()

    main(lf_drawing_frame)


"""
--------------------------------
Todo List Application
--------------------------------
"""


def open_todo_frame():
    lf_todo_frame = LabelFrame(lf_appTray, text="__________________\n         AGENDA\n__________________")
    lf_todo_frame.place_configure(in_=lf_appTray, relx=0.5, rely=0.3, height=300, width=150, anchor=N)

    agenda_input_field = Entry(lf_todo_frame, width=9)
    agenda_input_field.place(x=10, y=0)

    my_listbox = Listbox(lf_todo_frame, width=16)
    my_listbox.place(x=0, y=30)

    def add_task():
        my_listbox.insert(END, agenda_input_field.get())

    def delete():
        my_listbox.delete(ANCHOR)

    btn_add = Button(lf_todo_frame, text="+", width=1, command=add_task)
    btn_add.place(x=100, y=0)

    btn_complete_mark = Button(lf_todo_frame, text="Completed", width=10, command=delete)
    btn_complete_mark.place(x=12, y=205)


"""
--------------------------------
Calculator Application
--------------------------------
"""


def open_calculator_frame():
    lf_calculator_frame = LabelFrame(root, text="Calculator")
    lf_calculator_frame.place_configure(in_=root, relx=1, rely=1, height=510, width=900, anchor=N)


lf_appTray = LabelFrame(root, text="________________\nAPPLICATION TRAY\n________________")
btn_documentation = Button(lf_appTray, width=10, text="About PIBox", command=open_browsing_frame)
btn_documentation.pack()

lf_appTray.place(in_=root, relx=1, rely=1, height=root.winfo_screenheight(), width=150, anchor=SE)

btn_notepad = Button(lf_appTray, width=10, text="Notepad--", command=open_notepad_frame)
btn_notepad.pack()

btn_grapher = Button(lf_appTray, width=10, text="Grapher", command=open_grapher_frame)
btn_grapher.pack()

btn_web_browser = Button(lf_appTray, width=10, text="Park", command=open_browsing_frame)
btn_web_browser.pack()

btn_todo = Button(lf_appTray, width=10, text="Agenda", command=open_todo_frame)
btn_todo.pack()

btn_sticky_note = Button(lf_appTray, width=10, text="Sticky Note", command=open_notepad_frame)
btn_sticky_note.pack()

btn_settings = Button(lf_appTray, width=10, text="Settings")
btn_settings.pack()

btn_email = Button(lf_appTray, width=10, text="Email")
btn_email.pack()

btn_drawing = Button(lf_appTray, width=10, text="Drawing", command=open_drawing_frame)
btn_drawing.pack()

btn_calculator = Button(lf_appTray, width=10, text="Calculator", command=open_calculator_frame)
btn_calculator.pack()

btn_my_computer = Button(lf_appTray, width=10, text="My Computer")
btn_my_computer.pack()

btn_drawing = Button(lf_appTray, width=10, text="Quit", command=root.quit)
btn_drawing.pack()

# New Window Format
# new_label = LabelFrame(root)
# new_label.place(in_=lbl_wallpaper, relx=0.5, rely=0.5, anchor=CENTER)
# button2 = Button(new_label, text="I am inside the label frame")
# button2.pack()

# To run a file in shortcut
# os.startfile("C:\\Windows||System32\\notepad.exe")
mainloop()

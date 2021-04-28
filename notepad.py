from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('Notepad--')
root.geometry("900x510")

# Set the variable for open file name
global open_status_name
open_status_name = False

# Save As File
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
        root.title(f'{splitted_list[len(splitted_list) - 1]} - Notepad--')

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

# Create New File Function
def new_file():
    my_text.delete("1.0", END)
# Update Status Bars
    root.title("New File - NotePad--")
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
    root.title(f'{splitted_list[len(splitted_list)-1]} - Notepad--')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox
    my_text.insert(END, stuff)
    # Close the opened file
    text_file.close()

# Create Main Frame
my_frame = Frame(root)
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

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

# Add Status Bar
status_bar = Label(root, text="Ready        ", anchor=E, bg='grey')
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()

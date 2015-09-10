#!/usr/bin/python

from tkinter import *
from tkinter.ttk import Notebook
import tkinter.filedialog as tkfd
import tkinter.messagebox

#-----------------------------------Initialization-----------------------------------
# Create the root of the GUI and its title/dimensions:
root = Tk()
root.title('PyCon GUI')
root.geometry('600x500')

# Setup tabs via a "notebook":
notebook = Notebook(root)
notebook.pack(fill=BOTH, expand=Y, side=TOP)

# Initialize the different tabs, i.e., frames:
f1 = Frame(notebook)
f2 = Frame(notebook)
f3 = Frame(notebook)

#-----------------------------Tab 1: Dropdown and Listbox----------------------------
# Dropdown Menu first:
some_string = StringVar(f1)     # Attach variables and widgets to f1, not root
some_string.set('drop down menu button')

def grab_and_assign(event):
    # Callback function for the option menu
    chosen_option = some_string.get()
    label_chosen_variable = Label(f1, text=chosen_option)
    label_chosen_variable.grid(row=1, column=2)
    print(chosen_option)

# Create the drop down menu:
drop_menu = OptionMenu(f1, some_string, 'One', 'two', '34', command=grab_and_assign)
drop_menu.grid(row=0, column=0)

# Create a label to display the chosen option:
label_left = Label(f1, text='chosen variable = ')
label_left.grid(row=1, column=1)

# Now for the List Box:
def get_list(event):
    # Mouse button release callback
    # Read the listbox selection and put the result in an entry box widget
    index   = listbox1.curselection()[0]# get selected line index.
    seltext = listbox1.get(index)       # get the line's text & assign to a variable.
    enter_1.delete(0,50)                # delete previous text in enter_1 otherwise 
                                        # the entries append to each other.
    enter_1.insert(0, seltext)          # now display the selected text.

# Create the listbox (note that size is in characters)
listbox1 = Listbox(f1, width=50, height=6)
listbox1.place(x=60, y=200)

# Fill the listbox with data:
listbox1.insert(END, 'a list entry')
for item in ['one has begun','two is a shoe','three like a knee','four to the door']:
    listbox1.insert(END, item)

# Use entry widget to display/edit selection:
enter_1 = Entry(f1, width=50, bg='yellow')
enter_1.insert(0, 'Click on an item in the listbox')
enter_1.place(x=60, y=310)

# Left mouse click on a list item to display selection:
listbox1.bind('<ButtonRelease-1>', get_list)

#----------------------------Tab 2: RadioButtons/Checkboxes--------------------------
# Radio Buttons first!
# String to save an option into:
string2 = StringVar(f2)

# Now some radio buttions:
rad_1 = Radiobutton(f2, text='violent', variable=string2, value='action')
rad_1.place(x=30, y=30)
rad_2 = Radiobutton(f2, text='love', variable=string2, value='romance')
rad_2.place(x=30, y=50)
rad_3 = Radiobutton(f2, text='conflict', variable=string2, value='war')
rad_3.place(x=30, y=70)

def callback_radio():
    # Callback function for the radio buttons
    chosen_button = string2.get()
    print(chosen_button)

# A button to activate the choice from the radio button you picked
rad_activate_button = (Button(f2, text='Hit me', 
                              command=callback_radio).place(x=200,y=50))

# Now for check boxes!
# Some variables for storing choices:
check_var1 = IntVar(f2)
check_var2 = IntVar(f2)
check_var3 = StringVar(f2)
check_var4 = StringVar(f2)

# The check boxes themselves:
Ck_1 = (Checkbutton(f2, text='Dog', variable=check_var1, onvalue=1, offvalue=0,
                    height=1, width=10).place(x=30, y=200))
Ck_2 = (Checkbutton(f2, text='Cat', variable=check_var2, onvalue=1, offvalue=0,
                    height=1, width=10).place(x=30, y=230))
Ck_3 = (Checkbutton(f2, text='Rat', variable=check_var3, onvalue=1, offvalue=0,
                    height=1, width=10).place(x=30, y=260))
Ck_4 = (Checkbutton(f2, text='Frog', variable=check_var4, onvalue=1, offvalue=0,
                    height=1, width=10).place(x=30, y=290))

def callback_check():
    # Callback for the check boxes:
    checkChoice1 = check_var1.get()
    checkChoice2 = check_var2.get()
    checkChoice3 = check_var3.get()
    checkChoice4 = check_var4.get()
    print(checkChoice1, checkChoice2, checkChoice3, checkChoice4)

# Button to store choices and execute the callback:
checkChooseButton = Button(f2, text='Decide your choices!', command=callback_check)
checkChooseButton.place(x=200, y=245)

#----------------------------------Tab 3: File Chooser-------------------------------
def file_chooser():
    # Function that lets you choose a file and then do something with it.
    file = tkfd.askopenfile(parent=root, mode='rb', title='Choose a file')
    if file != None:
        data = file.read()
        file.close()
        print('I got %d bytes from this file') % len(data)
    if file == None:
        print("You didn't choose a file. Please try again.")

def callback_file_chooser():
    # The callback that runs the file_chooser.
    chooseFile = input('Choose a file? Yes or No: ')
    if chooseFile == 'Yes':
        file_chooser()
    elif chooseFile == 'No':
        print("Ok, don't choose a file, jerk.")
    else:
        print("Seriously, you don't know how to answer a simple Yes or No?")

# The button to start the callback function:
file_load_button = (Button(f3, text='Touch me and see what I can do!', 
                           command=callback_file_chooser).place(x=300, y=250))

#--------------------------------------Finish up-------------------------------------
# Once the tabs are all done, we have to attach them to the notebook. This will allow
# us to name the different tabs, and give them a 'state.' A normal state means it can
# be actively used and switched between. You can, if you wish, freeze a tab so you
# cannot use it until some interaction unfreezes the tab.
notebook.add(f1, text='Dropdown/Listbox', state='normal')
notebook.add(f2, text='Radios/Checks', state='normal')
notebook.add(f3, text='File Chooser', state='normal')

# Lastly, the main loop:
root.mainloop()

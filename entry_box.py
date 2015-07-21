#!/usr/bin/python

from tkinter import Tk, Entry, Label, Button
from tkinter.commondialog import Dialog

# Create a root GUI window called "Data Entry Box"
root = Tk()
root.title('Data Entry Box')

# Create a data entry window:
enter_data_1 = Entry(root, bg='pale green')     # Attach to root window, green background
enter_data_1.grid(row=1, column=1)              # Position the entry box
enter_data_1.insert(0, 'enter text here')       # Start with some text in the box

def callback_origin():
    # Push button event handler.
    data_input_1 = enter_data_1.get()           # Grab text in the entry box
    
    # Create a label and write the value from the entry box to it.
    # i.e., validate by displaying the newly acquired string as a label
    label_2_far_right = Label(root, text=data_input_1)
    label_2_far_right.grid(row=1, column=3)
    
# This is the button that triggers data transfer from entry box to named variable 'data_input_1'
button1 = Button(root, text='press to transfer', command=callback_origin).grid(row=5, column=0)

# Run the GUI when you run the file:
root.mainloop()
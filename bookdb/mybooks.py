from tkinter import Tk, Button, Label, Scrollbar, Listbox, StringVar, Entry, W, E, N, S, END
from tkinter import ttk
from tkinter import messagebox

# Constants
BCKGRND_COLOR = "light blue"
# Global
counter_column = 0


def increase_counter_column() -> int:
    global counter_column
    counter_column += 1
    return counter_column

# Initialize
root = Tk()
# Set appearance
root.title("Booking template for database")
root.configure(background=BCKGRND_COLOR)
root.geometry("950x500")
root.resizable(width=False, height=False)
# Title entry box
title_label = ttk.Label(root, text="Title", background=BCKGRND_COLOR, font=("TkDefaultFont", 16))
title_label.grid(row=0, column=increase_counter_column(), sticky=W)
title_text = StringVar()
title_entry = ttk.Entry(root, width=24, textvariable=title_text)
title_entry.grid(row=0, column=increase_counter_column(), sticky=W)
# Author entry box
author_label = ttk.Label(root, text="Author", background=BCKGRND_COLOR, font=("TkDefaultFont", 16))
author_label.grid(row=0, column=increase_counter_column(), sticky=W)
author_text = StringVar()
author_entry = ttk.Entry(root, width=24, textvariable=title_text)
author_entry.grid(row=0, column=increase_counter_column(), sticky=W)
# ISBN number entry box
isbn_label = ttk.Label(root, text="ISBN", background=BCKGRND_COLOR, font=("TkDefaultFont", 16))
isbn_label.grid(row=0, column=increase_counter_column(), sticky=W)
isbn_text = StringVar()
isbn_entry = ttk.Entry(root, width=24, textvariable=title_text)
isbn_entry.grid(row=0, column=increase_counter_column(), sticky=W)
# Button to add
add_btn = Button(root, text="Add Book", bg="green", fg="white", font="helvetica 10 bold", command="")
add_btn.grid(row=0, column=increase_counter_column(), sticky=W)
# List box
list_bx = Listbox(root, height=16, width=40, font="helvetica 13", bg="light green")
list_bx.grid(row=3, column=1, columnspan=14, sticky=W + E, pady=40, padx=15)
# Scroll bar
scroll_bar = Scrollbar(root)
scroll_bar.grid(row=1, column=8, rowspan=14, sticky=W)
# Add to list box
list_bx.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=list_bx.yview)
# Button for Modify
modify_btn = Button(root, text="Modify record", bg="purple", fg="white", font="helvetica 10 bold", command="")
modify_btn.grid(row=15, column=4)
# Button for Delete
delete_btn = Button(root, text="Delete record", bg="red", fg="white", font="helvetica 10 bold", command="")
delete_btn.grid(row=15, column=5)
# Button for View
view_btn = Button(root, text="View all records", bg="maroon", fg="white", font="helvetica 10 bold", command="")
view_btn.grid(row=15, column=1)
# Button for Clear
clear_btn = Button(root, text="Clear screen", bg="grey", fg="white", font="helvetica 10 bold", command="")
clear_btn.grid(row=15, column=2)
# Button for Exit
exit_btn = Button(root, text="Exit application", bg="black", fg="white", font="helvetica 10 bold", command="")
exit_btn.grid(row=15, column=3)


root.mainloop()
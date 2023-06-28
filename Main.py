from tkinter import *
from tkinter import ttk
import subprocess

# create the main window
main_window = Tk()

# set the background color of the window
main_window.config(bg ='light cyan')

# set the title of the window
main_window.title("City Gym Main Window")

# set the minimum size of the window
main_window.minsize(width=50, height=200)

# set the window to be non-resizable
main_window.resizable(False,False)

# create a label for the title of the window
title_label = Label(text="City Gym Main Window", fg = "black", bg = "light blue", width = "30", height = "1")

# set the font of the label
title_label.config(text="City Gym Main Window", font=("arial",16))

# pack the label in the window
title_label.pack()

# define a function to run the Membership.py file when the button is clicked
def run_membership():
    main_window.destroy()
    subprocess.run(["python", "Membership.py"])

# create a button to open the Membership Window, and set the command to run the run_membership function
ttk.Button(main_window, text="Membership Window", command=run_membership).place(x=20, y=70)


# define a function to run the Fitness.py file when the button is clicked
def run_fitness():
    main_window.destroy()
    subprocess.run(["python", "Fitness.py"])

# create a button to open the Fitness Window, and set the command to run the run_fitness function
ttk.Button(main_window, text="Fitness Window", command=run_fitness).place(x=150, y=70) 


# define a function to run the Search.py file when the button is clicked
def run_search():
    main_window.destroy()
    subprocess.run(["python", "Search.py"])

# create a button to open the Search Window, and set the command to run the run_search function
ttk.Button(main_window, text="Search Window", command=run_search).place(x=250, y=70) 


# define a function to run the Help.py file when the button is clicked
def run_help():
    main_window.destroy()
    subprocess.run(["python", "Help.py"])

# create a button to open the Help Window, and set the command to run the run_help function
ttk.Button(main_window, text="Help Window", command=run_help).place(x=100, y=120)

# define a function to exit the main window when the button is clicked
def exit():
    main_window.destroy()

# create a button to exit the program, and set the command to run the exit function
ttk.Button(main_window, text="Exit", command=exit).place(x=200, y=120)

# run the main loop
main_window.mainloop()
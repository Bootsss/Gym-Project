#Help Form

from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
import subprocess

#---------------------------Window---------------------------

help_window = Tk()
help_window.config(bg ='light cyan')
help_window.title("City Gym Membership Form")
help_window.minsize(width=700, height=550)

#---------------------------Title---------------------------

title_label = Label(text="City Gym Help Window", fg = "black", bg = "light blue", width = "60", height = "1")
title_label.config(text="City Gym Help Window", font=("arial",16))
title_label.pack()

#---------------------------Fitness Window---------------------------

frame1 = Frame(help_window, highlightbackground="black", highlightthickness=2, width = 600, height = 200 , bg ='light blue')
frame1.place(x=60, y=50)


# Create the instructions label
instructions_label = tk.Label(frame1, text="Instructions for Using the City Gym Search Form:", bg='light blue', font=("arial", 12))
instructions_label.pack()

# Create the first name instructions label
first_name_instructions = tk.Label(frame1, text="1. Enter the first name of the member you want to search for in the 'First Name' entry field.", bg='light blue')
first_name_instructions.pack()

# Create the last name instructions label
last_name_instructions = tk.Label(frame1, text="2. Enter the last name of the member you want to search for in the 'Last Name' entry field.", bg='light blue')
last_name_instructions.pack()

# Create the member ID instructions label
member_id_instructions = tk.Label(frame1, text="3. Enter the member ID of the member you want to search for in the 'Member ID' entry field.", bg='light blue')
member_id_instructions.pack()

# Create the membership plan ID instructions label
membership_plan_id_instructions = tk.Label(frame1, text="4. Enter the membership plan ID of the member you want to search for in the 'Membership Plan ID' entry field. \nUse 1 for Basic, 2 for Regular, and 3 for Premium.", bg='light blue')
membership_plan_id_instructions.pack()

# Create the search button instructions label
search_button_instructions = tk.Label(frame1, text="5. Press the 'Search' button to search the database and display the results in the 'Results' label.", bg='light blue')
search_button_instructions.pack()

#---------------------------Search Window---------------------------

frame2 = Frame(help_window, highlightbackground="black", highlightthickness=2, width = 600, height = 200 , bg ='light blue')
frame2.place(x=60, y=215)

# Create the instructions label
instructions_label = tk.Label(frame2, text="Instructions for Using the City Gym Fitness Form:", bg='light blue', font=("arial", 12))
instructions_label.pack()

# Create the first name instructions label
first_name_instructions = tk.Label(frame2, text="1. Enter the MemberID of the client you would like to view the classes they are enrolled in ", bg='light blue')
first_name_instructions.pack()

# Create the last name instructions label
last_name_instructions = tk.Label(frame2, text="2. If you want to register a client for a class enter the MemberID and select the classes you want to enroll them in.", bg='light blue')
last_name_instructions.pack()

# Create the member ID instructions label
member_id_instructions = tk.Label(frame2, text="3. You must click search after entering the MemberID for the app to show either the classes or the checkboxes", bg='light blue')
member_id_instructions.pack()

# Create the membership plan ID instructions label
membership_plan_id_instructions = tk.Label(frame2, text="4. If you want to register the user make sure you click the submit button to enroll them", bg='light blue')
membership_plan_id_instructions.pack()

# Create the search button instructions label
search_button_instructions = tk.Label(frame2, text="5. If you want to search for another user click the reset button and enter another MemberID", bg='light blue')
search_button_instructions.pack()

#---------------------------Membership Window---------------------------

frame3 = Frame(help_window, highlightbackground="black", highlightthickness=2, width = 600, height = 200 , bg ='light blue')
frame3.place(x=60, y=380)

# Create the instructions label
instructions_label = tk.Label(frame3, text="Instructions for Using the City Gym Membership Form:", bg='light blue', font=("arial", 12))
instructions_label.pack()

# Create the first name instructions label
first_name_instructions = tk.Label(frame3, text="1. Enter all your information including first name, last name etc.", bg='light blue')
first_name_instructions.pack()

# Create the last name instructions label
last_name_instructions = tk.Label(frame3, text="2. choose you base package, Basic, Regular, Premium and select how long you want to sign up for.", bg='light blue')
last_name_instructions.pack()

# Create the member ID instructions label
member_id_instructions = tk.Label(frame3, text="3. Select your payment type, credit or debit and payment frequency.", bg='light blue')
member_id_instructions.pack()

# Create the membership plan ID instructions label
membership_plan_id_instructions = tk.Label(frame3, text="4. select all the extras you want to add into your plan", bg='light blue')
membership_plan_id_instructions.pack()

# Create the search button instructions label
search_button_instructions = tk.Label(frame3, text="5. Press calculate to look at the price, Submit to submit the member into the database, and reset to reset the fields", bg='light blue')
search_button_instructions.pack()













def run_main():
    help_window.destroy()
    subprocess.run(["python", "Main.py"])

tk.Button(help_window, text="Back To Main", command=run_main).place(x=20, y=3)

help_window.mainloop()
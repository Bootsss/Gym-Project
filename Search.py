import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import StringVar
import subprocess

# Create the main window
search_window = tk.Tk()
search_window.config(bg ='light cyan')
search_window.title("City Gym Search Window")
search_window.minsize(width=350, height=450)
search_window.resizable(False,False)

title_label = tk.Label(text="City Gym Search Form", fg = "black", bg = "light blue", width = "30", height = "1")
title_label.config(text="City Gym Search Form", font=("arial",16))
title_label.pack()


first_name = StringVar()
last_name = StringVar()
member_id = StringVar()
membership_plan_id = StringVar()

# Create the first name label and entry
first_name_label = tk.Label(search_window, text="First Name:", bg='light cyan')
first_name_label.place(x=50, y=50)
first_name_entry = ttk.Entry(search_window, textvariable=first_name)
first_name_entry.place(x=200, y=50)

# Create the last name label and entry
last_name_label = tk.Label(search_window, text="Last Name:", bg='light cyan')
last_name_label.place(x=50, y=80)
last_name_entry = ttk.Entry(search_window, textvariable=last_name)
last_name_entry.place(x=200, y=80)

# Create the member id label and entry
member_id_label = tk.Label(search_window, text="Member ID:", bg='light cyan')
member_id_label.place(x=50, y=110)
member_id_entry = ttk.Entry(search_window, textvariable=member_id)
member_id_entry.place(x=200, y=110)

# Create the membership plan id label and entry
membership_plan_id_label = tk.Label(search_window, text="Membership Plan ID:", bg='light cyan')
membership_plan_id_label.place(x=50, y=140)
membership_plan_id_entry = ttk.Entry(search_window, textvariable=membership_plan_id)
membership_plan_id_entry.place(x=200, y=140)

# Create the rules labels

title_rule = tk.Label(search_window, text='Membership Plan ID Rules', fg = "black", bg = 'light cyan')
title_rule.place(x=120, y=205)
basic_rule = tk.Label(search_window, text='Search 1 For Basic', fg = "black", bg = 'light cyan')
basic_rule.place(x=135, y=223)
regular_rule = tk.Label(search_window, text='Search 2 for Regular', fg = "black", bg = 'light cyan')
regular_rule.place(x=133, y=240)
premium_rule = tk.Label(search_window, text='Search 3 for Premium', fg = "black", bg = 'light cyan')
premium_rule.place(x=130, y=257)


# Create the search frame
search_frame = ttk.Frame(search_window)
search_frame.place(x=20, y=170)

# Create a frame for the results label
results_frame = ttk.Frame(search_window)
results_frame.place(x=40, y=300)

# Create the results label and add it to the results frame
results_label = ttk.Label(results_frame, text="")
results_label.grid(row=0, column=0, padx=5, pady=5)

def search():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()
    member_id = member_id_entry.get().strip()
    membership_plan_id = membership_plan_id_entry.get().strip()

    # Check if any input is provided
    if not any([first_name, last_name, member_id, membership_plan_id]):
        messagebox.showerror("Error", "Please enter a valid entry")
        return

    # Connect to the database
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    # Build the query
    query = '''SELECT * FROM MemberTable
                WHERE (lower(FirstName) LIKE lower(?) OR lower(LastName) LIKE lower(?) OR lower(MemberID) LIKE lower(?) OR lower(membership_plan_id) LIKE lower(?)) '''
    if member_id:
        query += f" AND MemberID = {member_id}"
    if first_name:
        query += f" AND FirstName = '{first_name}'"
    if last_name:
        query += f" AND LastName = '{last_name}'"
    if membership_plan_id:
        query += f" AND membership_plan_id = '{membership_plan_id}'"

    # Execute the query
    c.execute(query, (first_name, last_name, member_id, membership_plan_id))
    results = c.execute(query, (first_name, last_name, member_id, membership_plan_id)).fetchall()
    
    # Display the results
    if len(results) == 0:
        results_label.config(text="No records found.")
    else:
        text = ""
        for result in results:
            membership_plan_id = result[-1]
            # Use a dictionary to map the membership plan IDs to names
            membership_plan_names = {1: "Basic", 2: "Regular", 3: "Premium"}
            membership_plan_name = membership_plan_names.get(membership_plan_id, "Unknown")
            # Add the membership plan name to the result tuple
            result = result[:-1] + (membership_plan_name,)
            text += ", ".join([str(x) for x in result]) + "\n"
        results_label.config(text=text)
    conn.close()


# Create the search button
search_button = ttk.Button(search_window, text="Search", command=search)
search_button.place(x=150, y=180)

def run_main():
    search_window.destroy()
    subprocess.run(["python", "Main.py"])

ttk.Button(search_window, text="Back To Main", command=run_main).place(x=140, y=400)

search_window.mainloop()


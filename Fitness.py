#fitness place

import tkinter as tk
from tkinter import messagebox
import sqlite3
import subprocess

class FitnessForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fitness Form")
        self.geometry("350x350")
        self.config(bg ='light cyan')
        self.resizable(False,False)

        title_label = tk.Label(text="City Gym Fitness Form", fg = "black", bg = "light blue", width = "30", height = "1")
        title_label.config(text="City Gym Fitness Form", font=("arial",16))
        title_label.pack()
        tk.Button(self, text="Back To Main", command=self.run_main).place(x=140, y=270)


        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()


        cursor.execute("""
            CREATE TABLE IF NOT EXISTS classes (
                class_name TEXT PRIMARY KEY,
                day_of_week TEXT,
                time TIME
            )
        """)
        try:
            cursor.execute("INSERT INTO classes (class_name, day_of_week, time) VALUES (?, ?, ?)", ("Cardio", "Thursday", "3 pm–5 pm"))
        except sqlite3.IntegrityError:
            pass
        try:
            cursor.execute("INSERT INTO classes (class_name, day_of_week, time) VALUES (?, ?, ?)", ("Pilates", "Friday", "9 am–11 am"))
        except sqlite3.IntegrityError:
            pass
        try:
            cursor.execute("INSERT INTO classes (class_name, day_of_week, time) VALUES (?, ?, ?)", ("Spin", "Monday", "2 pm–4 pm"))
        except sqlite3.IntegrityError:
            pass
        conn.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Enrollments (
                MemberID INTEGER,
                class_name TEXT,
                FOREIGN KEY(MemberID) REFERENCES MemberTable(MemberID),
                FOREIGN KEY(class_name) REFERENCES classes(class_name),
                PRIMARY KEY (MemberID, class_name)
            )
        """)
        conn.commit()
        conn.close()
        
        # create a label for the ID input
        self.id_label = tk.Label(self, text="ID: ", bg='light cyan')
        self.id_label.place(x=20, y=50)
        
        # create an entry for the ID input
        self.id_entry = tk.Entry(self)
        self.id_entry.place(x=80, y=50)
        
        # create a search button
        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.search_button.place(x=250, y=46)
        
        # create a label for the fitness class selection
        self.class_label = tk.Label(self, text="Select a Fitness Class: ", bg='light cyan')
        
        # create a variable to store the selected fitness class
        self.selected_class = tk.StringVar()
        
        
        


        # create a submit button
        self.submit_button = tk.Button(self, text="Submit", command=self.submit)
        self.submit_button.place(x=100, y=170)
        
        # create a reset button
        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.place(x=200, y=170)
        
        # create a message label
        self.message_label = tk.Label(self, text="")
        self.message_label.place(x=20, y=250)

    def run_main(self):
        self.destroy()
        subprocess.run(["python", "Main.py"])

    def search(self):
        # Get the user ID
        user_id = self.id_entry.get()
        # Connect to the database
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        # Check if the user exists
        cursor.execute("SELECT COUNT(*) FROM MemberTable WHERE MemberID=?", (user_id,))
        result = cursor.fetchone()
        # If the user exists
        if result[0] > 0:
            # Check if the user is already enrolled in any classes
            cursor.execute("SELECT COUNT(*) FROM Enrollments WHERE MemberID=?", (user_id,))
            result = cursor.fetchone()
            # If the user is already enrolled in any classes
            if result[0] > 0:
                # Get the classes the user is already enrolled in
                cursor.execute("SELECT class_name FROM Enrollments WHERE MemberID=?", (user_id,))
                enrolled_classes = [x[0] for x in cursor.fetchall()]
                message = f"You are enrolled in the classes: {', '.join(enrolled_classes)}"
                self.message_label.config(text=message, bg='light cyan')
                self.message_label.place(x=50, y=220)
                # disabling the entry widget and the search button
                self.id_entry.config(state='disable')
                self.search_button.config(state='disable')
            else:
                # Show the checkboxes for the available classes
                self.class_label.place(x=20, y=80)
                self.class_vars = []
                for i, class_name in enumerate(self.get_classes()):
                    var = tk.IntVar()
                    tk.Checkbutton(self, text=class_name, variable=var, bg='light cyan').place(x=70 + (i * 70), y=120)
                    self.class_vars.append((class_name, var))
        else:
            # Show an error message
            self.message_label.config(text="Invalid ID")
            
    def validate_user(self):
        # Connect to the database
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM MemberTable WHERE MemberId=?", (self.id_entry.get(),))
        result = cursor.fetchone()
        # Check if the user is valid
        if result:
            return True
        else:
            return False
            
    def display_enrolled_classes(self):
        # Connect to the database
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT class_name FROM Enrollments WHERE MemberID=?", (self.id_entry.get(),))
        result = cursor.fetchall()
        # Clear the message label
        self.message_label.config(text="")
        return result
    
    def get_classes(self):
        # connect to the database and get a list of all available classes
        # you can replace this with a call to a database function
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT class_name FROM classes")
        classes = [class_name[0] for class_name in cursor.fetchall()]
        conn.close()
        return classes
        
    def show_class_section(self):
        # Show the class label
        self.class_label.place(x=20, y=100)
        # Show the radio buttons
        for i, button in enumerate(self.class_buttons):
            button.place(x=20, y=120 + (i * 30))
        # Show the submit and reset buttons
        self.submit_button.place(x=20, y=200)
        self.reset_button.place(x=120, y=200)
        
    def submit(self):
        # Connect to the database
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        # Insert the selected class into the Enrollments table
        for class_name, var in self.class_vars:
            if var.get() == 1:
                cursor.execute("INSERT INTO Enrollments (MemberID, class_name) VALUES (?, ?)", (self.id_entry.get(), class_name))
        conn.commit()
        # Show a message box confirming the enrollment
        tk.messagebox.showinfo("Success", "Successfully enrolled in class/classes.")
        # Clear the form
        conn.close()
        self.reset()


    def reset(self):
        self.id_entry.config(state='normal')
        self.id_entry.delete(0, 'end')
        self.selected_class.set("")
        self.message_label.config(text="")
        self.search_button.config(state='normal')







    
            
    


if __name__ == "__main__":
    form = FitnessForm()
    form.mainloop()

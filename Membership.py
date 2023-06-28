#Membership Form

from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox
import sqlite3
import subprocess


cwd = os.getcwd()

base_cost = 0
extras_cost = 0
discount = 0
reg_payment = 0
net_cost = 0
memberid = 0

def validate_input(s):      #This function ensures that you cannot type numbers into first name, last name, or address.
    if s.isdigit():
        return False
    return True


def validate_input_phone(s):        #This function ensures that you cannot type letters into phone number
    if s.isdigit():
        return True
    return False







#---------------------------Window---------------------------

window = Tk()
window.config(bg ='light cyan')
window.title("City Gym Membership Form")
window.minsize(width=700, height=550)
window.resizable(False,False)

#---------------------------Title---------------------------

title_label = Label(text="City Gym Membership Form", fg = "black", bg = "light blue", width = "60", height = "1")
title_label.config(text="City Gym Membership Form", font=("arial",16))
title_label.pack()


#---------------------------Information Collecting---------------------------

frame1 = Frame(window, highlightbackground="black", highlightthickness=2, width = 325, height = 200 , bg ='light blue')     #makes my frame around the entries
frame1.place(x=15, y=50)

first_name_label = Label(frame1, text="First Name:" , bg ='light blue', font=("arial", 9, "italic"))        #creates a label
first_name_label.place(x=5, y=25)
first_name = Entry(frame1, width=30, validate="key", validatecommand=(window.register(validate_input), '%S'))       #creates my entry and calls the validate function
first_name.place(x=100, y=25, width=200, height=25)     #places entry


last_name_label = Label(frame1, text="Last Name:"  , bg ='light blue', font=("arial", 9, "italic"))
last_name_label.place(x=5, y=65)
last_name = Entry(frame1, width=30, validate="key", validatecommand=(window.register(validate_input), '%S'))
last_name.place(x=100, y=65, width=200, height=25)

address_label = Label(frame1, text="Address:"  , bg ='light blue', font=("arial", 9, "italic"))
address_label.place(x=5, y=105)
address = Entry(frame1, width=30, validate="key", validatecommand=(window.register(validate_input), '%S'))
address.place(x=100, y=105, width=200, height=25)

phone_label = Label(frame1, text="Phone Number:"  , bg ='light blue', font=("arial", 9, "italic"))
phone_label.place(x=5, y=145)
phone = Entry(frame1, width=30, validate="key", validatecommand=(window.register(validate_input_phone), '%S'))
phone.place(x=100, y=145, width=200, height=25)

#---------------------------Base Membership---------------------------

frame2 = Frame(window, highlightbackground="black", highlightthickness=2, width = 325, height = 200 , bg ='light blue')
frame2.place(x=365, y=50)

membership_details = Label(frame2, text="Membership Details:")
membership_details.config(text="Membership Details:" , bg ='light blue', font=("arial", 9, "italic"))
membership_details.place(x=5, y=25)

membership_time = Label(frame2, text="Membership Time:")
membership_time.config(text="Membership Time:" , bg ='light blue', font=("arial", 9, "italic"))
membership_time.place(x=5, y=100)

def radio_base_package():
    print(base_package.get())
base_package = StringVar()
base_package.set('0')    #Holds variable at 0 till checked
basic_button = Radiobutton(frame2, text="Basic ($10 pw)", value='10', variable=base_package, command=radio_base_package ,  bg ='light blue')       #Creates my first radio button that the user can check
regular_button = Radiobutton(frame2, text="Regular ($15 pw)", value='15', variable=base_package, command=radio_base_package  , bg ='light blue')
premium_button = Radiobutton(frame2, text="Premium ($20 pw)", value='20', variable=base_package, command=radio_base_package  , bg ='light blue')
basic_button.place(x=185, y=25)
regular_button.place(x=185, y=50)
premium_button.place(x=185, y=75)

def radio_signup_time():
    print(sign_up_time.get())
sign_up_time = StringVar()
sign_up_time.set('0')
three_month_button = Radiobutton(frame2, text="3 months", value='1', variable=sign_up_time, command=radio_signup_time , bg ='light blue')
twelve_month_button = Radiobutton(frame2, text="12 months", value='2', variable=sign_up_time, command=radio_signup_time , bg ='light blue')
max_month_button = Radiobutton(frame2, text="24 months", value='3', variable=sign_up_time, command=radio_signup_time , bg ='light blue')
three_month_button.place(x=185, y=100)
twelve_month_button.place(x=185, y=125)
max_month_button.place(x=185, y=150)

#---------------------------Payment Options---------------------------

frame3 = Frame(window, highlightbackground="black", highlightthickness=2, width = 325, height = 200  , bg ='light blue')        #creates new frame
frame3.place(x=15, y=265)

payment_options_title = Label(frame3, text="Payment Options")       #creates new label inside frame 3
payment_options_title.config(text="Payment Options" , bg ='light blue', font=("arial", 9, "italic"))
payment_options_title.place(x=115, y=5)

def radio_payment_type():
    print(payment_type.get())
payment_type = StringVar()
payment_type.set('0')
debit_button = Radiobutton(frame3, text='Debit', value='1', variable=payment_type, command=radio_payment_type , bg ='light blue')       #creates new radio button for debit
credit_button = Radiobutton(frame3, text="credit", value='2', variable=payment_type, command=radio_payment_type , bg ='light blue')
debit_button.place(x=75, y=30)
credit_button.place(x=175, y=30)

def radio_payment_time():
    print(payment_time.get())
payment_time = StringVar()
payment_time.set('0')
weekly_payment_button = Radiobutton(frame3, text='Weekly', value='1', variable=payment_time, command=radio_payment_time , bg ='light blue')
monthly_payment_button = Radiobutton(frame3, text="Monthly", value='2', variable=payment_time, command=radio_payment_time , bg ='light blue')
weekly_payment_button.place(x=75, y=50)
monthly_payment_button.place(x=175, y=50)

#---------------------------Extras---------------------------

extras_label = Label(frame3, text="Extras")
extras_label.config(text="Extras" , bg ='light blue', font=("arial", 9, "italic"))
extras_label.place(x=140, y=80)

def radio_access():             #This function is called when the radio button is checked
    global access_clicked       #It looks if the button is checked or not already and if it is checked it will reset the button
    if access_clicked == True:
        access.set('0')
        access_clicked = False
    else:
        print(access.get())
        access_clicked =True

access = IntVar()
access.set('0')
access_clicked = False
access_button = Radiobutton(frame3, text='24/7 Access ($1 per week)', value='1', variable=access, command=radio_access , bg ='light blue')
access_button.place(x=70, y=100)

def radio_trainer():           
    global trainer_clicked      
    if trainer_clicked == True:
        trainer.set('0')
        trainer_clicked = False
    else:
        print(trainer.get())
        trainer_clicked =True

trainer = IntVar()
trainer_clicked = False
trainer.set('0')
trainer_button = Radiobutton(frame3, text='Personal Trainer ($20 per week)', value='20', variable=trainer, command=radio_trainer , bg ='light blue')
trainer_button.place(x=70, y=120)

def radio_diet():
    global diet_clicked
    if diet_clicked == True:
        diet.set('0')
        diet_clicked = False
    else:
        print(diet.get())
        diet_clicked =True


diet = IntVar()
diet.set('0')
diet_clicked = False
diet_button = Radiobutton(frame3, text='Diet Consultation ($20 per week)', value='20', variable=diet, command=radio_diet , bg ='light blue')
diet_button.place(x=70, y=140)

def radio_videos():
    global videos_clicked
    if videos_clicked == True:
        videos.set('0')
        videos_clicked = False
    else:
        print(videos.get())
        videos_clicked =True


videos = IntVar()
videos.set('0')
videos_clicked = False
videos_button = Radiobutton(frame3, text='Online Videos ($2 per week)', value='2', variable=videos, command=radio_videos , bg ='light blue')
videos_button.place(x=70, y=160)

#---------------------------Staff Only Show Calculations---------------------------

frame4 = Frame(window, highlightbackground="black", highlightthickness=2, width = 325, height = 200 , bg ='light blue')
frame4.place(x=365, y=265)

extras_label = Label(frame4, text="Membership Cost Calculations")       #creates label inside frame 4
extras_label.config(text="Membership Cost Calculations" , bg ='light blue', font=("arial", 9, "italic"))
extras_label.place(x=80, y=5)

base_cost_label = Label(frame4, text="Base Cost:" , bg ='light blue')       #creates label inside frame 4
base_cost_label.place(x=5, y=40)        #places label
base_cost_entry = Entry(frame4)     #Creates empty entry inside frame 4
base_cost_entry.place(x=200, y=40, width=50, height=15)


extra_charges_label = Label(frame4, text="Extra Charges:" , bg ='light blue')
extra_charges_label.place(x=5, y=60)
extra_charges_entry = Entry(frame4, width=30)
extra_charges_entry.place(x=200, y=60, width=50, height=15)

total_discount_label = Label(frame4, text="Total Discount:" , bg ='light blue')
total_discount_label.place(x=5, y=80)
total_discount_entry = Entry(frame4, width=30)
total_discount_entry.place(x=200, y=80, width=50, height=15)

net_membership_label = Label(frame4, text="Net Membership Cost:" , bg ='light blue')
net_membership_label.place(x=5, y=100)
net_membership_entry = Entry(frame4, width=30)
net_membership_entry.place(x=200, y=100, width=50, height=15)

regular_payment_label = Label(frame4, text="Regular Payment Ammount:" , bg ='light blue')
regular_payment_label.place(x=5, y=120)
regular_payment_entry = Entry(frame4, width=30)
regular_payment_entry.place(x=200, y=120, width=50, height=15)

#---------------------------Discount Options---------------------------

discount1_label = Label(text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type")
discount1_label.config(text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type" , bg ='light cyan', font=("arial", 9, "italic"))
discount1_label.place(x=100, y=480)
discount2_label = Label(text="Sign up for 24 months to receive a $5 per week discount on any membership type.")
discount2_label.config(text="Sign up for 24 months to receive a $5 per week discount on any membership type." , bg ='light cyan', font=("arial", 9, "italic"))
discount2_label.place(x=125, y=500)
discount3_label = Label(text="For direct debits, there is a 1% discount on the base membership cost.")
discount3_label.config(text="For direct debits, there is a 1% discount on the base membership cost." , bg ='light cyan', font=("arial", 9, "italic"))
discount3_label.place(x=145, y=520)

#---------------------------DataBase---------------------------
def create_tables():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    # Create the 'MembershipPlan' table
    c.execute('''CREATE TABLE IF NOT EXISTS MembershipPlan (membership_plan_ID INTEGER PRIMARY KEY, membership_type TEXT, base_cost REAL)''')

    # Insert data into the 'MembershipPlan'
    data = [
        (1, 'Basic', base_package.get()),
        (2, 'Regular', base_package.get()),
        (3, 'Premium', base_package.get())
    ]
    for item in data:
        try:
            c.execute("INSERT INTO MembershipPlan (membership_plan_ID, membership_type, base_cost) VALUES (?, ?, ?)", item)
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f'Error: {e}')
            print(f"The membership_plan_ID {item[0]} already exists in the table.")

    # Create the 'FitnessTable' table
    c.execute('''CREATE TABLE IF NOT EXISTS FitnessTable (fitness_id INTEGER PRIMARY KEY, fitness_type TEXT)''')
    # Insert data into the 'FitnessTable'
    data = [
    (1, 'cardio'),
    (2, 'pilates'),
    (3, 'spin')
    ]

    for item in data:
        try:
            c.execute("INSERT INTO FitnessTable (fitness_id, fitness_type) VALUES (?, ?)", item)
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(f'Error: {e}')
            print(f"The fitness_id {item[0]} already exists in the table.")

    conn.close()

def submit():
    create_tables()

    global reg_payment
    global memberid
    membership_extras = ""
    membership_plan_id = 0

    conn = sqlite3.connect('data.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS MemberTable(
                        MemberID INTEGER PRIMARY KEY AUTOINCREMENT, 
                        FirstName TEXT, 
                        LastName TEXT, 
                        Phone INT, Address 
                        TEXT, Extras TEXT, 
                        RegularPayment INT, 
                        membership_plan_id INTEGER,
                        FOREIGN KEY(membership_plan_id) REFERENCES MembershipPlan(membership_plan_id))
            '''
    conn.execute(table_create_query)

    # Insert Data
    data_insert_query = '''INSERT INTO MemberTable(
                        FirstName, 
                        LastName, 
                        Phone, 
                        Address, 
                        Extras, 
                        RegularPayment, 
                        membership_plan_id) VALUES 
                        (?, ?, ?, ?, ?, ?, ?)'''

    # determine the membership_plan_id based on the base_cost variable
    if base_package.get() == 10:
        membership_plan_id = 1
    elif base_package.get() == 15:
        membership_plan_id = 2
    elif base_package.get() == 20:
        membership_plan_id = 3
    else:
        membership_plan_id = None

    if access.get() == 1:
        membership_extras += "Access, "

    if trainer.get() == 20:
        membership_extras += "Trainer, "

    if diet.get() == 20:
        membership_extras += "Diet, "

    if videos.get() == 2:
        membership_extras += "Videos, "

    # remove trailing comma and space
    membership_extras = membership_extras[:-2]  # determine the membership_plan_id based on the base_package variable

    print(base_package.get())
    if base_package.get():
    #... rest of the code
        if base_package.get() == '10':
            membership_plan_id = 1
        elif base_package.get() == '15':
            membership_plan_id = 2
        elif base_package.get() == '20':
            membership_plan_id = 3
        else:
            membership_plan_id = None
    data_insert_tuple = (first_name.get(), last_name.get(), phone.get(), address.get(), membership_extras, reg_payment, membership_plan_id)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
    print("SUBMITTED")
     


        
         
ttk.Button(frame4, text="Submit", command=lambda:[error_checking(), submit()]).place(x=20, y=150)       #button that calls the submit function

#---------------------------Calculations---------------------------

def calculate_extras():     #calculates extras function
    global extras_cost      
    access_extra = access.get()
    trainer_extra = trainer.get()
    diet_extra = diet.get()
    videos_extra = videos.get()
    extras_cost = (int(access_extra) + int(trainer_extra) + int(diet_extra) + int(videos_extra))        #calculations after variable changes

def calculate_base():
    global base_cost
    base_cost = base_package.get()      #gives the variable base_cost a number
    

def calculate_discount():
    global discount
    global base_cost

    if payment_type.get() == '1':
        discount = 0.01 * int(base_cost)        #calculations for discount
    if sign_up_time.get() == '2':
        discount += 2
    elif sign_up_time.get() == '3':
        discount += 5
    

def net_membership():
    global extras_cost, base_cost, discount, net_cost
    net_cost = (int(extras_cost) + int(base_cost) - float(discount))        #calculations for the total membership cost
    

def regular_payment():
    global net_cost
    global reg_payment
    if payment_time.get() == '2':       #calculations for regular payment
        reg_payment = net_cost * 4
    else:
        reg_payment = net_cost
    

def calculate():        #calculate funcion
    base_cost_entry.delete(0, 'end')        #deletes characters in base cost entry
    extra_charges_entry.delete(0, 'end')
    total_discount_entry.delete(0, 'end')
    net_membership_entry.delete(0, 'end')
    regular_payment_entry.delete(0, 'end')

    global extras_cost, base_cost, discount, net_cost, reg_payment      #makes variables global
    extras_cost = 0 
    base_cost = 0 
    discount = 0 
    net_cost = 0 
    reg_payment = 0


    calculate_extras()
    calculate_base()
    calculate_discount()
    net_membership()
    regular_payment()

    base_cost_entry.configure(state='normal')       #changes state so it refreshes itself from disabled for a split second to allow for the calculations to show
    base_cost_entry.delete(0,END)       #deletes numbers out of base cost entry
    base_cost_entry.insert(0, '$' + str(base_cost))     #inserts base cost into base cost entry
    base_cost_entry.configure(state='disabled')     #changes state so user cannot change the numbers after calculations

    extra_charges_entry.configure(state='normal')
    extra_charges_entry.delete(0,END)
    extra_charges_entry.insert(0, '$' + str(extras_cost))
    extra_charges_entry.configure(state='disabled')

    total_discount_entry.configure(state='normal')
    total_discount_entry.delete(0,END)
    total_discount_entry.insert(0, '$' + str(discount))
    total_discount_entry.configure(state='disabled')

    net_membership_entry.configure(state='normal')
    net_membership_entry.delete(0,END)
    net_membership_entry.insert(0, '$' + str(net_cost))
    net_membership_entry.configure(state='disabled')

    regular_payment_entry.configure(state='normal')
    regular_payment_entry.delete(0,END)
    regular_payment_entry.insert(0, '$' + str(reg_payment))
    regular_payment_entry.configure(state='disabled')

ttk.Button(frame4, text="Calculate", command=lambda: [calculate()]).place(x= 120, y = 150)      #button that calls calculate

regular_payment_entry.configure(state='disabled')
net_membership_entry.configure(state='disabled')
total_discount_entry.configure(state='disabled')
extra_charges_entry.configure(state='disabled')
base_cost_entry.configure(state='disabled') 
#---------------------------Reset Button---------------------------
def reset():        #reset function
    videos.set(0)       #sets videos variable to 0 same for the rest
    diet.set(0)
    access.set(0)
    trainer.set(0)
    payment_time.set(0)
    payment_type.set(0)
    sign_up_time.set(0)
    base_package.set(0)
    first_name.delete(0, END)
    last_name.delete(0, END)
    phone.delete(0, END)
    address.delete(0, END)

reset_button = ttk. Button(frame4, text= "Reset", command=lambda: [reset(), calculate()]).place(x=220, y=150)        #button that calls reset

#---------------------------Error Checking---------------------------

def error_checking() -> None:       #error checking function
    if first_name.get() == "":      #checks if name is empty
        messagebox.showerror(title='Error', message='Error, Enter a valid first name')      #gives error if name is empty
    elif last_name.get() == "":
        messagebox.showerror(title='Error', message='Error, Enter a valid last name')
    elif phone.get() == "":
        messagebox.showerror(title='Error', message='Error, Enter a valid phone number')
    elif address.get() == "":
        messagebox.showerror(title='Error', message='Enter a valid address')
    elif base_package.get() == '0':
        messagebox.showerror(title='Error', message='Please choose your base package')
    elif sign_up_time.get() == '0':
        messagebox.showerror(title='Error', message='Please choose your membership time')
    elif payment_type.get() == '0':
        messagebox.showerror(title='Error', message='Please choose your payment type')   
    elif payment_time.get() == '0':
        messagebox.showerror(title='Error', message='Please choose your payment time')


def run_main():
    window.destroy()
    subprocess.run(["python", "Main.py"])

ttk.Button(window, text="Back To Main", command=run_main).place(x=20, y=3)


window.mainloop()
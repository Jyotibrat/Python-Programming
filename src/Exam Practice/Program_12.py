import tkinter as tk
from tkinter import messagebox 

def display_values():
    Name = name.get()
    Registration_number = registration_number.get()
    Age = age.get()
    
    print(Name)
    print(Registration_number)
    print(Age)
    
    messagebox.showinfo("Entered Details", f"Name: {Name}\nRegistration Number: {Registration_number}\nAge: {Age}")

root = tk.Tk()
root.title("A simple form")

name_label = tk.Label(root, text="Name: ")
name_label.pack()
name = tk.Entry(root)
name.pack()

registration_number_label = tk.Label(root, text="Registration Number: ")
registration_number_label.pack()
registration_number = tk.Entry(root)
registration_number.pack()

age_label = tk.Label(root, text="Age: ")
age_label.pack()
age = tk.Entry(root)
age.pack()

button = tk.Button(root, text="Enter", command=display_values)
button.pack()

root.mainloop()
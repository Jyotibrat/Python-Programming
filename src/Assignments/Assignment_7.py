import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    age = entry_age.get()
    email = entry_email.get()

    messagebox.showinfo("Form Submitted", f"Name: {name}\nAge: {age}\nEmail: {email}")

root = tk.Tk()
root.title("Simple GUI Form")

label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

root.mainloop()

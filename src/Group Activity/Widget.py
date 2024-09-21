import tkinter as tk
from tkinter import messagebox

def show_entry_text():
    messagebox.showinfo("Entry Content", entry.get())

root = tk.Tk()
root.title("Complete GUI Example")
root.geometry("300x200")

label = tk.Label(root, text="Enter something:", font=("Helvetica", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=25, font=("Helvetica", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Show Entry", command=show_entry_text, bg="#2980b9", fg="white", font=("Helvetica", 12))
button.pack(pady=10)

root.mainloop()
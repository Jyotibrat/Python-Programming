import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Info", "This is a message box")

root = tk.Tk()
root.title("Dialog Example")

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

root.mainloop()
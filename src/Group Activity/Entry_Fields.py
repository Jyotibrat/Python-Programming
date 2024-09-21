import tkinter as tk

def show_entry_text():
    print(entry.get())

root = tk.Tk()
root.title("Entry Example")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show Text", command=show_entry_text)
button.pack()

root.mainloop()
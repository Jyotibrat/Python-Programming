import tkinter as tk

counter = 0

def button_pressed(label):
    global counter
    counter += 1
    print(counter)
    label.config(text=f"Button Pressed: {counter} times")

def main():
    root = tk.Tk()
    root.title("Demo project")
    root.geometry("400x400")
    label = tk.Label(root, text=f"Button Pressed: {counter} times", font=25)
    button = tk.Button(root, text="Button", font=25, command=lambda: button_pressed(label))
    label.pack()
    button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk

def on_button_click():
    label.config(text="batyrmany basu")

root = tk.Tk()
root.title("stack")
root.geometry("600x500")

button = tk.Button(root, text="bastau", command=on_button_click)
button.pack()

root.mainloop()

import tkinter as tk

def on_button_click():
    label.config(text="basu")
    
    second_window=tk.Toplevel(root)
    second_window.title("oryndalu")
    second_window.geometry("600x500")

    second_label=tk.Label(second_window, text="ekinshi tereze")
    second_label.pack(pady=20)

def on_submit():
    try:
        num_elements = int(entry.get())
        if num_elements <= 0:
            raise ValueError("element sany on boluy kerek")


root = tk.Tk()
root.title("stack")
root.geometry("600x500")

stack= []

submit_button = tk.Button(root, text="Ondeu", command=on_submit)
submit_button.pack(pady=10)

label = tk.Label(root, text="batyrmany basu")
label.pack(pady=20)

button = tk.Button(root, text="bastau", command=on_button_click)
button.pack()

root.mainloop()

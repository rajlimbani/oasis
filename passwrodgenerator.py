import tkinter as tk
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
    pyperclip.copy(password)

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

complexity_label = tk.Label(root, text="Password Complexity:")
complexity_label.pack()

complexity_var = tk.IntVar()
complexity_var.set(1)

complexity_frame = tk.Frame(root)
complexity_frame.pack()

simple_radio = tk.Radiobutton(complexity_frame, text="Simple", variable=complexity_var, value=1)
simple_radio.pack(side=tk.LEFT)

medium_radio = tk.Radiobutton(complexity_frame, text="Medium", variable=complexity_var, value=2)
medium_radio.pack(side=tk.LEFT)

complex_radio = tk.Radiobutton(complexity_frame, text="Complex", variable=complexity_var, value=3)
complex_radio.pack(side=tk.LEFT)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root)
password_entry.pack()

root.mainloop()
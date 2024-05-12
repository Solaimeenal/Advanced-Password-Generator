import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        self.label = tk.Label(master, text="Enter password length:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="")
        self.password_label.pack()

    def generate_password(self):
        try:
            length = int(self.entry.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer")
            
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choices(characters, k=length))

            self.password_label.config(text=f"Generated Password: {password}")
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

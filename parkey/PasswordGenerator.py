import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string

class PasswordGenerator(Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        
        if master:
            self.master.title("Password Generator")
            self.master.geometry("400x300")
        self.pack(expand=True, fill='both')
        self.configure(bg="#E8E2D6")
        
        main_frame = Frame(self, bg="#E8E2D6")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.length_label = Label(main_frame, text="Password Length:", font=("Arial", 12), bg="#E8E2D6")
        self.length_label.grid(row=0, column=0, pady=5, sticky="w")
        
        self.length_var = IntVar(value=12)
        self.length_entry = Entry(main_frame, textvariable=self.length_var, width=5, font=("Arial", 12))
        self.length_entry.grid(row=0, column=1, pady=5, sticky="w")
        
        self.uppercase_var = BooleanVar(value=True)
        self.uppercase_check = Checkbutton(main_frame, text="Include Uppercase", variable=self.uppercase_var, font=("Arial", 12), bg="#E8E2D6")
        self.uppercase_check.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")
        
        self.lowercase_var = BooleanVar(value=True)
        self.lowercase_check = Checkbutton(main_frame, text="Include Lowercase", variable=self.lowercase_var, font=("Arial", 12), bg="#E8E2D6")
        self.lowercase_check.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")
        
        self.numbers_var = BooleanVar(value=True)
        self.numbers_check = Checkbutton(main_frame, text="Include Numbers", variable=self.numbers_var, font=("Arial", 12), bg="#E8E2D6")
        self.numbers_check.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")
        
        self.symbols_var = BooleanVar(value=True)
        self.symbols_check = Checkbutton(main_frame, text="Include Symbols", variable=self.symbols_var, font=("Arial", 12), bg="#E8E2D6")
        self.symbols_check.grid(row=4, column=0, columnspan=2, pady=5, sticky="w")
        
        self.generate_button = Button(main_frame, text="Generate Password", command=self.generate_password, font=("Arial", 12, "bold"))
        self.generate_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        self.password_label = Label(main_frame, text="Generated Password:", font=("Arial", 12), bg="#E8E2D6")
        self.password_label.grid(row=6, column=0, pady=5, sticky="w")
        
        self.password_var = StringVar()
        self.password_entry = Entry(main_frame, textvariable=self.password_var, width=30, font=("Arial", 12))
        self.password_entry.grid(row=6, column=1, pady=5, sticky="w")

    def generate_password(self):
        length = self.length_var.get()
        include_uppercase = self.uppercase_var.get()
        include_lowercase = self.lowercase_var.get()
        include_numbers = self.numbers_var.get()
        include_symbols = self.symbols_var.get()
        
        if not any([include_uppercase, include_lowercase, include_numbers, include_symbols]):
            messagebox.showerror("Error", "You must select at least one character type.")
            return
            
        chars = ""
        if include_uppercase:
            chars += string.ascii_uppercase
        if include_lowercase:
            chars += string.ascii_lowercase
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += string.punctuation
            
        password = "".join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)

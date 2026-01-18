import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from pathlib import Path
from CreateNewPasswordProfile import *
from lib.user_data_manager import UserDataManager
from EditPasswordProfile import *
from PasswordGenerator import *

class MainMenu(Frame):
    def __init__(self, master=None,username = "", key=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.username = username
        self.key = key
        self.user_data_manager = UserDataManager(Path(__file__).parent)
        
        if master:
            self.master.title("Main Menu")
            self.master.attributes("-fullscreen", True)
        self.pack(expand=True, fill='both')
        self.configure(bg="#E8E2D6")
        
        self.main_frame = Frame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.search_var = StringVar()
        self.search_var.trace("w", lambda name, index, mode: self.filter_treeview())
        self.search_entry = Entry(self.main_frame, textvariable=self.search_var, font=("Arial", 12))
        self.search_entry.pack(pady=5, fill="x")

        self.tree = ttk.Treeview(self.main_frame, columns=("Username", "Password", "Link", "Note"), show="headings")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Link", text="Link")
        self.tree.heading("Note", text="Note")
        self.tree.pack(pady=10, fill="both", expand=True)
        
        self.show_password_profiles()
        
        button_frame = Frame(self.main_frame)
        button_frame.pack(pady=20)
        
        self.create_button = Button(button_frame, text="Create", width=20, height=1, command=self.Create_new_password_profile, font=('Arial', 16, 'bold'), borderwidth=5)
        self.create_button.grid(row=0, column=0, padx=10,pady=5)
        
        self.password_generator_button = Button(button_frame, text="Password Generator", width=20, height=1, command=self.open_password_generator, font=('Arial', 16, 'bold'), borderwidth=5)
        self.password_generator_button.grid(row=0, column=1, padx=10, pady=5)
        
        self.tree.bind("<Double-1>", self.on_double_click)

    def show_password_profiles(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.profiles = self.user_data_manager.get_user_password_profiles(self.username, self.key)
        
        for profile_name, profile_data in self.profiles.items():
            self.tree.insert("", "end", values=(profile_name, profile_data['password'], profile_data['link'], profile_data['notes']))

    def filter_treeview(self):
        search_query = self.search_var.get().lower()
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for profile_name, profile_data in self.profiles.items():
            if search_query in profile_name.lower():
                self.tree.insert("", "end", values=(profile_name, profile_data['password'], profile_data['link'], profile_data['notes']))

    def on_double_click(self, event):
        item = self.tree.selection()[0]
        profile_name = self.tree.item(item, "values")[0]
        profile_data = self.profiles[profile_name]
        self.edit_password_profile(profile_name, profile_data)

    def Create_new_password_profile(self):
        new_profile_window = tk.Toplevel(self.master)
        CreateNewPasswordProfile(new_profile_window, self.username, self.key)
        self.master.withdraw()
        self.master.bind("<Visibility>", lambda event: self.refresh_password_profiles())

    def edit_password_profile(self, profile_name, profile_data):
        edit_profile_window = tk.Toplevel(self.master)
        EditPasswordProfile(edit_profile_window, self.username, self.key, profile_name, profile_data)
        self.master.withdraw()
        self.master.bind("<Visibility>", lambda event: self.refresh_password_profiles())

    def delete_password_profile(self, profile_name):
        if messagebox.askyesno("Delete Profile", f"Are you sure you want to delete the profile '{profile_name}'?"):
            del self.profiles[profile_name]
            self.user_data_manager.save_user_password_profiles(self.username, self.key, self.profiles)
            self.refresh_password_profiles()

    def copy_to_clipboard(self, password):
        self.master.clipboard_clear()
        self.master.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

    def open_password_generator(self):
        password_generator_window = tk.Toplevel(self.master)
        PasswordGenerator(password_generator_window)

    def refresh_password_profiles(self):
        self.show_password_profiles()

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk

from lib.user_data_manager import UserDataManager

class EditPasswordProfile(Frame):
    def __init__(self,master=None,username = "", key=None, profile_name="", profile_data=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.username = username
        self.key = key
        self.profile_name = profile_name
        self.profile_data = profile_data
        self.user_data_manager = UserDataManager(Path(__file__).parent)

        if master:
            self.master.title("Edit profile")
            self.master.attributes("-fullscreen", True)
        self.pack(expand=True, fill='both')
        self.configure(bg="#E8E2D6")
        
        bg2_path = (Path(__file__).parent / 'bg' / 'bg3.png')
        imgbg = Image.open(bg2_path)
        w, h = imgbg.size
        imgbg = imgbg.resize((int(w * 0.82), int(h * 0.82)), Image.LANCZOS)
        self.bg2 = ImageTk.PhotoImage(imgbg, master=self)
        self.bg2_label = tk.Label(self, image=self.bg2, borderwidth=0)
        self.bg2_label.place(relx=0, rely=0)

        #FRAME CHO BUTTON

        button2_frame = Frame(self)
        button2_frame.place(relx=0.75, rely=0.5, anchor='center')
        button2_frame.config(bg="#E8E2D6")
        
        Text1 = tk.Label(button2_frame, text="EDIT NOTE", font=('Arial', 30, 'bold'), bg="#E8E2D6")
        Text1.grid(row=0, column=0, pady=10)

        self.username_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.username_entry.insert(0, self.profile_name)
        self.username_entry.grid(row=1, column=0, pady=10)
        self.username_entry.config(state='disabled')

        self.password_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.password_entry.insert(0, self.profile_data['password'])
        self.password_entry.grid(row=2, column=0, pady=10)

        self.link_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.link_entry.insert(0, self.profile_data['link'])
        self.link_entry.grid(row=3, column=0, pady=10)
        
        self.notes_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.notes_entry.insert(0, self.profile_data['notes'])
        self.notes_entry.grid(row=4, column=0, pady=10)
    
        self.create_but = Button(button2_frame, text="Save", width=20, height=1, command=self.Save_password_profile, font=('Arial', 16, 'bold'), borderwidth=5)
        self.create_but.grid(row=5, column=0, pady=10)
        self.create_but.bind("<Enter>", lambda e: self.create_but.config(fg="#0066ff"))
        self.create_but.bind("<Leave>", lambda e: self.create_but.config(fg="#000000"))
        
        self.back_but = Button(button2_frame, text="Back", width=20, height=1, command=self.go_back, font=('Arial', 16, 'bold'), borderwidth=5)
        self.back_but.grid(row=6, column=0, pady=10)
        self.back_but.bind("<Enter>", lambda e: self.back_but.config(fg="#0066ff"))
        self.back_but.bind("<Leave>", lambda e: self.back_but.config(fg="#000000"))

    def Save_password_profile(self):
        profile_password = self.password_entry.get()
        profile_link = self.link_entry.get()
        profile_notes = self.notes_entry.get()

        if not profile_password:
            messagebox.showerror("Error", "Password is required!")
            return

        profiles = self.user_data_manager.get_user_password_profiles(self.username, self.key)
        
        profiles[self.profile_name] = {
            "password": profile_password,
            "link": profile_link,
            "notes": profile_notes,
        }

        self.user_data_manager.save_user_password_profiles(self.username, self.key, profiles)
        messagebox.showinfo("Success", f"Password profile '{self.profile_name}' saved successfully!")
        
        self.master.master.deiconify()
        self.master.withdraw()

    def go_back(self):
        self.master.master.deiconify()
        self.master.withdraw()

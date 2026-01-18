import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk

from lib.user_data_manager import UserDataManager

class CreateNewPasswordProfile(Frame):
    def __init__(self,master=None,username = "", key=None):
        tk.Frame.__init__(self,master)
        self.master = master
        self.username = username
        self.key = key
        self.user_data_manager = UserDataManager(Path(__file__).parent)

        if master:
            self.master.title("New profile")
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
        
        Text1 = tk.Label(button2_frame, text="ADD NOTE", font=('Arial', 30, 'bold'), bg="#E8E2D6")
        Text1.grid(row=0, column=0, pady=10)

        self.username_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.username_entry.insert(0, '👤Username')
        self.username_entry.grid(row=1, column=0, pady=10)

        self.username_entry.bind('<FocusIn>', self.user_focus_in)
        self.username_entry.bind('<FocusOut>', self.user_focus_out)
        
        pass_container = tk.Frame(button2_frame)
        pass_container.grid(row=2, column=0, columnspan=2, pady=10)

        self.password_entry = tk.Entry(pass_container, width=21, fg='grey', font=('Arial', 16))
        self.password_entry.insert(0, '🔒Password')
        self.password_entry.pack(side="left")

        self.password_entry.bind('<FocusIn>', self.pw_focus_in)
        self.password_entry.bind('<FocusOut>', self.pw_focus_out)
        
        # Hold to reveal button
        self.reveal_password = Button(pass_container, text="🙈", relief="raised")
        self.reveal_password.pack(side="left", padx=2)
        self.reveal_password.bind("<ButtonPress-1>", self.pressed_reveal_password)
        self.reveal_password.bind("<ButtonRelease-1>", self.released_reveal_password)
        
        self.link_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.link_entry.insert(0, '🌐Link')
        self.link_entry.grid(row=3, column=0, pady=10)

        self.link_entry.bind('<FocusIn>', self.link_focus_in)
        self.link_entry.bind('<FocusOut>', self.link_focus_out)
        
        self.notes_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.notes_entry.insert(0, '✎Note')
        self.notes_entry.grid(row=4, column=0, pady=10)

        self.notes_entry.bind('<FocusIn>', self.note_focus_in)
        self.notes_entry.bind('<FocusOut>', self.note_focus_out)
    
        self.create_but = Button(button2_frame, text="Save", width=20, height=1, command=self.Save_password_profile, font=('Arial', 16, 'bold'), borderwidth=5)
        self.create_but.grid(row=5, column=0, pady=10)
        self.create_but.bind("<Enter>", lambda e: self.create_but.config(fg="#0066ff"))
        self.create_but.bind("<Leave>", lambda e: self.create_but.config(fg="#000000"))
    
    def user_focus_in(self, event):
        if self.username_entry.get() == '👤Username':
            self.username_entry.delete(0, tk.END)
            self.username_entry.config(fg="#000000")

    def user_focus_out(self, event):
        if self.username_entry.get() == '':
            self.username_entry.insert(0,'👤Username')
            self.username_entry.config(fg='grey')

    def pw_focus_in(self, event):
        if self.password_entry.get() == '🔒Password':
            self.password_entry.delete(0, tk.END)
            self.password_entry.config(fg="#000000")
            self.password_entry.config(show="*")

    def pw_focus_out(self, event):
        if self.password_entry.get() == '':
            self.password_entry.insert(0,'🔒Password')
            self.password_entry.config(fg='grey')
            self.password_entry.config(show="")

    def link_focus_in(self, event):
        if self.link_entry.get() == '🌐Link':
            self.link_entry.delete(0, tk.END)
            self.link_entry.config(fg="#000000")

    def link_focus_out(self, event):
        if self.link_entry.get() == '':
            self.link_entry.insert(0,'🌐Link')
            self.link_entry.config(fg='grey')

    def note_focus_in(self, event):
        if self.notes_entry.get() == '✎Note':
            self.notes_entry.delete(0, tk.END)
            self.notes_entry.config(fg="#000000")

    def note_focus_out(self, event):
        if self.notes_entry.get() == '':
            self.notes_entry.insert(0,'✎Note')
            self.notes_entry.config(fg='grey')

    def pressed_reveal_password(self, event):
        self.password_entry.config(show="")
        self.reveal_password.config(text="👁", bg="lightblue")
    
    def released_reveal_password(self, event):   
        self.password_entry.config(show="*")
        self.reveal_password.config(text="🙈", bg="SystemButtonFace")

    def Save_password_profile(self):
        profile_username = self.username_entry.get()
        profile_password = self.password_entry.get()
        profile_link = self.link_entry.get()
        profile_notes = self.notes_entry.get()

        if not profile_username or not profile_password:
            messagebox.showerror("Error", "Username and Password are required!")
            return

        profiles = self.user_data_manager.get_user_password_profiles(self.username, self.key)
        
        if profile_username in profiles:
            response = messagebox.askyesno("Overwrite?", 
                f"Profile '{profile_username}' already exists.\nOverwrite it?")
            if not response:
                return

        profiles[profile_username] = {
            "password": profile_password,
            "link": profile_link,
            "notes": profile_notes,
        }

        self.user_data_manager.save_user_password_profiles(self.username, self.key, profiles)
        messagebox.showinfo("Success", f"Password profile '{profile_username}' saved successfully!")
        
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.link_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)
        
        self.master.master.deiconify()
        self.master.withdraw()
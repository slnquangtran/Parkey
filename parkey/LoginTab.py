import tkinter as tk
from tkinter import *
from tkinter import messagebox
from pathlib import Path
from menu import *
from PIL import Image, ImageTk

from lib.user_data_manager import UserDataManager

class LoginTab(Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.user_data_manager = UserDataManager(Path(__file__).parent)

        if master:
            self.master.title("Login")
            self.master.attributes("-fullscreen", True)
        self.pack(expand=True, fill='both')
        self.configure(bg="#E8E2D6")
        

        bg2_path = (Path(__file__).parent / 'bg' / 'bg2.png')
        imgbg = Image.open(bg2_path)
        w, h = imgbg.size
        imgbg = imgbg.resize((int(w * 0.82), int(h * 0.82)), Image.LANCZOS)
        self.bg2 = ImageTk.PhotoImage(imgbg)

        self.bg2_label = tk.Label(self, image=self.bg2, borderwidth=0)
        self.bg2_label.place(relx=0, rely=0)

        #FRAME CHO BUTTON
        button2_frame = Frame(self)
        button2_frame.place(relx=0.75, rely=0.5, anchor='center')
        button2_frame.config(bg="#E8E2D6")
        
        Text1 = tk.Label(button2_frame, text="SIGN IN", font=('Arial', 30, 'bold'), bg="#E8E2D6")
        Text1.grid(row=0, column=1, pady=10)

        Text2 = tk.Label(button2_frame, text="Login your account to start the service", font=('Arial', 16), bg="#E8E2D6")
        Text2.grid(row=1, column=1, pady=10)

        #USERNAME ENTRY
        self.username_entry = tk.Entry(button2_frame, width=23, fg='grey', font=('Arial', 16))
        self.username_entry.insert(0, '👤Username')
        self.username_entry.grid(row=2, column=1, pady=10)

        self.username_entry.bind('<FocusIn>', self.user_focus_in)
        self.username_entry.bind('<FocusOut>', self.user_focus_out)
        
        pass_container = tk.Frame(button2_frame)
        pass_container.grid(row=3, column=1, columnspan=2, pady=10)

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
        
        # Login button
        self.login_but = Button(button2_frame, text="Login", width=20, height=1, command=self.LoginUser, font=('Arial', 16, 'bold'), borderwidth=5)
        self.login_but.grid(row=4, column=1, pady=10)
        self.login_but.bind("<Enter>", lambda e: self.login_but.config(fg="#0066ff"))
        self.login_but.bind("<Leave>", lambda e: self.login_but.config(fg="#000000"))
        
        # Back button
        self.back_but = Button(button2_frame, text="Back", width=20, height=1, command=self.go_back, font=('Arial', 16, 'bold'), borderwidth=5)
        self.back_but.grid(row=5, column=1, pady=10)
        self.back_but.bind("<Enter>", lambda e: self.back_but.config(fg="#0066ff"))
        self.back_but.bind("<Leave>", lambda e: self.back_but.config(fg="#000000"))

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
            

    def pressed_reveal_password(self, event):
        self.password_entry.config(show="")
        self.reveal_password.config(text="👁", bg="lightblue")
    
    def released_reveal_password(self, event):   
        self.password_entry.config(show="*")
        self.reveal_password.config(text="🙈", bg="SystemButtonFace")
    
    def go_back(self):
        # Create a new window for login
        self.master.master.deiconify()
        self.master.withdraw()  # Close current window
    
    def LoginUser(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return
            
        key = self.user_data_manager.authenticate_user(username, password)
        
        if key:
            messagebox.showinfo("Success", f"Welcome back, {username}!")
            main_menu_window = tk.Tk()
            MainMenu(main_menu_window, username, key)
            self.master.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password!")
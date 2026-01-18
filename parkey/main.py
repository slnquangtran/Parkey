import tkinter as tk
from tkinter import *
from pathlib import Path
from menu import *
from LoginTab import *
from RegisterTab import *
from PIL import Image, ImageTk

class LoginStep01(Frame):
    def __init__(self, master=None):
        # Pass master to the parent Frame class
        tk.Frame.__init__(self, master)
        
        # Store master reference
        self.master = master
        
        if master:
            self.master.title("Password Manager")
            self.master.configure(bg="#E8E2D6")
            self.master.attributes("-fullscreen", True)
        
        self.pack(expand=True, fill='both')
        self.configure(bg="#E8E2D6")

        bg_path = (Path(__file__).parent / 'bg' / 'bg.png')
        img = Image.open(bg_path)
        w, h = img.size
        img = img.resize((int(w * 1.1), int(h * 1)), Image.LANCZOS)
        self.icon = ImageTk.PhotoImage(img)

        self.icon_label = tk.Label(self, image=self.icon, borderwidth=0)
        self.icon_label.place(relx=0, rely=0)
        
        # Use a frame for better button layout
        button_frame = Frame(self)
        button_frame.place(relx=0.75, rely=0.5, anchor='center')
        button_frame.configure(bg="#E8E2D6")

        Text1 = tk.Label(button_frame, text="Password Manager 🔑", font=('Arial', 30, 'bold'), bg="#E8E2D6")
        Text1.grid(row=0, column=0, pady=30)
        
        # Login button
        self.button1 = Button(button_frame, text="Login", width=20, height=1, command=self.Login_tab, font=('Arial', 16, 'bold'), borderwidth=5)
        self.button1.grid(row=1, column=0, padx=10, pady=5)
        self.button1.bind("<Enter>", lambda e: self.button1.config(fg="#0066ff"))
        self.button1.bind("<Leave>", lambda e: self.button1.config(fg="#000000"))
        
        # Register button
        self.button2 = Button(button_frame, text="Register", width=20, height=1, command=self.Register_tab, font=('Arial', 16, 'bold'), borderwidth=5)
        self.button2.grid(row=2, column=0, padx=10, pady=5)
        self.button2.bind("<Enter>", lambda e: self.button2.config(fg="#0066ff"))
        self.button2.bind("<Leave>", lambda e: self.button2.config(fg="#000000"))


    def Login_tab(self):
        # Create a new window for login
        login_window = tk.Toplevel(self.master)
        LoginTab(login_window)
        self.master.withdraw()
    
    def Register_tab(self):
        # Create a new window for register
        register_window = tk.Toplevel(self.master)
        RegisterTab(register_window)
        self.master.withdraw()
    
def main(): 
    root = tk.Tk()
    root.geometry("300x150")
    
    app = LoginStep01(root)  # Pass root window as master
    root.title("Password Manager")
    try:
        # Convert Path to string for tkinter
        icon_path = (Path(__file__).parent / 'logo.png')
        
        # Check if file exists
        if icon_path.exists():
            # Try to load the image
            icon_img = tk.PhotoImage(file=icon_path)
            root.iconphoto(False, icon_img)
            print(f"Icon loaded from: {icon_path}")
        else:
            print(f"Icon file not found: {icon_path}")
                
    except Exception as e:
        print(f"Could not load icon: {e}")
        # Continue without icon - not critical
    root.mainloop()

if __name__ == '__main__':
    main()
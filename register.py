from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Face Recognition System\Photos\background5.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left background image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Face Recognition System\Photos\registrationlogo.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=90, y=100, width=470, height=550)

        # entry frame
        frame = Frame(self.root, bg="white")
        frame.place(x=560, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=20, y=20)

        # label & entry
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=50, y=100)
        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        l_name.place(x=370, y=100)
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # row 2
        contact = Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # row 3
        security_Q = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_Q.place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Mother Name", "Your Pet Name", "Your First School Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=370, y=240)
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # row 4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_pswd.place(x=370, y=310)
        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*")
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # check button
        self.var_check = IntVar()
        checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree the Terms & Conditions", font=("times new roman", 11, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=400)

        # register button
        img = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\registerbtn2.jpg")
        img = img.resize((200, 56), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2")
        b1.place(x=30, y=450, width=200)

        # login button
        img1 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\loginbtn1.JPG")
        img1 = img1.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b2.place(x=265, y=453, width=200)

    # ✅ Moved inside class (proper indentation)
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to the Terms & Conditions", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="V@rathod123",
                    database="face_detection_attendance"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
                else:
                    my_cursor.execute(
                        "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_securityA.get(),
                            self.var_pass.get()
                        )
                    )
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Register Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()

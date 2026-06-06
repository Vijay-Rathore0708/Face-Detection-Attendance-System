from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
from tkinter import filedialog
import numpy as np
from main import FaceRecognitionSystem


def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\iipslogin2.jpg")
        self.bg = self.bg.resize((1550, 800), Image.Resampling.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg)

        lbl_bg = Label(self.root, image=self.bg_image)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="white")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\loginlogo2.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=100)

        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username.place(x=70, y=152)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password.place(x=70, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\userlogo1.png")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="white", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\locklogo1.png")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="white", borderwidth=0)
        lblimg1.place(x=650, y=390, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3,
                          relief=RIDGE, fg="white", bg="blue")
        loginbtn.place(x=110, y=300, width=120, height=35)

        registerbtn = Button(frame, text="New User Register", command=self.register_window,
                             font=("times new roman", 12, "bold"), borderwidth=0, fg="black", bg="white")
        registerbtn.place(x=15, y=350, width=160)

        registerbtn = Button(frame, text="Forgot Password", font=("times new roman", 12, "bold"),
                             borderwidth=0, fg="black", bg="white")
        registerbtn.place(x=7, y=375, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All field are required")
        elif self.txtuser.get() == "Vijay Rathod" and self.txtpass.get() == "vijay123":
            messagebox.showinfo("success", "Successfully logged in to IIPS")
            self.new_window = Toplevel(self.root)
            self.app = FaceRecognitionSystem(self.new_window)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="V@rathod123",
                database="face_detection_attendance"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = FaceRecognitionSystem(self.new_window)
                else:
                    return
            conn.commit()
            conn.close()

                
                 




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






class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background Image
        img = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\BLUE.jpg")
        img = img.resize((1500, 850), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1530, height=850)


        # STUDENT BUTTON
        img1 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student3.WEBP")
        img1 = img1.resize((165, 165), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(self.root, image=self.photoimg1, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=200, width=180, height=180)

        b1_1 = Button(self.root, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=200, y=350, width=180, height=40)

        
        # face detector BUTTON
        img2 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student1.WEBP")
        img2 = img2.resize((165, 165), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(self.root, image=self.photoimg2, cursor="hand2",command=self.face_data)
        b1.place(x=650, y=200, width=180, height=180)

        b1_1 = Button(self.root, text="Face-Detection", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=650, y=350, width=180, height=40)



        
        # Attendance BUTTON
        img3 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\Attendance1.WEBP")
        img3 = img3.resize((165, 165), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(self.root, image=self.photoimg3, cursor="hand2",command=self.attendance_data)
        b1.place(x=1100, y=200, width=180, height=180)

        b1_1 = Button(self.root, text="Attendance", cursor="hand2",command=self.attendance_data,
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=1100, y=350, width=180, height=40)




        
        # Train Data BUTTON
        img4 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\traindata2.WEBP")
        img4 = img4.resize((165, 165), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(self.root, image=self.photoimg4, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=465, width=180, height=180)

        b1_1 = Button(self.root, text="Train-Data", cursor="hand2",command=self.train_data,
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=200, y=643, width=180, height=40)


        # Photo BUTTON
        img5 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\photo1.WEBP")
        img5 = img5.resize((165, 165), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(self.root, image=self.photoimg5, cursor="hand2",command=self.open_img)
        b1.place(x=650, y=465, width=180, height=180)

        b1_1 = Button(self.root, text="Photo", cursor="hand2",command=self.open_img,
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=650, y=643, width=180, height=40)



        #  Help-Desk BUTTON
        img6 = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\help2.WEBP")
        img6 = img6.resize((165, 165), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(self.root, image=self.photoimg6, cursor="hand2",command=self.help_data)
        b1.place(x=1100, y=465, width=180, height=180)

        b1_1 = Button(self.root, text="Help-Desk", cursor="hand2",command=self.help_data,
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        b1_1.place(x=1100, y=643, width=180, height=40)


    def open_img(self):
        os.startfile("data")
        # ========Function BUtton=====
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)





    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognize(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)






class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =======variables========
        self.var_Dep = StringVar()
        self.var_Course = StringVar()
        self.var_Year = StringVar()
        self.var_Sem = StringVar()
        self.var_Name = StringVar()
        self.var_Roll = StringVar()
        self.var_Gender = StringVar()
        self.var_Email = StringVar()
        self.var_Phone = StringVar()
        self.var_Address = StringVar()
        self.var_Photo = StringVar()
        self.var_DOB = StringVar()
        self.var_ID = StringVar()
        self.var_Div = StringVar()
        self.var_Teacher = StringVar()

        # title 
        # Background Image
        img = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\BLUE.jpg")
        img = img.resize((1500, 850), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1530, height=850)

        title_lbl = Label(f_lbl, text="Student Record System",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=57, width=1530, height=60)

        # frames
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=23, y=140, width=1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("bold", 12))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student1.WEBP")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=720, height=130)

        # current course 
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("bold", 12))
        current_course_frame.place(x=5, y=135, width=715, height=122)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=15, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Dep, font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "IIPS", "IMS", "EMRC", "SOC", "SOP", "SOE", "SJMC")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Course, font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "MBA", "MTECH", "MCA", "CS")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2k21", "2k22", "2k23", "2k24", "2k25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_Sem, font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8", "Semester-9", "Semester-10")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # class student information 
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("bold", 12))
        class_Student_frame.place(x=5, y=265, width=715, height=290)

        # Student ID
        studentId_label = Label(class_Student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_Student_frame, textvariable=self.var_ID, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studenName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studenName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_Student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        class_div_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Div, width=20, font=("times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_Student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Roll, width=20, font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Gender, width=20, font=("times new roman", 13, "bold"))
        gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_DOB, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # phone no
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Address, width=20, font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_Student_frame, textvariable=self.var_Teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        radiobtn2 = ttk.Radiobutton(class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # buttons frame
        btn_frame = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=710, height=40)

        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, command=self.update_data, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame,command=self.delete_data, text="Delete", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame,command=self.reset_data, text="Reset", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        # take and update frame

        btn_frame1 = Frame(class_Student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=710, height=35)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        img_right = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student2.WEBP")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl_right = Label(Right_frame, image=self.photoimg_right)
        f_lbl_right.place(x=5, y=0, width=720, height=130)

         # ======Search System======
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 15, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)
        # ======== Table Frame ===========
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            table_frame,
            columns=("Dep", "Course", "Year", "Sem","ID","Name", "Division", "Roll", "Gender","DOB", "Email", "Phone", "Address","Teacher", "Photo"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("ID", text="Stud_ID")
        self.student_table.heading("Name", text="Stud_Name")
        self.student_table.heading("Division", text="Division")
        self.student_table.heading("Roll", text="Roll No.")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone No.")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Division", width=100)
        self.student_table.column("Roll", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Teacher", width=100)
        self.student_table.column("Photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # def student_details(self):
    #     self.new_window = Toplevel(self.root)
    #     self.app = student(self.new_window)

    def add_data(self):
        if self.var_Dep.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields are Required")
        else:
            try:
                conn = mysql.connector.connect(host="127.0.0.1", user="root", password="V@rathod123", database="face_detection_attendance")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_Dep.get(),
                        self.var_Course.get(),
                        self.var_Year.get(),
                        self.var_Sem.get(),
                        self.var_ID.get(),
                        self.var_Name.get(),
                        self.var_Div.get(),
                        self.var_Roll.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(), 
                        self.var_Email.get(),
                        self.var_Phone.get(),
                        self.var_Address.get(),
                        self.var_Teacher.get(),
                        self.var_Photo.get(),
                        
                     
                    )
                )

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)


    # ==============fetch data================
    def fetch_data(self):
        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="V@rathod123", database="face_detection_attendance")  
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # ============get cursor======



    def get_cursor(self,event=""):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"]

            self.var_Dep.set(data[0]),
            self.var_Course.set(data[1])
            self.var_Year.set(data[2]),
            self.var_Sem.set(data[3]),
            self.var_ID.set(data[4]),
            self.var_Name.set(data[5]),
            self.var_Div.set(data[6]),
            self.var_Roll.set(data[7]),
            self.var_Gender.set(data[8]),
            self.var_DOB.set(data[9]),
            self.var_Email.set(data[10]),
            self.var_Phone.set(data[11]),
            self.var_Address.set(data[12]),
            self.var_Teacher.set(data[13]),
            self.var_radio1.set(data[14])
    
    # update fuction
    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Upadte","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="V@rathod123", database="face_detection_attendance") 
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where ID=%s",(
                                                                                        self.var_Dep.get(),
                                                                                        self.var_Course.get(),
                                                                                        self.var_Year.get(),
                                                                                        self.var_Sem.get(),
                                                                                        self.var_Name.get(),
                                                                                        self.var_Div.get(),
                                                                                        self.var_Roll.get(),
                                                                                        self.var_Gender.get(),
                                                                                        self.var_DOB.get(), 
                                                                                        self.var_Email.get(),
                                                                                        self.var_Phone.get(),
                                                                                        self.var_Address.get(),
                                                                                        self.var_Teacher.get(),
                                                                                        self.var_Photo.get(),
                                                                                        self.var_ID.get(),
                                                                                    ))
                else:
                    if not Upadate:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    #delete function
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this Student",parent=self.root)    
                if delete>0:
                    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="V@rathod123", database="face_detection_attendance")    
                    my_cursor=conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_ID.get(),) 
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully deleted details",parent=self.root)   
            except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # reset buttton
    def reset_data(self):
            self.var_Dep.set("Select Department"),
            self.var_Course.set("Select Course")
            self.var_Year.set("Select Year"),
            self.var_Sem.set("Select Semester"),
            self.var_ID.set(""),
            self.var_Name.set(""),
            self.var_Div.set(""),
            self.var_Roll.set(""),
            self.var_Gender.set(""),
            self.var_DOB.set(""),
            self.var_Email.set(""),
            self.var_Phone.set(""),
            self.var_Address.set(""),
            self.var_Teacher.set(""),
            self.var_radio1.set("")


    # ==========Generate data set and take photo sample===========\
    def generate_dataset(self):
        if self.var_Dep.get() == "Select Department" or self.var_Name.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="V@rathod123",
                database="face_detection_attendance"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult = my_cursor.fetchall()
            student_id = 0
            for x in myresult:
                student_id += 1

            my_cursor.execute("""
                update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,
                Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,
                Teacher=%s,PhotoSample=%s where ID=%s
            """, (
                self.var_Dep.get(),
                self.var_Course.get(),
                self.var_Year.get(),
                self.var_Sem.get(),
                self.var_Name.get(),
                self.var_Div.get(),
                self.var_Roll.get(),
                self.var_Gender.get(),
                self.var_DOB.get(),
                self.var_Email.get(),
                self.var_Phone.get(),
                self.var_Address.get(),
                self.var_Teacher.get(),
                self.var_Photo.get(),
                self.var_ID.get(),
            ))

            conn.commit()
            self.fetch_data()
            self.reset_data()  # ✅ added parentheses
            conn.close()

            # ========= Load Haarcascade for face detection =======
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face = img[y:y+h, x:x+w]
                    return face
                return None

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to access camera.", parent=self.root)
                    break

                face = face_cropped(my_frame)
                if face is not None:
                    img_id += 1
                    face = cv2.resize(face, (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    file_name_path = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name_path, face)

                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                else:
                    cv2.imshow("Cropped Face", my_frame)

                if cv2.waitKey(1) == 13 or img_id == 100:  # 13 = Enter key
                    break

            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating dataset completed successfully!", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="TRAIN DATA SET",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student3.WEBP")
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=340)
      #  button

        b1_1 = Button(self.root, text="TRAIN DATA ",command=self.train_classifier,cursor="hand2",
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=340, width=1530, height=60) 

        
     


        img_bottom = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student3.WEBP")
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_lbl_bottom.place(x=0, y=400, width=1530, height=340)
         
        
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert()  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        ####Train the classifier and save    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")  
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !")                        


class Face_Recognize:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title Label
        title_lbl = Label(self.root, text="FACE DETECTOR",
                          font=("times new roman", 35, "bold"),
                          bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Image
        img_top = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student3.WEBP")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Bottom Image
        img_bottom = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student3.WEBP")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
        f_lbl_bottom.place(x=650, y=55, width=950, height=700)

        # === Button ===
        b1_1 = Button(self.root, text="DETECT FACE", cursor="hand2", command=self.face_recog,
                      font=("times new roman", 30, "bold"), bg="red", fg="white")
        b1_1.place(x=0, y=340, width=1530, height=60)

    # ===================attendance==================
    def mark_attendance(self, i, r, n, d):
        with open("IIPS.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



    # === Face recognition function ===
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="V@rathod123",
                    database="face_detection_attendance"
                )
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where ID=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n is not None else "Unknown"

                my_cursor.execute("select Roll from student where ID=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r is not None else "Unknown"

                my_cursor.execute("select Department from student where ID=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d is not None else "Unknown"

                my_cursor.execute("select ID from student where ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i) if d is not None else "Unknown"


                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Name:{n}", (x, y - 30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0), 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()



mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =============variables===============

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # Background Image
        img = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\BLUE.jpg")
        img = img.resize((1500, 850), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1530, height=850)

        title_lbl = Label(f_lbl, text=" ATTENDANCE SYSTEM",
                          font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=57, width=1530, height=60)

        # frames
        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=23, y=140, width=1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("bold", 12))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student1.WEBP")
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)
        f_lbl_left.place(x=5, y=0, width=720, height=130)

        left_inside_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("bold", 12))
        left_inside_frame.place(x=5, y=135, width=715, height=418)

        # ====labels and entry=======
        # attendance id ==

        attendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceId_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id, width=20, font=("times new roman", 13, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W) 

        # Name
        rollLabel = Label(left_inside_frame, text="Roll:", bg="white", font="comicsansns 11 bold")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)

        atten_roll = ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll ,width=22, font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # date
        nameLabel = Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame,textvariable=self.var_atten_name, width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep, width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timeLabel = Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame,textvariable=self.var_atten_time ,width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame,textvariable=self.var_atten_date ,width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance
        attendanceLabel = Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=710, height=40)

        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data ,width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)



        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        # ======== Scroll bar table ========
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,
                                                column=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                xscrollcommand=scroll_x.set,
                                                yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview) 
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # =========fetch data=========
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # =========import csv=========
    def importCsv(self):
        global mydata
        mydata = []
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                        filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
        print(mydata)  # 🔍 Debug check
        self.fetchData(mydata)
    # export csv
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV",
                                            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")



class Help:
    def __init__(self, root):  # ✅ Corrected: __init__ (double underscores)
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # ✅ Background Image
        img = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\BLUE.jpg")
        img = img.resize((1500, 850), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0, y=0, width=1530, height=850)

        # ✅ Title Label
        title_lbl = Label(
            f_lbl,
            text="HELP DESK",
            font=("times new roman", 35, "bold"),
            bg="white",
            fg="black"
        )
        title_lbl.place(x=0, y=57, width=1530, height=60)

        img_right = Image.open(r"C:\Users\DELL\Desktop\Face Recognition System\Photos\student2.WEBP")
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl_right = Label(self.root, image=self.photoimg_right)
        f_lbl_right.place(x=380, y=200, width=745, height=450)

        f_lbl_right = Label(self.root, image=self.photoimg_right)
        f_lbl_right.place(x=380, y=150, width=745, height=460)

        dev_label = Label(self.root,
            text="     Email: vijayrathore0708@gmail.com      ",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="black")
        dev_label.place(x=380, y=610)
   
        dev_label1 = Label(self.root,
            text="     Email: rahul@gmail.com      ",
            font=("times new roman", 30, "bold"),
            bg="white",
            fg="black")
        dev_label1.place(x=470, y=560)







if __name__ == "__main__":
    main()

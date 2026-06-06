from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

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







if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()

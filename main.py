from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import student
from train import Train
from face_recognize import Face_Recognize
from attendance import Attendance
from help import Help

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


    


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

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
    root = Tk()
    obj = Help(root)
    root.mainloop()

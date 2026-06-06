from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


class RoundedFrame(Canvas):
    def __init__(self, parent, width, height, corner_radius=60, bg_color="white", **kwargs):
        super().__init__(parent, width=width, height=height, bg=parent["bg"], highlightthickness=0, **kwargs)

        self.corner_radius = corner_radius
        self.bg_color = bg_color

        # Draw rounded rectangle
        self.round_rect = self._draw_rounded_rect(0, 0, width, height, corner_radius, fill=bg_color, outline="")

    def _draw_rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1,
            x2, y1+r,
            x2, y2-r,
            x2, y2,
            x2-r, y2,
            x1+r, y2,
            x1, y2,
            x1, y2-r,
            x1, y1+r,
            x1, y1
        ]
        return self.create_polygon(points, smooth=True, **kwargs)


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Face Recognition System\Photos\background5.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left background image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\DELL\Desktop\Face Recognition System\Photos\registrationlogo.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=90, y=100, width=470, height=550)

        # more rounded entry frame
        frame = RoundedFrame(self.root, width=800, height=550, corner_radius=60, bg_color="white")
        frame.place(x=560, y=100)

        # container inside the rounded frame
        container = Frame(frame, bg="white")
        container.place(x=0, y=0, width=800, height=550)

        register_lbl = Label(container, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="black", bg="white")
        register_lbl.place(x=20, y=20)

        # label & entry
        fname = Label(container, text="First Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        fname.place(x=50, y=100)

        fname_entry = ttk.Entry(container, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        l_name = Label(container, text="Last Name", font=("times new roman", 15, "bold"), fg="black", bg="white")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(container, font=("times new roman", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # row 2
        contact = Label(container, text="Contact No.", font=("times new roman", 15, "bold"), fg="black", bg="white")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(container, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(container, text="Email", font=("times new roman", 15, "bold"), fg="black", bg="white")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(container, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # row 3
        security_Q = Label(container, text="Select Security Question", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(container, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Mother Name", "Your Pet Name", "Your First School Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(container, text="Security Answer", font=("times new roman", 15, "bold"), fg="black", bg="white")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(container, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # row 4
        pswd = Label(container, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(container, font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(container, text="Confirm Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(container, font=("times new roman", 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # check button
        checkbtn = Checkbutton(container, text="I Agree the Terms & Conditions", font=("times new roman", 11, "bold"), onvalue=1, offvalue=0, bg="white")
        checkbtn.place(x=50, y=400)


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()

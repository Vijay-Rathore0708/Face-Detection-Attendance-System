    def register_data(self):
        if self.var_fname.get()==" " or self.var_email.get()==" " or self.var_securityQ.get()=="Select":
             messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
             messagebox.showerror("Error","Password & Confirm password must be same")
        elif self.var_check.get()==0:
             messagebox.showerror("Error","Please agree terms & condition")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="V@rathod123", database="face_detection_attendance")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

        if row != None:
            messagebox.showerror("Error", "User already exist, please try another email")
        else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_SecurityA.get(),
                                                                                    self.var_pass.get()
                                                                                    ))

        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Register Successfully"
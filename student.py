from cgitb import text
from email import message
from multiprocessing import connection
from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import cvtColor
import mysql.connector
import cv2


class Student:

    #================================== Add function declaration =============================
    def add_student(self):
        if self.var_dept.get() =="Select Department" or self.var_studentName.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","Ooops!, all fields are required!",parent=self.root)
        else:
            try:
                #======================== MySQL Database connection ==============================
                conn=mysql.connector.connect(host='localhost',username="root",password="yourdatabasepassword",database="sms_face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_campus.get(),
                    self.var_course_duration.get(),
                    self.var_student_id.get(),
                    self.var_studentName.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone1.get(),
                    self.var_phone2.get(),
                    self.var_address.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Details successfully added to the database",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Caused By :{str(es)}",parent=self.root)
    
    #================================== Fetch Data fuction =============================
    def fetch_data(self):
        #======================== Database connection ==============================
        conn=mysql.connector.connect(host='localhost',username="root",password="yourdatabasepassword",database="sms_face_recog")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        #Check if there is there
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            #loop
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #================================== Get Cursor Focus =============================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_campus.set(data[2]),
        self.var_course_duration.set(data[3]),
        self.var_student_id.set(data[4]),
        self.var_studentName.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone1.set(data[9]),
        self.var_address.set(data[10]),
        self.var_phone2.set(data[11]),
        #self.var_radio1.set(data[12]),

    #================================== Update Function =============================
    def update_data(self):
        if self.var_dept.get() =="Select Department" or self.var_studentName.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","Ooops!, select a field to update!",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you really want to update this student detail",parent=self.root)
                if update>0:
                    #======================== Database connection ==============================
                    conn=mysql.connector.connect(host='localhost',username="root",password="yourdatabasepassword",database="sms_face_recog")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,campus=%s,course_description=%s,student_name=%s,gender=%s,dob=%s,email=%s,phone_1=%s,address=%s,phone_2=%s, where student_id=%s",(
                        self.var_dept.get(),
                        self.var_course.get(),
                        self.var_campus.get(),
                        self.var_course_duration.get(),
                        self.var_studentName.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone1.get(),
                        self.var_address.get(),
                        self.var_phone2.get(),
                        self.var_student_id.get(),
                    ))
                else:
                    if not update:
                        return 
                messagebox.showinfo("Success","Student detail successfully updated.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #================================== Delete Function =============================
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Student is a required for deletion!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("About to Delete this Student Permanently","Are you sure you want to permanently delete this student's data?",parent=self.root)
                if delete>0:
                    #======================== Database connection ==============================
                    conn=mysql.connector.connect(host='localhost',username="root",password="yourdatabasepassword",database="sms_face_recog")
                    my_cursor=conn.cursor()
                    sql_query="delete from student where student_id=%s"
                    value=(self.var_student_id.get(),)
                    my_cursor.execute(sql_query,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Data successfully deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #================================== Clear Data Function =============================
    def clear_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_campus.set("Select Campus")
        self.var_course_duration.set("Select Course Duration")
        self.var_student_id.set("")
        self.var_studentName.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone1.set("")
        self.var_phone2.set("")
        self.var_address.set("")
        self.var_radio1.set("")


    #======================================== Generate Dataset for Photos ================================
    def generate_dataset(self):
        if self.var_dept.get() =="Select Department" or self.var_studentName.get()=="" or self.var_student_id.get()=="":
            messagebox.showerror("Error","Ooops!, select a field to update!",parent=self.root)
        else:
            try:
                #======================== Database connection ==============================
                conn=mysql.connector.connect(host='localhost',username="root",password="yourdatabasepassword",database="sms_face_recog")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                my_result=my_cursor.fetchall()
                id=0
                
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dept=%s,course=%s,campus=%s,course_description=%s,student_name=%s,gender=%s,dob=%s,email=%s,phone_1=%s,address=%s,phone_2=%s where student_id=%s",(
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_campus.get(),
                    self.var_course_duration.get(),
                    self.var_studentName.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone1.get(),
                    self.var_address.get(),
                    self.var_phone2.get(),
                    self.var_student_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()

                #========================== Load predefined data on the frontal face from opencv2 ========================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    #scaling factor=1.3
                    #minimum neighbors=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path_name="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path_name,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result Generated","Generating Image Dataset has completed successfully!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")
        

        #================================ Variable Declarations ====================
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_campus=StringVar()
        self.var_course_duration=StringVar()
        self.var_student_id=StringVar()
        self.var_studentName=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone1=StringVar()
        self.var_phone2=StringVar()
        self.var_address=StringVar()
        self.var_radio1=StringVar()


        bg_img=Image.open(r"C:\Users\Isaac NSB. Kargbo\Desktop\projects\student_attendance\images\bg.webp")
        bg_img=bg_img.resize((1920,1080),Image.Resampling.LANCZOS)
        self.bg_image=ImageTk.PhotoImage(bg_img)

        bg_img=Label(self.root,image=self.bg_image)
        bg_img.place(x=0,y=0,width=1940,height=1080)


        ######################## Project Title label ################################
        title_label=Label(bg_img,text="STUDENT ATTENDANCE SYSTEM WITH FACE RECOGNITION",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=50)


        #======================================= MAIN FRAME ===================================#
        main_frame=Frame(bg_img,bd=3)
        main_frame.place(x=0,y=50,width=1920,height=1030)


        #======================================= LEFT FRAME ===================================#
        left_frame=LabelFrame(main_frame,bd=2,text="STUDENT DETAILS",font=('times new roman',12,'bold'),bg="white",fg="black",relief="ridge")
        left_frame.place(x=0,y=10,width=700,height=950)


        #======================================= COURSE FRAME ===================================#
        course_frame=LabelFrame(left_frame,bd=2,text="COURSE DETAILS",font=('times new roman',12,'bold'),bg="white",fg="black",relief="ridge")
        course_frame.place(x=5,y=15,width=680,height=150)

        #================= DEPARTMENT ====================#
        deparment_label=Label(course_frame,text="Department",font=('times new roman',12,'bold'),bg="white")
        deparment_label.grid(row=0,column=0,padx=5,pady=10)

        department_combo=ttk.Combobox(course_frame,textvariable=self.var_dept,font=('times new roman',12,'bold'),width=26,state="read only")
        department_combo["values"]=(
            "Select Department",
            "Physics and Computer",
            "Sociology",
            "Public Health",
        )
        department_combo.current(0)
        department_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)


        #================= COURSE ====================#
        course_label=Label(course_frame,text="COURSE",font=('times new roman',12,'bold'),bg="white")
        course_label.grid(row=0,column=2,padx=5,pady=10)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_course,font=('times new roman',12,'bold'),width=23,state="read only")
        course_combo["values"]=(
            "Select Course",
            "Computer Science",
            "Business Information Technology",
            "Engineering",
            "Maths and Statistics",
            "Telecommunications",
            "Business Administration",
            "Economics",
            "Agric General"
        )
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        #================= CAMPUS ====================#
        course_label=Label(course_frame,text="Campus",font=('times new roman',12,'bold'),bg="white")
        course_label.grid(row=1,column=0,padx=0,pady=10)

        course_combo=ttk.Combobox(course_frame,textvariable=self.var_campus,font=('times new roman',12,'bold'),width=23,state="read only")
        course_combo["values"]=(
            "Select Campus",
            "Njala University - Njala Campus",
            "Njala University - Bo Torwama",
            "Njala University - Bo Kowama",
            "Njala University - Henry Street",
        )
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #================= CAMPUS ====================#
        # campus_label=Label(course_frame,text="Campus",font=('times new roman',12,'bold'),bg="white")
        # campus_label.grid(row=1,column=0,padx=0,pady=10)

        # campus_combo=ttk.Combobox(course_frame,textvariable=var_campus,font=('times new roman',12,'bold'),width=25,state="read only")
        # campus_combo["values"]=(
        #     "Select Campus",
        #     "Njala University - Njala Campus",
        #     "Njala University - Bo Torwama",
        #     "Njala University - Bo Kowama",
        #     "Njala University - Henry Street",
        # )
        # campus_combo.current(0)
        # campus_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)


        #================= COURSE DURATION ====================#
        course_duration_label=Label(course_frame,text="Course Duration",font=('times new roman',12,'bold'),bg="white")
        course_duration_label.grid(row=1,column=2,padx=0,pady=10)

        course_duration_combo=ttk.Combobox(course_frame,textvariable=self.var_course_duration,font=('times new roman',12,'bold'),width=23,state="read only")
        course_duration_combo["values"]=(
            "Select Course Duration",
            "4 Years",
            "3 Years",
            "2 Years",
            "18 Months",
            "6 Months",
        )
        course_duration_combo.current(0)
        course_duration_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)


        #======================================= PERSONAL DETAIL FRAME ===================================#
        personal_info_frame=LabelFrame(left_frame,bd=2,text="PERSONAL DETAIL",font=('times new roman',12,'bold'),bg="white",fg="black",relief="ridge")
        personal_info_frame.place(x=5,y=170,width=678,height=370)

        #================ STUDENT ID ===============#
        studentID_label=Label(personal_info_frame,text="Student ID",font=('times new roman',12,'bold'),bg="white")
        studentID_label.grid(row=0,column=0,padx=3,pady=10)

        studentID_label=ttk.Entry(personal_info_frame,textvariable=self.var_student_id,width=30)
        studentID_label.grid(row=0,column=1)

        #================ STUDENT NAME ===============#
        studentName_label=Label(personal_info_frame,text="Student Name",font=('times new roman',12,'bold'),bg="white")
        studentName_label.grid(row=0,column=2,padx=8,pady=10)

        studentName_label=ttk.Entry(personal_info_frame,textvariable=self.var_studentName,width=30)
        studentName_label.grid(row=0,column=3)


        #================ GENDER ===============#
        student_gender_label=Label(personal_info_frame,text="Gender",font=('times new roman',12,'bold'),bg="white")
        student_gender_label.grid(row=1,column=0,padx=0,pady=10)

        student_gender_combo=ttk.Combobox(personal_info_frame,textvariable=self.var_gender,font=('times new roman',12,'bold'),width=20,state="read only")
        student_gender_combo["values"]=(
            "Select Gender",
            "Male",
            "Female",
        )
        student_gender_combo.current(0)
        student_gender_combo.grid(row=1,column=1,padx=0,pady=10,sticky=W)


        #================ STUDENT DOB ===============#
        studentDOB_label=Label(personal_info_frame,text="DOB",font=('times new roman',12,'bold'),bg="white")
        studentDOB_label.grid(row=1,column=2,padx=8,pady=10)

        studentDOB_label=ttk.Entry(personal_info_frame,textvariable=self.var_dob,width=30)
        studentDOB_label.grid(row=1,column=3)


        #================ STUDENT EMAIL ===============#
        studentEmail_label=Label(personal_info_frame,text="Email",font=('times new roman',12,'bold'),bg="white")
        studentEmail_label.grid(row=2,column=0,padx=8,pady=10)

        studentEmail_label=ttk.Entry(personal_info_frame,textvariable=self.var_email,width=30)
        studentEmail_label.grid(row=2,column=1)

        #================ STUDENT PHONE ===============#
        studentPhoneNo_label=Label(personal_info_frame,text="Phone No",font=('times new roman',12,'bold'),bg="white")
        studentPhoneNo_label.grid(row=2,column=2,padx=8,pady=10)

        studentPhoneNo_label=ttk.Entry(personal_info_frame,textvariable=self.var_phone1,width=30)
        studentPhoneNo_label.grid(row=2,column=3)

        #================ STUDENT ADDRESS ===============#
        studentAddress_label=Label(personal_info_frame,text="Address",font=('times new roman',12,'bold'),bg="white")
        studentAddress_label.grid(row=3,column=0,padx=8,pady=10)

        studentAddress_label=ttk.Entry(personal_info_frame,textvariable=self.var_address,width=30)
        studentAddress_label.grid(row=3,column=1)

        #================ STUDENT PHONE 2 ===============#
        studentPhone2_label=Label(personal_info_frame,text="Phone No",font=('times new roman',12,'bold'),bg="white")
        studentPhone2_label.grid(row=3,column=2,padx=8,pady=10)

        studentPhone2_label=ttk.Entry(personal_info_frame,textvariable=self.var_phone2,width=30)
        studentPhone2_label.grid(row=3,column=3)


        #================ RADIO BUTTONS ===============#
        #self.var_radio2=StringVar()

        student_sample_photo_option=ttk.Radiobutton(personal_info_frame,variable=self.var_radio1,text="Capture Sample Photo",value="Yes")
        student_sample_photo_option.grid(row=4,column=0,padx=15,pady=20)

        student_skip_photo_option=ttk.Radiobutton(personal_info_frame,variable=self.var_radio1,text="Skip Photo",value="No")
        student_skip_photo_option.grid(row=4,column=1,padx=15,pady=20)

        #================ ACTION BUTTONS ===============#
        action_buttons_frame=Frame(personal_info_frame,bd=2,relief="ridge",bg="white")
        action_buttons_frame.place(x=5,y=230,width=660,height=50)
        
        #================ SAVE BUTTON ===============#
        save_button=Button(action_buttons_frame,text="SAVE",command=self.add_student,font=('times new roman',12,'bold'),bg="blue",fg="white",width=16)
        save_button.grid(row=0,column=0,padx=5,pady=5)

        #================ UPDATE BUTTON ===============#
        update_button=Button(action_buttons_frame,text="UPDATE",command=self.update_data,font=('times new roman',12,'bold'),bg="blue",fg="white",width=16)
        update_button.grid(row=0,column=1,padx=5,pady=5)

        #================ DELETE BUTTON ===============#
        delete_button=Button(action_buttons_frame,text="DELETE",command=self.delete_data,font=('times new roman',12,'bold'),bg="blue",fg="white",width=16)
        delete_button.grid(row=0,column=2,padx=5,pady=5)

        #================ RESET BUTTON ===============#
        reset_button=Button(action_buttons_frame,text="RESET",command=self.clear_data,font=('times new roman',12,'bold'),bg="blue",fg="white",width=16)
        reset_button.grid(row=0,column=3,padx=5,pady=5)


        #================ ACTION BUTTONS ===============#
        sample_phot_buttons_frame=Frame(personal_info_frame,bd=2,relief="ridge",bg="white")
        sample_phot_buttons_frame.place(x=5,y=280,width=660,height=50)

        #================ ADD PHOTO SAMPLE BUTTON ===============#
        add_sample_button=Button(sample_phot_buttons_frame,command=self.generate_dataset,text="ADD PHOTO SAMPLE",font=('times new roman',12,'bold'),bg="blue",fg="white",width=34)
        add_sample_button.grid(row=1,column=0,padx=5,pady=5)

        #================ UPDATE PHOTO SAMPLE BUTTON ===============#
        update_sample_button=Button(sample_phot_buttons_frame,text="UPDATE PHOTO SAMPLE",font=('times new roman',12,'bold'),bg="blue",fg="white",width=34)
        update_sample_button.grid(row=1,column=1,padx=5,pady=5)


        #======================================= RIGHT FRAME ===================================#
        right_frame=LabelFrame(main_frame,bd=2,text="STUDENT INFORMATION",font=('times new roman',12,'bold'),bg="white",fg="black",relief="ridge")
        right_frame.place(x=720,y=10,width=1165,height=950)


        #================ STUDENT VIEW ===============#
        student_info_frame=LabelFrame(right_frame,bd=2,text="STUDENT VIEW AND SEARCH DETAIL",font=('times new roman',9,'bold'),bg="white",fg="black",relief="ridge")
        student_info_frame.place(x=5,y=15,width=1150,height=900)

        search_frame=LabelFrame(right_frame,bd=2,text="SEARCH FORM",font=('times new roman',8,'bold'),bg="white",fg="black",relief="ridge")
        search_frame.place(x=15,y=45,width=1130,height=65)

        #================ SEARCH FILTER ===============#
        search_label=Label(search_frame,text="Search Filter:",font=('times new roman',16,'bold'),bg="white",fg="black")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        # student_gender_label=Label(search_frame,text="Search",font=('times new roman',12,'bold'),bg="white")
        # student_gender_label.grid(row=0,column=1,padx=10,pady=5)

        search_combo=ttk.Combobox(search_frame,font=('times new roman',11,'bold'),width=20,state="read only")
        search_combo["values"]=(
            "Select Option",
            "Gender",
            "Name",
            "student_id",
            "Phone",
        )
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        search_label=ttk.Entry(search_frame,width=40)
        search_label.grid(row=0,column=2)


        #================ SEARCH BUTTONS ===============#
        search_button=Button(search_frame,text="SEARCH",font=('times new roman',12,'bold'),bg="blue",fg="white",width=27)
        search_button.grid(row=0,column=3,padx=5,pady=5)

        search_all_button=Button(search_frame,text="SEARCH ALL",font=('times new roman',12,'bold'),bg="blue",fg="white",width=27)
        search_all_button.grid(row=0,column=4,padx=5,pady=5)


        #======================== TABLE DISPLAY RESULT ===================#
        table_frame=Frame(right_frame,bd=2,relief="ridge")
        table_frame.place(x=15,y=130,width=1130,height=770)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dept","Course","Campus","Duration","student_id","Student_Name","Gender","DOB","Email","Phone_1","Phone_2","Address","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Dept',text="Department")
        self.student_table.heading('Course',text="Course")
        self.student_table.heading('Campus',text="Campus")
        self.student_table.heading('Duration',text="Duration")
        self.student_table.heading('student_id',text="ID")
        self.student_table.heading('Student_Name',text="Student Name")
        self.student_table.heading('Gender',text="Gender")
        self.student_table.heading('DOB',text="DOB")
        self.student_table.heading('Email',text="Email")
        self.student_table.heading('Phone_1',text="Primary Phone")
        self.student_table.heading('Phone_2',text="Alternate Phone")
        self.student_table.heading('Address',text="Address")
        self.student_table.heading('Photo',text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column('Dept',width=180)
        self.student_table.column('Course',width=180)
        self.student_table.column('Campus',width=180)
        self.student_table.column('Duration',width=100)
        self.student_table.column('student_id',width=80)
        self.student_table.column('Student_Name',width=180)
        self.student_table.column('Gender',width=100)
        self.student_table.column('DOB',width=100)
        self.student_table.column('Email',width=100)
        self.student_table.column('Phone_1',width=100)
        self.student_table.column('Phone_2',width=100)
        self.student_table.column('Address',width=180)
        self.student_table.column('Photo',width=180)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
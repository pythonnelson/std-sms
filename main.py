from tkinter import *
from tkinter import ttk
import tkinter
from tokenize import String
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help
from face_recognition import FaceRecognition



class Student_Face_Recognition_System:
    #======================== FUNCTION FOR CALLING THE STUDENTS LIST =======================================#
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
    
    def open_images(self):
        os.startfile("data")

    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Student Attendance Management System","Are you sure you want to exit now?")
        if self.iExit>0:
            self.root.destroy()
        else:
            return
        
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")

        ######################## BACKGROUND IMAGE ################################
        bg_img=Image.open(r"images\bg.webp")
        bg_img=bg_img.resize((1920,1080),Image.Resampling.LANCZOS)
        self.bg_image=ImageTk.PhotoImage(bg_img)

        bg_img=Label(self.root,image=self.bg_image)
        bg_img.place(x=0,y=0,width=1940,height=1080)


        ######################## Project Title label ################################
        title_label=Label(bg_img, text="STUDENT ATTENDANCE SYSTEM WITH FACE RECOGNITION",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=45)


        #================================================ BUTTONS ===================================================#

        ######################## Students Button Section ################################
        std_img_btn=Image.open(r"images\student.png")
        std_img_btn=std_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.std_photo_btn=ImageTk.PhotoImage(std_img_btn)

        std_btn=Button(bg_img,image=self.std_photo_btn,command=self.student_details,cursor="hand2")
        std_btn.place(x=500,y=100,width=150,height=150)

        std_btn_label=Button(bg_img,text="View Students",command=self.student_details,cursor="hand2",font=('times new roman',15,'bold'),bg="white",fg="black")
        std_btn_label.place(x=500,y=210,width=150,height=40)



        ######################## Face Detection Button Section ################################
        face_img_btn=Image.open(r"images\face_recognition.gif")
        face_img_btn=face_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.face_photo_btn=ImageTk.PhotoImage(face_img_btn)

        face_btn=Button(bg_img,image=self.face_photo_btn,cursor="hand2",command=self.face_recognition)
        face_btn.place(x=700,y=100,width=150,height=150)

        face_btn_label=Button(bg_img,text="Detect Face",cursor="hand2",command=self.face_recognition,font=('times new roman',15,'bold'),bg="white",fg="black")
        face_btn_label.place(x=700,y=210,width=150,height=40)



        ######################## Attendance Detection Button Section ################################
        attendance_img_btn=Image.open(r"images\attendance.png")
        attendance_img_btn=attendance_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.attendance_photo_btn=ImageTk.PhotoImage(attendance_img_btn)

        attendance_btn=Button(bg_img,image=self.attendance_photo_btn,cursor="hand2",command=self.attendance)
        attendance_btn.place(x=900,y=100,width=150,height=150)

        attendance_btn_label=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance,font=('times new roman',15,'bold'),bg="white",fg="black")
        attendance_btn_label.place(x=900,y=210,width=150,height=40)



        ######################## Help Desk Button Section ################################
        help_img_btn=Image.open(r"images\help.png")
        help_img_btn=help_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.help_photo_btn=ImageTk.PhotoImage(help_img_btn)

        help_btn=Button(bg_img,image=self.help_photo_btn,cursor="hand2",command=self.help)
        help_btn.place(x=1100,y=100,width=150,height=150)

        help_btn_label=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=('times new roman',15,'bold'),bg="white",fg="black")
        help_btn_label.place(x=1100,y=210,width=150,height=40)


        ######################## Train Model Button Section ################################
        train_model_img_btn=Image.open(r"images\train_model.png")
        train_model_img_btn=train_model_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.train_model_photo_btn=ImageTk.PhotoImage(train_model_img_btn)

        train_model_btn=Button(bg_img,image=self.train_model_photo_btn,cursor="hand2",command=self.train_data)
        train_model_btn.place(x=500,y=300,width=150,height=150)

        train_model_btn_label=Button(bg_img,text="Train Model",cursor="hand2",command=self.train_data,font=('times new roman',15,'bold'),bg="white",fg="black")
        train_model_btn_label.place(x=500,y=410,width=150,height=40)

        
        ######################## Photos Button Section ################################
        photos_img_btn=Image.open(r"images\photos.png")
        photos_img_btn=photos_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.photos_photo_btn=ImageTk.PhotoImage(photos_img_btn)

        photos_btn=Button(bg_img,image=self.photos_photo_btn,cursor="hand2",command=self.open_images,)
        photos_btn.place(x=700,y=300,width=150,height=150)

        photos_btn_label=Button(bg_img,text="Models",cursor="hand2",command=self.open_images,font=('times new roman',15,'bold'),bg="white",fg="black")
        photos_btn_label.place(x=700,y=410,width=150,height=40)



        ######################## Developer Button Section ################################
        developer_img_btn=Image.open(r"images\developer.png")
        developer_img_btn=developer_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.developer_photo_btn=ImageTk.PhotoImage(developer_img_btn)

        developer_btn=Button(bg_img,image=self.developer_photo_btn,cursor="hand2",command=self.developer)
        developer_btn.place(x=900,y=300,width=150,height=150)

        developer_btn_label=Button(bg_img,text="Developer",cursor="hand2",command=self.developer,font=('times new roman',15,'bold'),bg="white",fg="black")
        developer_btn_label.place(x=900,y=410,width=150,height=40)



        ######################## Exit Button Section ################################
        exit_img_btn=Image.open(r"images\exit.png")
        developer_img_btn=exit_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.exit_photo_btn=ImageTk.PhotoImage(exit_img_btn)

        exit_btn=Button(bg_img,image=self.exit_photo_btn,cursor="hand2",command=self.iExit)
        exit_btn.place(x=1100,y=300,width=150,height=150)

        exit_btn_label=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=('times new roman',15,'bold'),bg="white",fg="black")
        exit_btn_label.place(x=1100,y=410,width=150,height=40)


if __name__ == "__main__":
    root=Tk()
    obj=Student_Face_Recognition_System(root)
    root.mainloop()
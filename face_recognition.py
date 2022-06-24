from cgitb import text
from email import message
from importlib.resources import path
from multiprocessing import connection
from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import cvtColor, putText
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from train import *


class FaceRecognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")


        ######################## Project Title label ################################
        title_label=Label(self.root,text="STUDENT ATTENDANCE SYSTEM FACE DETECTION",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=50)

        top_image=Image.open(r"images\face_recognition.jpg")
        top_image=top_image.resize((1920,1000),Image.Resampling.LANCZOS)
        self.top_photo_image=ImageTk.PhotoImage(top_image)

        top_image_label=Label(self.root,image=self.top_photo_image)
        top_image_label.place(x=0,y=55,width=1920,height=1000)


        train_data_btn_label=Button(top_image_label,text="FACE RECOGNITION", command=self.face_recog, cursor="hand2",font=('times new roman',20,'bold'),bg="white",fg="black")
        train_data_btn_label.place(x=800,y=410,width=300,height=60)

    #====================================== ATTENDANCE SYSTEM =====================
    def mark_attendance(self,i,n,d,c):
        with open("attendance.csv","r+",newline="\n") as f:
            my_dataList=f.readlines()
            name_list=[]
            for line in my_dataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((i not in name_list) and (n not in name_list) and (d not in name_list) and (c not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{c},{dtString},{d1},Present")  

    #====================================== FACE RECOGNITION =====================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300))) # Calculate the predicted gray_image
                
                #===================== CONNECT TO DATABASE =============================
                conn=mysql.connector.connect(host='localhost',username="root",password="yourdatabasepassword",database="sms_face_recog")
                my_cursor=conn.cursor()

                my_cursor.execute("select student_id from student where student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                my_cursor.execute("select student_name from student where student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Dept from student where student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select course from student where student_id="+str(id))
                c=my_cursor.fetchone()
                c="+".join(c)


                if confidence>77:
                    cv2.putText(img,f"Student ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Student Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Course:{c}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,n,d,c)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Student Attendance System Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=FaceRecognition(root)
    root.mainloop()
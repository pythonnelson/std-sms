from cgitb import text
from email import message
from importlib.resources import path
from multiprocessing import connection
from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import cvtColor
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")


        ######################## Project Title label ################################
        title_label=Label(self.root,text="STUDENT ATTENDANCE SYSTEM TRAIN DATASET",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=50)

        train_data_btn_label=Button(self.root,text="TRAIN DATA", command=self.train_classifier,cursor="hand2",font=('times new roman',20,'bold'),bg="white",fg="black")
        train_data_btn_label.place(x=800,y=410,width=200,height=40)

    
    #===================================== TRAIN DATASET FUNCTION ================================
    def train_classifier(self):
        data_dir=("data")
        path=[ os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Did a grayscale image convertion here
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("System is Training, Please Wait..",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #================================ TRAIN THE CLASSIFIER AND SAVE THE DATA ===============================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Training Success","System Training successfully completed.")


if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
from cgitb import text
from email import message
from multiprocessing import connection
from tkinter import *
from tkinter import ttk
from turtle import title, update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import cvtColor
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")

        ######################## Project Title label ################################
        title_label=Label(self.root,text="ABOUT THE DEVELOPER",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=50)

        right_frame=Frame(self.root,bd=2,bg="white")
        right_frame.place(x=1200,y=100,width=700,height=700)

        developer_label=Label(right_frame,text="Alpha Umaru Jalloh",font=('times new roman',55,'bold'),bg="white")
        developer_label.grid(row=0,column=0,padx=3,pady=10)

        developer_label=Label(right_frame,text="Email: aujalloh97@gmail.com",font=('times new roman',30,'bold'),bg="white")
        developer_label.grid(row=1,column=0,padx=3,pady=10)






if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
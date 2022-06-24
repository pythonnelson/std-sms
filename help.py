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


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")

        ######################## Project Title label ################################
        title_label=Label(self.root,text="OUR HELP DESK",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=50)

        right_frame=Frame(self.root,bd=2,bg="white")
        right_frame.place(x=0,y=100,width=1920,height=150)

        developer_label=Label(right_frame,text="For Tech Support, Contact",font=('times new roman',40,'bold'),bg="white")
        developer_label.place(x=550,y=10)

        developer_label=Label(right_frame,text="Email: aujalloh97@gmail.com",font=('times new roman',20,'bold'),bg="white")
        developer_label.place(x=650,y=90)






if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
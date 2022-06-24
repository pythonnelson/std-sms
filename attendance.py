from email import message
from mimetypes import init
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


myData=[]
class Attendance:
    
    #======================== Fetch Attendance Data ==========================
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    #========== Import csv =============   
    def import_csv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)

        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    #========== Export csv =============
    def export_csv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","Sorry, No Data Found To Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                export_write=csv.writer(myfile,delimiter=",")
            for i in myData:
                export_write.writerow(i)
            messagebox.showinfo("Export Data","Data Exported successfully to " +os.path.basename(fln))
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    
    #================================== Get Cursor Focus =============================
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content["values"]

        self.var_student_atten_id.set(rows[0]),
        self.var_student_atten_name.set(rows[1]),
        self.var_student_atten_dept.set(rows[2]),
        self.var_student_atten_course.set(rows[3]),
        self.var_student_atten_date.set(rows[4]),
        self.var_student_atten_time.set(rows[5]),
        self.var_student_atten_attendance.set(rows[6]),
    
    def reset_data(self):
        self.var_student_atten_id.set("")
        self.var_student_atten_name.set("")
        self.var_student_atten_dept.set("")
        self.var_student_atten_course.set("")
        self.var_student_atten_date.set("")
        self.var_student_atten_time.set("")
        self.var_student_atten_attendance.set("Select Attendance")


    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Attendance with Face Recognition System")

         #==================== VARIABLES ===================
        self.var_student_atten_id=StringVar()
        self.var_student_atten_name=StringVar()
        self.var_student_atten_dept=StringVar()
        self.var_student_atten_course=StringVar()
        self.var_student_atten_date=StringVar()
        self.var_student_atten_time=StringVar()
        self.var_student_atten_attendance=StringVar()

        ######################## Project Title label ################################
        title_label=Label(self.root,text="STUDENT ATTENDANCE",font=('times new roman',35,'bold'),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1920,height=50)

        #======================================= MAIN FRAME ===================================#
        main_frame=Frame(self.root,bd=3)
        main_frame.place(x=0,y=75,width=1920,height=1030)

        #======================================= LEFT FRAME ===================================#
        left_frame=LabelFrame(main_frame,bd=2,text="STUDENT ATTENDANCE",font=('times new roman',12,'bold'),bg="white",fg="black",relief="ridge")
        left_frame.place(x=0,y=10,width=700,height=900)

        #======================================= LEFT INFO FRAME ===================================#
        left_info_frame=Frame(left_frame,bd=2,relief="ridge",bg="white")
        left_info_frame.place(x=5,y=15,width=680,height=200)

        #================ STUDENT ID ===============#
        studentID_label=Label(left_info_frame,text="Student ID",font=('times new roman',12,'bold'),bg="white")
        studentID_label.grid(row=0,column=0,padx=3,pady=10)

        studentID_label=ttk.Entry(left_info_frame,width=30,textvariable=self.var_student_atten_id)
        studentID_label.grid(row=0,column=1)

        #================ NAME ===============#
        studentName_label=Label(left_info_frame,text="Student Name",font=('times new roman',12,'bold'),bg="white")
        studentName_label.grid(row=0,column=2,padx=3,pady=10)

        studentName_label=ttk.Entry(left_info_frame,width=30,textvariable=self.var_student_atten_name)
        studentName_label.grid(row=0,column=3)

        #================ DEPARTMENT ===============#
        department_label=Label(left_info_frame,text="Department",font=('times new roman',12,'bold'),bg="white")
        department_label.grid(row=1,column=0,padx=3,pady=10)

        department_label=ttk.Entry(left_info_frame,width=30,textvariable=self.var_student_atten_dept)
        department_label.grid(row=1,column=1)


        #================= ATTENDANCE STATUS ====================#
        attendance_status_label=Label(left_info_frame,text="Attendance Status",font=('times new roman',12,'bold'),bg="white")
        attendance_status_label.grid(row=1,column=2,padx=0,pady=10)

        attendance_status_combo=ttk.Combobox(left_info_frame,textvariable=self.var_student_atten_attendance,font=('times new roman',12,'bold'),width=23,state="read only")
        attendance_status_combo["values"]=(
            "Attendance Status",
            "Present",
            "Absent",
        )
        attendance_status_combo.current(0)
        attendance_status_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)

        #================ DATE ===============#
        date_label=Label(left_info_frame,text="Date",font=('times new roman',12,'bold'),bg="white")
        date_label.grid(row=2,column=0,padx=3,pady=10)

        date_label=ttk.Entry(left_info_frame,width=30,textvariable=self.var_student_atten_date)
        date_label.grid(row=2,column=1)

        #================ TIME ===============#
        time_label=Label(left_info_frame,text="Time",font=('times new roman',12,'bold'),bg="white")
        time_label.grid(row=2,column=2,padx=3,pady=10)

        time_label=ttk.Entry(left_info_frame,width=30,textvariable=self.var_student_atten_time)
        time_label.grid(row=2,column=3)


        #================ IMPORT BUTTON ===============#
        import_button=Button(left_info_frame,text="Import CSV",command=self.import_csv,font=('times new roman',12,'bold'),bg="blue",fg="white",width=13)
        import_button.grid(row=3,column=0,padx=5,pady=5)

        #================ EXPORT BUTTON ===============#
        export_button=Button(left_info_frame,text="Export CSV",command=self.export_csv,font=('times new roman',12,'bold'),bg="blue",fg="white",width=13)
        export_button.grid(row=3,column=1,padx=5,pady=5)

        #================ UPDATE BUTTON ===============#
        update_button=Button(left_info_frame,text="Update",font=('times new roman',12,'bold'),bg="blue",fg="white",width=13)
        update_button.grid(row=3,column=2,padx=5,pady=5)

        #================ RESET BUTTON ===============#
        reset_button=Button(left_info_frame,text="RESET",command=self.reset_data,font=('times new roman',12,'bold'),bg="blue",fg="white",width=13)
        reset_button.grid(row=3,column=3,padx=5,pady=5)



        #======================================= RIGHT FRAME ===================================#
        right_frame=LabelFrame(main_frame,bd=2,text="ATTENDANCE INFORMATION",font=('times new roman',12,'bold'),bg="white",fg="black",relief="ridge")
        right_frame.place(x=720,y=10,width=1165,height=900)

        #======================================= RIGHT INSIDE TABLE FRAME ===================================#
        table_frame=Frame(right_frame,bd=2,bg="white",relief="ridge")
        table_frame.place(x=5,y=15,width=1150,height=850)

        #======================================= SCROLL BAR ===================================#
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","name","department","course","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading('id',text="Student ID")
        self.AttendanceReportTable.heading('name',text="Student Name")
        self.AttendanceReportTable.heading('department',text="Department")
        self.AttendanceReportTable.heading('course',text="Course")
        self.AttendanceReportTable.heading('date',text="Date")
        self.AttendanceReportTable.heading('time',text="Time")
        self.AttendanceReportTable.heading('attendance',text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column('id',width=80)
        self.AttendanceReportTable.column('name',width=200)
        self.AttendanceReportTable.column('department',width=200)
        self.AttendanceReportTable.column('course',width=200)
        self.AttendanceReportTable.column('date',width=180)
        self.AttendanceReportTable.column('time',width=180)
        self.AttendanceReportTable.column('attendance',width=180)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
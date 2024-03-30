from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")
        
        #============== Variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
        
        # First Image
        img1=Image.open(r"college_images\smart-attendance.jpg")
        img1=img1.resize((700,200))
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=680,height=200)
        
        # Second Image
        img=Image.open(r"college_images\cllg.jpg")
        img=img.resize((700,200))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=680,y=0,width=680,height=200)
        
        # background Image
        img4=Image.open(r"college_images\bgimg.jpg")
        img4=img4.resize((1350,700))
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1350,height=700)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1350,height=40)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1320,height=500)
        
        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=660,height=480)
        
        img_left=Image.open(r"college_images\face-recognition.png")
        img_left=img_left.resize((650,100))
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=100)
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=105,width=630,height=480)
        
        # labels and entries
        # attendance id
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("comicsansns",10,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("comicsansns",10,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Roll 
        rollLabel=Label(left_inside_frame,text="Roll:",font=("comicsansns",10,"bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=4,pady=8)
        
        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("comicsansns",10,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)
        
        # Name
        nameLabel=Label(left_inside_frame,text="Name:",font=("comicsansns",10,"bold"),bg="white")
        nameLabel.grid(row=1,column=0)
        
        atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("comicsansns",10,"bold"))
        atten_name.grid(row=1,column=1,pady=8)
        
        # Department
        depLabel=Label(left_inside_frame,text="Department:",font=("comicsansns",10,"bold"),bg="white")
        depLabel.grid(row=1,column=2)
        
        atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("comicsansns",10,"bold"))
        atten_dep.grid(row=1,column=3,pady=8)
        
        # Time
        timeLabel=Label(left_inside_frame,text="Time:",font=("comicsansns",10,"bold"),bg="white")
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("comicsansns",10,"bold"))
        atten_time.grid(row=2,column=1,pady=8)
        
        # Date
        dateLabel=Label(left_inside_frame,text="Date:",font=("comicsansns",10,"bold"),bg="white")
        dateLabel.grid(row=2,column=2)
        
        atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("comicsansns",10,"bold"))
        atten_date.grid(row=2,column=3,pady=8)
        
        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font=("comicsansns",10,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0)
        
        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)
        
        #buttons Frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=645,height=25)
        
        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=22,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",width=22,command=self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
        # Right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=630,height=480)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=615,height=380)
        
        # ==================== scroll bar table==============
        
        scroll_x =ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y =ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # ============ fatch data ==============
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
     
    # import csv       
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])
        
    # Reset data  
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
            
    
        
        
        
        
        
        
        
        



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
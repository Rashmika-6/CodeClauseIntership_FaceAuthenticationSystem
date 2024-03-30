from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1350,height=40)
        
        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1350,620))
        self.photoimg_top=ImageTk.PhotoImage(img_top)
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=1350,height=620)
        
        # frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=430,height=500)
        
        img_top1=Image.open(r"college_images\Rashmiphoto.jpg")
        img_top1=img_top1.resize((180,180))
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)
        
        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=250,y=0,width=180,height=180)
        
        # Developer Info
        dev_label=Label(main_frame,text="Hello!! My name is Rashmi",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)
        
        dev_label=Label(main_frame,text="I am MCA Student",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=40)
        
        
        img3=Image.open(r"college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img3=img3.resize((450,300))
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(main_frame,image=self.photoimg3)
        f_lbl.place(x=0,y=200,width=450,height=300)
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

class QrGenerator:
    def __init__(self,root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(False,False)
        
        title = Label(self.root, text="   Qr Code Generator", font=("times new roman",40),bg="#053246", fg="white", anchor='w').place(x=0, y=0, relwidth=1)
        
        # Student details window
        # Variable
        self.var_std_prn = StringVar()
        self.var_std_name = StringVar()
        self.var_std_emailID = StringVar()
        self.var_std_mob = StringVar()
        
        std_frame = Frame(self.root, bd=2,relief=RIDGE, bg='white')
        std_frame.place(x=50, y=100, width=500,height=380)
        
        std_title = Label(std_frame, text="Student Details", font=("goudy old style",20),bg="#043256", fg="white").place(x=0, y=0, relwidth=1)
        
        lbl_std_prn = Label(std_frame, text="Name :", font=("times new roman",15,"bold"),bg="white").place(x=50, y=60)
        lbl_name = Label(std_frame, text="PRN :", font=("times new roman",15,"bold"),bg="white").place(x=50, y=100)
        lbl_department = Label(std_frame, text="Email ID :", font=("times new roman",15,"bold"),bg="white").place(x=50, y=140)
        lbl_designation = Label(std_frame, text="Mobile No :", font=("times new roman",15,"bold"),bg="white").place(x=50, y=180)
        
        txt_std_prn = Entry(std_frame, textvariable=self.var_std_prn, font=("times new roman",15),bg="lightyellow").place(x=200, y=60)
        txt_name = Entry(std_frame, textvariable=self.var_std_name, font=("times new roman",15),bg="lightyellow").place(x=200, y=100)
        txt_department = Entry(std_frame, textvariable=self.var_std_emailID, font=("times new roman",15),bg="lightyellow").place(x=200, y=140)
        txt_designation = Entry(std_frame,  textvariable=self.var_std_mob, font=("times new roman",15),bg="lightyellow").place(x=200, y=180)
        
        btn_generator = Button(std_frame,text="QR Generate", command=self.generate, font=("times new roman",17,"bold"),bg="#2196f3", fg="white").place(x=90, y=250, width=170,height=30)
        btn_clear = Button(std_frame,text="Clear", command=self.clear, font=("times new roman",17,"bold"),bg="#607d8b", fg="white").place(x=282, y=250, width=120,height=30)
        
        self.msg = ""
        self.lbl_msg = Label(std_frame, text=self.msg, font=("goudy old style",20,"bold"),bg="white", fg="green")
        self.lbl_msg.place(x=0, y=310, relwidth=1)
        
        # Students QR prn window
        qr_frame = Frame(self.root, bd=2,relief=RIDGE, bg='white')
        qr_frame.place(x=600, y=100, width=250,height=380)
        
        std_title = Label(qr_frame, text="QR Code", font=("goudy old style",20),bg="#043256", fg="white").place(x=0, y=0, relwidth=1)
        
        self.qr_prn = Label(qr_frame,text="QR Code\nNot Available", font=("times new roman",15),bg="#3f51b5",fg="white", bd=1, relief=RIDGE)
        self.qr_prn.place(x=35, y=100, width=180, height=180)
        
    def generate(self):
        if self.var_std_mob.get()=="" or self.var_std_prn.get()=="" or self.var_std_emailID.get()=="" or self.var_std_name.get()=="":
            self.msg = "All Fields are Required!!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        else:
            qr_data = (f"Student Details\nName: {self.var_std_prn.get()}\nPRN: {self.var_std_name.get()}\nEmail ID: {self.var_std_emailID.get()}\nMobile No: {self.var_std_mob.get()}")
            qr_prn = qrcode.make(qr_data)
            # print(qr_prn)
            qr_prn = resizeimage.resize_cover(qr_prn,[180,180])
            qr_prn.save("QRs/Std_"+str(self.var_std_prn.get())+".png")
            # QR prn image update
            self.im = ImageTk.PhotoImage(file="QRs/Std_"+str(self.var_std_prn.get())+".png")
            self.qr_prn.config(image=self.im)
            # updating notafications
            self.msg = "QR Generated Successfully!!!"
            self.lbl_msg.config(text=self.msg,fg="green")
            
    def clear(self):
        self.var_std_prn.set("")
        self.var_std_name.set("")
        self.var_std_emailID.set("")
        self.var_std_mob.set("")
        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_prn.config(image='')
        
        
root = Tk()
obj = QrGenerator(root)
root.mainloop()

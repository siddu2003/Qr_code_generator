from tkinter import *
import qrcode
from PIL import Image,ImageTk


class qr_gen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1800+200+50")
        self.root.title("QR Generator | Developed By __")


        title = Label(self.root, text="  Qr Code Generator", font=("times new roman", 40), bg='#053246', fg='white',
                      anchor='w').place(x=0, y=0, relwidth=1)

        # ======DETAILS_frame====
        det_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        det_Frame.place(x=50, y=100, width=500, height=380)

        det_Frame = title = Label(det_Frame, text="Details", font=("goudy old style", 30), bg='#043256',
                                  fg='white', ).place(x=0, y=0, relwidth=1)

        # --text--
        # ---variables--
        self.var_name = StringVar()
        self.var_phnumber = StringVar()
        self.var_email = StringVar()
        self.var_linkedin = StringVar()
        lbl_det_name = title = Label(det_Frame, text="Name", font=("times new roman", 20, 'bold'), bg='white').place(x=60, y=170)
        lbl_det_phnumber = title = Label(det_Frame, text="Phonenumber", font=("times new roman", 20, 'bold'),bg='white').place(x=60, y=210)
        lbl_det_email = title = Label(det_Frame, text="Email", font=("times new roman", 20, 'bold'), bg='white').place(x=60, y=250)
        lbl_det_linkdin = title = Label(det_Frame, text="Linkedin", font=("times new roman", 20, 'bold'),bg='white').place(x=60, y=290)

        # ---text_input----in details

        txt_det_name = title = Entry(det_Frame, font=("times new roman", 15), textvariable=self.var_name,
                                     bg='lightblue',width=26).place(x=250, y=175)
        txt_det_phnumber = title = Entry(det_Frame, font=("times new roman", 15), textvariable=self.var_phnumber,
                                         bg='lightblue',width=26).place(x=250, y=215)
        txt_det_email = title = Entry(det_Frame, font=("times new roman", 15), textvariable=self.var_email,
                                      bg='lightblue',width=26).place(x=250, y=255)
        txt_det_linkdin = title = Entry(det_Frame, font=("times new roman", 15), textvariable=self.var_linkedin,
                                        bg='lightblue',width=26).place(x=250, y=295)

        # --button--

        btn_gen = Button(det_Frame, text='Clear', command=self.clear, font=("times new roman", 18, 'bold'),
                         bg='red', fg='white').place(x=230, y=350, width=75, height=35)
        btn_gen = Button(det_Frame, text='QR Generate', command=self.generate, font=("times new roman", 18, 'bold'),
                         bg='green', fg='white').place(x=350, y=350, width=180, height=35)

        self.msg = ''
        self.lbl_msg = Label(det_Frame, text=self.msg, font=("times new roman", 20), bg='white', fg='green')
        self.lbl_msg.place(x=147, y=410)

        # ======QR frame====
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=870, height=650)

        qr_Frame = title = Label(qr_Frame, text="QR Code", font=("goudy old style", 30), bg='#043256',
                                 fg='white', ).place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text='No Qr \n Available', font=('times new roman', 15), bg='white',
                             fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=600, y=155, width=870, height=630)

    def clear(self):
        self.var_name.set('')
        self.var_phnumber.set('')
        self.var_email.set('')
        self.var_linkedin.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_name.get()=='' or self.var_email.get()=='' or self.var_linkedin.get()=='' or self.var_phnumber.get()=='':
            self.msg='ALL FIELDS ARE REQUIRED!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data = (f"Name: {self.var_name.get()}\nPhone Number: {self.var_phnumber.get()}\nEmail:{self.var_email.get()}\nLinkedin: {self.var_linkedin.get()}")
            qr_code = qrcode.make(qr_data)

            qr_code.save("emp_QR/qr_" + str(self.var_name.get()) + '.png')
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            self.msg = 'QR Generated Successfully!!'
            self.lbl_msg.config(text=self.msg, fg='green')




root = Tk()
obj = qr_gen(root)
root.mainloop()

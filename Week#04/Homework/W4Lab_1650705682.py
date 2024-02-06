'''
Author  : Nuttanon Rungpiron
STD ID  : 1650705682
Week    : 4
Label   : Homework
Desc    : Lab 4
Date    : 2024-01-31
'''

'''
Hint!

1 สร้างหน้าต่างโปรแกรม พร้อมกำหนด grid rowconfigure, columnconfigure ให้เหมาะสม
2 ออกแบบโครงสร้างของหน้าจอด้วย Frame & Labelframe พร้อมกำหนด grid rowconfigure, columnconfigure ให้เหมาะสมกับแต่ละ Frame
3 วาง widget ตามแบบ
4 ประกาศตัวแปรประเภท Spy เพื่อช่วยผูกข้อมูลกับ widget
5 ผูก function กับ widget เพื่อคำนวณ และแสดงรายละเอียด
6 ใช้ messagebox สำหรับ confirm กับผู้ใช้

Keep Fighting!

'''

from tkinter import *
from tkinter import messagebox

COLOR_PINK = "lightpink"
COLOR_BLUE = "lightblue"
COLOR_GREEN = "lightgreen"

def mainwindow() :
    root = Tk()
    root.title("LAB4: My Sweety Cake Shop by Nuttanon Rungpiron")
    root.geometry("750x650")
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=4)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    return(root)

def CreateFrame(root) :
    fm_top = Frame(root, bg=COLOR_PINK)
    fm_top.grid_propagate(0)
    fm_top.rowconfigure(0, weight=1)
    fm_top.columnconfigure(0, weight=1)

    fm_left = LabelFrame(root, text="Cake Menu", bg=COLOR_BLUE)
    fm_left.rowconfigure((0,1,2,3,4,5,6), weight=1)
    fm_left.columnconfigure((0,1), weight=1)
    fm_left.grid_propagate(0)

    fm_right = LabelFrame(root, text="Product Summary", bg=COLOR_GREEN)
    fm_right.rowconfigure((0,1,2,3), weight=1)
    fm_right.rowconfigure(4, weight=3)
    fm_right.columnconfigure((0,1), weight=1)
    fm_right.grid_propagate(0)

    fm_bottom = Frame(root, bg=COLOR_PINK)
    fm_bottom.columnconfigure(0, weight=1)
    fm_bottom.rowconfigure(0, weight=1)
    fm_bottom.grid_propagate(0)

    fm_top.grid(row=0, columnspan=2, sticky="news")
    fm_left.grid(row=1, column=0, sticky="news")
    fm_right.grid(row=1, column=1, sticky="news")
    fm_bottom.grid(row=2, columnspan=2, sticky="news")
    return(root, fm_top, fm_left, fm_right, fm_bottom)

def CreateTopWidget(top) : 
    lbl_title = Label(top, text = "My Cake Shop", font="Tahoma 22 bold", bg=COLOR_PINK, fg="#FFFFFF")
    lbl_title.grid(row=0, column=0, sticky=NSEW, ipadx=10, ipady=10)

def CreateLeftWidget(left) : 
    img_cake1 = Label(left, bg=COLOR_BLUE, image=IMG_CAKE1)
    img_cake2 = Label(left, bg=COLOR_BLUE, image=IMG_CAKE2)
    img_cake3 = Label(left, bg=COLOR_BLUE, image=IMG_CAKE3)
    lbl_cake1 = Label(left, bg=COLOR_BLUE, text="Product 1 : Wow 1\nPrice 180 THB")
    lbl_cake2 = Label(left, bg=COLOR_BLUE, text="Product 2 : Wow 2\nPrice 250 THB")
    lbl_cake3 = Label(left, bg=COLOR_BLUE, text="Product 3 : Wow 3\nPrice 380 THB")
    ipt_cake1 = Spinbox(left, justify="center", from_=0, to=1000)
    ipt_cake2 = Spinbox(left, justify="center", from_=0, to=1000)
    ipt_cake3 = Spinbox(left, justify="center", from_=0, to=1000)

    btn_checkout = Button(left, text="Checkout", image=IMG_CHECKOUT, compound=LEFT, command=lambda: CalculateSummary(ipt_cake1, ipt_cake2, ipt_cake3))

    img_cake1.grid(row=0, column=0, rowspan=2)
    img_cake2.grid(row=2, column=0, rowspan=2)
    img_cake3.grid(row=4, column=0, rowspan=2)
    lbl_cake1.grid(row=0, column=1, sticky="s")
    lbl_cake2.grid(row=2, column=1, sticky="s")
    lbl_cake3.grid(row=4, column=1, sticky="s")
    ipt_cake1.grid(row=1, column=1, sticky="n")
    ipt_cake2.grid(row=3, column=1, sticky="n")
    ipt_cake3.grid(row=5, column=1, sticky="n")

    btn_checkout.grid(row=6, columnspan=2, sticky="NSEW")

def CreateRightWidget(right) :
    lbl_cake1 = Label(right, bg=COLOR_GREEN, text="Product 1 : Wow 1\nPrice 180 THB")
    lbl_cake2 = Label(right, bg=COLOR_GREEN, text="Product 2 : Wow 2\nPrice 250 THB")
    lbl_cake3 = Label(right, bg=COLOR_GREEN, text="Product 3 : Wow 3\nPrice 380 THB")
    lbl_total = Label(right, bg=COLOR_GREEN, text="Total Price :")

    sum_cake1 = Entry(right, textvariable=spy_cake1, justify="center")
    sum_cake2 = Entry(right, textvariable=spy_cake2, justify="center")
    sum_cake3 = Entry(right, textvariable=spy_cake3, justify="center")
    sum_total = Entry(right, textvariable=spy_total, justify="center")

    lbl_cake1.grid(row=0, column=0)
    lbl_cake2.grid(row=1, column=0)
    lbl_cake3.grid(row=2, column=0)
    lbl_total.grid(row=3, column=0)
    sum_cake1.grid(row=0, column=1)
    sum_cake2.grid(row=1, column=1)
    sum_cake3.grid(row=2, column=1)
    sum_total.grid(row=3, column=1)

def CreateBottomWidget(bottom) : 
    btn_exit = Button(bottom, text="Exit Program", command=ExitProgram, image=IMG_EXIT, compound=LEFT, width=130, height=40)
    btn_exit.grid(column=0, row=0, padx=10, sticky="e")

def CalculateSummary(ipt_cake1, ipt_cake2, ipt_cake3):
    spy_cake1.set("{:.2f}".format(int(ipt_cake1.get()) * 180))
    spy_cake2.set("{:.2f}".format(int(ipt_cake2.get()) * 250))
    spy_cake3.set("{:.2f}".format(int(ipt_cake3.get()) * 380))
    spy_total.set("{:.2f}".format(float(spy_cake1.get()) + float(spy_cake2.get()) + float(spy_cake3.get())))

def ExitProgram() :
    if messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?"):
        root.quit()



root = mainwindow()
root, fm_top, fm_left, fm_right, fm_bottom = CreateFrame(root)

IMG_CAKE1 = PhotoImage(file = "images\cake_1.png").subsample(2,2)
IMG_CAKE2 = PhotoImage(file = "images\cake_2.png").subsample(2,2)
IMG_CAKE3 = PhotoImage(file = "images\cake_3.png").subsample(2,2)
IMG_CHECKOUT = PhotoImage(file = "images\cart.png").subsample(2,2)
IMG_EXIT = PhotoImage(file = "images\exit.png").subsample(2,2)

spy_cake1 = IntVar()
spy_cake2 = IntVar()
spy_cake3 = IntVar()
spy_total = IntVar()

CreateTopWidget(fm_top)
CreateLeftWidget(fm_left)
CreateRightWidget(fm_right)
CreateBottomWidget(fm_bottom)
root.mainloop()
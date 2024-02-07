'''
Author  : Nuttanon Rungpiron
STD ID  : 1650705682
Week    : 5
Label   : Homework 5
Desc    : To create a creativity calculator by using Lambda Function and Eval()
Date    : 2024-02-07
'''


'''
Hint!
1. สร้างหน้าต่างโปรแกรม และปรับแต่งให้เหมาะสม
2. สร้าง Widgets เพื่อเป็นส่วนประกอบของเครื่องคิดเลข เช่น ส่วนแสดงผล (Label), และแป้นกด (Button) เป็นต้น
3. ใช้ตัวแปร Spy เป็นตัวกลางระหว่าง Code และ Widget
4. ใช้ Lambda Function ในการเรียกใช้ฟังก์ชัน
5. ใช้ Eval เพื่อประมวลผลนิพจน์ทางคณิตศาสตร์

Keep Fighting!

'''

from tkinter import *

def mainWindow() :
    root = Tk()
    root.title("My Calculator by Nuttanon Rungpiron")
    root.geometry("400x500")
    root.rowconfigure(0, weight=2)
    root.rowconfigure((1,2,3,4,5), weight=1)
    root.columnconfigure((0,1,2,3), weight=1)
    return(root)

def CreateWidgets(root) :
    Label(root, bg="orange", justify="center", textvariable=spy_display, font=("Helvetica", "40", "bold")).grid(row=0, column=0, columnspan=4, sticky="NEWS")

    Button(root, text="AC", bg="lightpink", font=("Helvetica", "12", "bold"), command=onClickAllClear).grid(row=1, column=0, sticky="NEWS")
    Button(root, text="Clear", bg="lightpink", font=("Helvetica", "12", "bold"), command=onClickClear).grid(row=1, column=1, sticky="NEWS")
    Button(root, text="%", font=("Helvetica", "12", "bold"), command=lambda:onClick("%")).grid(row=1, column=2, sticky="NEWS")
    Button(root, text="÷", font=("Helvetica", "12", "bold"), command=lambda:onClick("÷")).grid(row=1, column=3, sticky="NEWS")

    Button(root, text="7", font=("Helvetica", "12", "bold"), command=lambda:onClick("7")).grid(row=2, column=0, sticky="NEWS")
    Button(root, text="8", font=("Helvetica", "12", "bold"), command=lambda:onClick("8")).grid(row=2, column=1, sticky="NEWS")
    Button(root, text="9", font=("Helvetica", "12", "bold"), command=lambda:onClick("9")).grid(row=2, column=2, sticky="NEWS")
    Button(root, text="x", font=("Helvetica", "12", "bold"), command=lambda:onClick("x")).grid(row=2, column=3, sticky="NEWS")

    Button(root, text="4", font=("Helvetica", "12", "bold"), command=lambda:onClick("4")).grid(row=3, column=0, sticky="NEWS")
    Button(root, text="5", font=("Helvetica", "12", "bold"), command=lambda:onClick("5")).grid(row=3, column=1, sticky="NEWS")
    Button(root, text="6", font=("Helvetica", "12", "bold"), command=lambda:onClick("6")).grid(row=3, column=2, sticky="NEWS")
    Button(root, text="-", font=("Helvetica", "12", "bold"), command=lambda:onClick("-")).grid(row=3, column=3, sticky="NEWS")

    Button(root, text="1", font=("Helvetica", "12", "bold"), command=lambda:onClick("1")).grid(row=4, column=0, sticky="NEWS")
    Button(root, text="2", font=("Helvetica", "12", "bold"), command=lambda:onClick("2")).grid(row=4, column=1, sticky="NEWS")
    Button(root, text="3", font=("Helvetica", "12", "bold"), command=lambda:onClick("3")).grid(row=4, column=2, sticky="NEWS")
    Button(root, text="+", font=("Helvetica", "12", "bold"), command=lambda:onClick("+")).grid(row=4, column=3, sticky="NEWS")

    Button(root, text="0", bg="lightpink", font=("Helvetica", "12", "bold"), command=lambda:onClick("0")).grid(row=5, column=0, columnspan=2, sticky="NEWS")
    Button(root, text=".", font=("Helvetica", "12", "bold"), command=lambda:onClick(".")).grid(row=5, column=2, sticky="NEWS")
    Button(root, text="=", font=("Helvetica", "12", "bold"), command=onClickCalculate).grid(row=5, column=3, sticky="NEWS")


def onClickAllClear() :
    spy_display.set("0.0")

def onClickClear() :
    current_value = spy_display.get()
    if current_value != "0.0" and len(current_value) > 1:
        new_value = current_value[:-1]
        spy_display.set(new_value)
    else:
        spy_display.set("0.0")

def onClick(value) :
    temp = spy_display.get()
    if temp == "0.0" :
        spy_display.set(value)
    else :
        spy_display.set(temp + value)

def onClickCalculate() :
    temp = spy_display.get()
    temp = temp.replace("x", "*")
    temp = temp.replace("÷", "/")
    result = eval(temp)
    spy_display.set(result)

root = mainWindow()
spy_display = StringVar()
spy_display.set("0.0")
CreateWidgets(root)
root.mainloop()
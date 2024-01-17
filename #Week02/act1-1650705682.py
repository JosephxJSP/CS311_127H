# ID : 1650705682
# NAME : Nuttanon Rungpiron
# DESC : Activity 2

from tkinter import *

top = Tk()
top.title("Basic GUI#2: Create widgets")
top.geometry("500x350")
top.configure(bg="#F5CBA7")

lbl_title = Label(top, text="Calculating Program", font="Tahoma 14", bg="#F5CBA7", pady=10)
lbl_tag1 = Label(top, text="Tag name 1 :", font="Tahoma 14", bg="#F5CBA7", pady=10, fg="blue")
lbl_tag2 = Label(top, text="Tag name 2 :", font="Tahoma 14", bg="#F5CBA7", fg="green")
txt_tag1 = Entry(top, bg="lightgray", font="Tahoma 14")
txt_tag2 = Entry(top, bg="lightgray", font="Tahoma 14")
btn_button1 = Button(top, text="Button 1", font="Tahoma 14")
btn_button2 = Button(top, text="Button 2", font="Tahoma 14")

lbl_title.grid(row=0, column=0, columnspan=2)
lbl_tag1.grid(row=1, column=0)
txt_tag1.grid(row=1, column=1)
lbl_tag2.grid(row=2, column=0)
txt_tag2.grid(row=2, column=1)
btn_button1.grid(row=3, column=0)
btn_button2.grid(row=3, column=1)

top.mainloop()
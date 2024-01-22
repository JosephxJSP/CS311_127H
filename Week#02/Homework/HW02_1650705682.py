# ID : 1650705682
# NAME : Nuttanon Rungpiron
# DESC : HomeWork 2

from tkinter import *

top = Tk()
top.title("Registration form by Nuttanon Rungpiron")
top.geometry("420x480")

lbl_title = Label(top, text="Registration Form", font="Tahoma 16 bold", fg="blue")
lbl_name = Label(top, text="Name :", font="Tahoma 12")
lbl_email = Label(top, text="Email :", font="Tahoma 12")
lbl_gender = Label(top, text="Gender :", font="Tahoma 12")
lbl_phone = Label(top, text="Phone Number :", font="Tahoma 12")
lbl_username = Label(top, text="User name :", font="Tahoma 12")
lbl_password = Label(top, text="Password :", font="Tahoma 12")
lbl_question = Label(top, text="Security Question :", font="Tahoma 12")
lbl_answaer = Label(top, text="Answer :", font="Tahoma 12")

txt_name = Entry(top, bg="yellow", font="Tahoma 12")
txt_email = Entry(top, bg="yellow", font="Tahoma 12")
radio_gender1 = Radiobutton(top, text="Male", value=1)
radio_gender2 = Radiobutton(top, text="Female", value=2)
radio_gender3 = Radiobutton(top, text="Other", value=3)
txt_phone = Entry(top, bg="yellow", font="Tahoma 12")
txt_username = Entry(top, bg="yellow", font="Tahoma 12")
txt_password = Entry(top, bg="yellow", font="Tahoma 12")
txt_question = Entry(top, bg="yellow", font="Tahoma 12")
txt_answaer = Entry(top, bg="yellow", font="Tahoma 12")

btn_cancel = Button(text="Cancel", bg="lightgray")
btn_register = Button(text="Register", bg="lightgray")

lbl_title.grid(row=0, column=0, columnspan=2, pady=10)
lbl_name.grid(row=1, column=0, sticky="w", padx=30, pady=5)
lbl_email.grid(row=2, column=0, sticky="w", padx=30, pady=5)
lbl_gender.grid(row=3, column=0, rowspan=3, sticky="nw", padx=30, pady=5)
lbl_phone.grid(row=7, column=0, sticky="w", padx=30, pady=5)
lbl_username.grid(row=8, column=0, sticky="w", padx=30, pady=5)
lbl_password.grid(row=9, column=0, sticky="w", padx=30, pady=5)
lbl_question.grid(row=10, column=0, sticky="w", padx=30, pady=5)
lbl_answaer.grid(row=11, column=0, sticky="w", padx=30, pady=5)

txt_name.grid(row=1, column=1, sticky="w", pady=5)
txt_email.grid(row=2, column=1, sticky="w", pady=5)
radio_gender1.grid(row=3, column=1, sticky="w", pady=5)
radio_gender2.grid(row=4, column=1, sticky="w", pady=5)
radio_gender3.grid(row=5, column=1, sticky="w", pady=5)
txt_phone.grid(row=7, column=1, sticky="w", pady=5)
txt_username.grid(row=8, column=1, sticky="w", pady=5)
txt_password.grid(row=9, column=1, sticky="w", pady=5)
txt_question.grid(row=10, column=1, sticky="w", pady=5)
txt_answaer.grid(row=11, column=1, sticky="w", pady=5)

btn_cancel.grid(row=12, column=0, pady=25, ipadx=60)
btn_register.grid(row=12, column=1, pady=25, ipadx=60)

top.mainloop()
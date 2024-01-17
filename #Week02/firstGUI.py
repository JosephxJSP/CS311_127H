from tkinter import *

top = Tk()
top.title("Basic GUI#1: Createmain window")
top.geometry("500x350")
top.configure(bg="#F5CBA7")

lbl_name = Label(top, text="Nuttanon Rungpiron", font="Tahoma 14", background="#F5CBA7", fg="blue")
lbl_nickname = Label(top, text="Friend", bg="lightpink")

txt_username = Entry(top, font="Tohoma 18")
txt_password = Entry(top, font="Tohoma 18", show="*")

btn_login = Button(top, text="Login", bg="lightgray")

lbl_name.pack()
lbl_nickname.pack()
txt_username.pack()
txt_password.pack()
btn_login.pack()

top.mainloop()
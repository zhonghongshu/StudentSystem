from tkinter import *
import tkinter.messagebox
from DataBase import connectDB
from DataBase import closeDB
from DataBase import find
from Student import studentMainWindow
from Teacher import teacherMainWindow
from Administrator import administratorMainWindow

def check(root):
    db=connectDB()
    account=inp1.get()
    password=inp2.get()
    inp1.delete(0, 'end')
    inp2.delete(0, 'end')
    
    results=find(db,account,password)
    
    if not results:
        tkinter.messagebox.showinfo(message='账号/密码错误！')
    else:
        if results[0][2]=="T0":
            administratorMainWindow(root)
        elif results[0][2][0]=='S':
            studentMainWindow(root,account)
        else:
            teacherMainWindow(root)

    closeDB(db)
        
 
root = Tk()
root.geometry('400x300')

root.title('系统登录')
lb1 = Label(root, text='账号：')
lb1.place(relx=0.025, rely=0.25, relwidth=0.4, relheight=0.1)
inp1 = Entry(root)
inp1.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.1)
lb2 = Label(root, text='密码：')
lb2.place(relx=0.025, rely=0.55, relwidth=0.4, relheight=0.1)
inp2 = Entry(root,show='*')
inp2.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.1)


login = Button(root, text='登录',command=lambda:check(root))
login.place(relx=0.15,rely=0.8,relwidth=0.2, relheight=0.1)
quit = Button(root, text='退出',command=root.quit)
quit.place(relx=0.65,rely=0.8,relwidth=0.2, relheight=0.1)


root.mainloop()
exit()

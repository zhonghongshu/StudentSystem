from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import tkinter.messagebox
from DataBase import getScorebyCNAME
from DataBase import getTnamebyCNAME
from DataBase import connectDB
from DataBase import closeDB
from DataBase import getCnobyCname
from DataBase import add
from DataBase import Modify
from DataBase import Delete

def getpoint(num):
    grade=int(num)
    if(grade<60): return 0
    if(grade>=90): return 4.0
    if(grade<90 and grade>=85): return 3.7
    if(grade<85 and grade>=82): return 3.3
    if(grade<82 and grade>=78): return 3.0
    if(grade<78 and grade>=75): return 2.7
    if(grade<75 and grade>=72): return 2.3
    if(grade<72 and grade>=68): return 2.0
    if(grade<68 and grade>=66): return 1.7
    if(grade<66 and grade>=64): return 1.5
    if(grade<64 and grade>=60): return 1.0
    
def newadd(lesson,sno,grade):
    db=connectDB()
    cno=getCnobyCname(db,lesson)
    point=getpoint(grade)
    add(db,sno,cno,grade,point)
    closeDB(db)
    tkinter.messagebox.showinfo(message='添加成绩成功！')
    
def modify(lesson,sno,grade):
    db=connectDB()
    cno=getCnobyCname(db,lesson)
    point=getpoint(grade)
    Modify(db,sno,cno,grade,point)
    closeDB(db)
    tkinter.messagebox.showinfo(message='修改成绩成功！')
    
def delete(lesson,sno):
    db=connectDB()
    cno=getCnobyCname(db,lesson)
    Delete(db,sno,cno)
    closeDB(db)
    tkinter.messagebox.showinfo(message='删除成绩成功！')

def ManageGrade(root,lesson):
    root1 = Toplevel(root)
    root1.geometry('400x300')
    root1.title('成绩管理')
    s="当前选择课程："+lesson
    lb = Label(root1, text=s)
    lb.place(relx=0.25, rely=0.1, relwidth=0.4, relheight=0.1)
    lb1 = Label(root1, text='请输入学号：')
    lb1.place(relx=0.025, rely=0.25, relwidth=0.4, relheight=0.1)
    inp1 = Entry(root1)
    inp1.place(relx=0.3, rely=0.25, relwidth=0.4, relheight=0.1)
    lb2 = Label(root1, text='请输入成绩：')
    lb2.place(relx=0.025, rely=0.55, relwidth=0.4, relheight=0.1)
    inp2 = Entry(root1)
    inp2.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.1)
    
    
    btn1 = Button(root1, text='添加成绩',command=lambda:newadd(lesson,inp1.get(),inp2.get()))
    btn1.place(relx=0.1,rely=0.8,relwidth=0.2, relheight=0.1)
    btn2 = Button(root1, text='修改成绩',command=lambda:modify(lesson,inp1.get(),inp2.get()))
    btn2.place(relx=0.3,rely=0.8,relwidth=0.2, relheight=0.1)
    btn3 = Button(root1, text='删除成绩',command=lambda:delete(lesson,inp1.get()))
    btn3.place(relx=0.5,rely=0.8,relwidth=0.2, relheight=0.1)
    btn4 = Button(root1, text='退出',command=root1.quit)
    btn4.place(relx=0.7,rely=0.8,relwidth=0.2, relheight=0.1)
    
    inp1.delete(0, 'end')
    inp2.delete(0, 'end')
    
    
    root1.mainloop()
    exit()

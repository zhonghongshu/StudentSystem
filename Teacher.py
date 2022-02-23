from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from DataBase import getScorebyCNAME
from DataBase import getTnamebyCNAME
from DataBase import connectDB
from DataBase import closeDB
from Graph import showGraph
from GradeManage import ManageGrade

def clear(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)

def check(treeview1,lesson):
    clear(treeview1)
    db=connectDB()
    
    result=getScorebyCNAME(db,lesson)
    for row in result:
        info = []
        info.append(row[0])
        info.append(row[1])
        treeview1.insert('',END,values=info)
    tname=getTnamebyCNAME(db,lesson)
    
    closeDB(db)
    
    lb1 = Label(root1, text=lesson) 
    lb1.place(relx=0.125, rely=0.0125, relwidth=0.15, relheight=0.1)
    lb2 = Label(root1, text=tname) 
    lb2.place(relx=0.45, rely=0.0125, relwidth=0.15, relheight=0.1)

def showGrade(root1):
    showGraph(root1);

def teacherMainWindow(root):
    root1 = Toplevel(root)
    root1.geometry('800x600')
    root1.title('成绩管理')
             
    lb1 = Label(root1, text='课程：') 
    lb1.place(relx=0.0125, rely=0.0125, relwidth=0.15, relheight=0.1)
    lb2 = Label(root1, text='任课教师：') 
    lb2.place(relx=0.35, rely=0.0125, relwidth=0.15, relheight=0.1)
    lb3 = Label(root1, text='请选择课程名：') 
    lb3.place(relx=0.0125, rely=0.1, relwidth=0.15, relheight=0.2)
    lb4 = Label(root1, text='已选修课此课程的学生：') 
    lb4.place(relx=0.35, rely=0.1, relwidth=0.25, relheight=0.2)
    
    btn1 = Button(root1, text='查询', command=lambda:check(treeview1,combobox.get()))
    btn1.place(relx=0.75,rely=0.35,relwidth=0.15, relheight=0.1)
    btn2 = Button(root1, text='成绩管理', command=lambda:ManageGrade(root1,combobox.get()))
    btn2.place(relx=0.75,rely=0.5,relwidth=0.15, relheight=0.1)
    btn3 = Button(root1, text='成绩分布', command=lambda:showGrade(root1))
    btn3.place(relx=0.75,rely=0.65,relwidth=0.15, relheight=0.1)
    btn4 = Button(root1, text='退出', command=root1.destroy)
    btn4.place(relx=0.75,rely=0.8,relwidth=0.15, relheight=0.1)
    
    values = ['Pascal','数据结构','离散数学','计算机原理','数据库原理','Windows技术','编译原理','系统结构']
    combobox = ttk.Combobox(
                master=root1,
                height=10,  
                width=30, 
                state='normal', 
                cursor='arrow',
                font=('', 15),  
                values=values,  
                )
    combobox.place(relx=0.0125, rely=0.225, relwidth=0.25, relheight=0.05)
    
    columns1 = ("学号", "成绩")
    treeview1 = ttk.Treeview(root1, height=100, show="headings", columns=columns1)
    treeview1.column("学号", width=30, anchor='center') 
    treeview1.column("成绩", width=30, anchor='center') 
    treeview1.heading("学号", text="学号")
    treeview1.heading("成绩", text="成绩")
    treeview1.pack(side=LEFT, fill=BOTH)
    treeview1.place(relx=0.35, rely=0.225, relwidth=0.3, relheight=0.5)
    
    root1.mainloop()
    exit()

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from DataBase import getCount
from DataBase import connectDB
from DataBase import closeDB
from DataBase import getStudentTable
from DataBase import addstudent
from DataBase import addnewaccount
from DataBase import deletestudent
from DataBase import deletenewaccount
import datetime

def clear(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)
    
def refresh(root1,treeview1):
    clear(treeview1)
    db=connectDB()
    table=getStudentTable(db)
    for row in table:
        info = []
        info.append(row[0])
        info.append(row[1])
        info.append(row[2])
        info.append(row[3])
        info.append(row[4])
        info.append(row[5])
        info.append(row[6])
        treeview1.insert('',END,values=info)

    s="记录总数："+str(getCount(db))
    lb1 = Label(root1, text=s) 
    lb1.place(relx=0.3, rely=0.0225, relwidth=0.25, relheight=0.1)
    
    closeDB(db)
    
def newadd(treeview1,s1,s2,s3,s4,s5,i1,i2,root1):
    db=connectDB()
    try:
        addstudent(db,s1,s2,s3,s4,s5)
        addnewaccount(db,i1,i2,i1,s2)
        tkinter.messagebox.showinfo(message='添加信息成功！')
    except:
        tkinter.messagebox.showinfo(message='添加信息失败！此学号已存在！')
    closeDB(db)
    refresh(root1,treeview1)

    
def newdelete(treeview1,sno,root1):
    if(tkinter.messagebox.askyesno(message='删除信息不可恢复！\n确定是否删除该信息！')):
        db=connectDB()
        pre=getCount(db)
        deletestudent(db,sno)
        deletenewaccount(db,sno)
        cur=getCount(db)
        closeDB(db)
        if(pre!=cur):
            tkinter.messagebox.showinfo(message='删除信息成功！')
        else:
            tkinter.messagebox.showinfo(message='删除信息失败！此学号不存在！')
        refresh(root1,treeview1)
    

def add(root,treeview1):
    root1 = Toplevel(root)
    root1.geometry('400x300')
    root1.title('添加信息')
    
    lb1 = Label(root1, text='请输入学号：')
    lb1.place(relx=0.025, rely=0.1, relwidth=0.3, relheight=0.1)
    inp1 = Entry(root1)
    inp1.place(relx=0.3, rely=0.1, relwidth=0.3, relheight=0.1)
    lb2 = Label(root1, text='请输入姓名：')
    lb2.place(relx=0.025, rely=0.2, relwidth=0.3, relheight=0.1)
    inp2 = Entry(root1)
    inp2.place(relx=0.3, rely=0.2, relwidth=0.3, relheight=0.1)
    lb3 = Label(root1, text='请输入性别：')
    lb3.place(relx=0.025, rely=0.3, relwidth=0.3, relheight=0.1)
    inp3 = Entry(root1)
    inp3.place(relx=0.3, rely=0.3, relwidth=0.1, relheight=0.1)
    lb4 = Label(root1, text='请输入年龄：')
    lb4.place(relx=0.025, rely=0.4, relwidth=0.3, relheight=0.1)
    inp4= Entry(root1)
    inp4.place(relx=0.3, rely=0.4, relwidth=0.1, relheight=0.1)
    lb5 = Label(root1, text='请输入专业：')
    lb5.place(relx=0.025, rely=0.5, relwidth=0.4, relheight=0.1)
    inp5 = Entry(root1)
    inp5.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
    lb6 = Label(root1, text='请输入账号：')
    lb6.place(relx=0.025, rely=0.6, relwidth=0.4, relheight=0.1)
    inp6 = Entry(root1)
    inp6.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.1)
    lb7 = Label(root1, text='请输入密码：')
    lb7.place(relx=0.025, rely=0.7, relwidth=0.4, relheight=0.1)
    inp7 = Entry(root1)
    inp7.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)

    
    btn1 = Button(root1, text='添加信息',command=lambda:newadd(treeview1,inp1.get(),inp2.get(),inp3.get(),inp4.get(),inp5.get(),inp6.get(),inp7.get(),root))
    btn1.place(relx=0.4,rely=0.85,relwidth=0.2, relheight=0.1)
    
    
    inp1.delete(0, 'end')
    inp2.delete(0, 'end')
    inp3.delete(0, 'end')
    inp4.delete(0, 'end')
    inp5.delete(0, 'end')
    inp6.delete(0, 'end')
    inp7.delete(0, 'end')
    
    
    root1.mainloop()
    sys.exit()
    
def delete(root,treeview1):
    root1 = Toplevel(root)
    root1.geometry('400x250')
    root1.title('删除信息')
    
    lb1 = Label(root1, text='请输入要删除的学号：')
    lb1.place(relx=0.25, rely=0.1, relwidth=0.4, relheight=0.1)
    inp1 = Entry(root1)
    inp1.place(relx=0.25, rely=0.3, relwidth=0.4, relheight=0.2)
   
    btn1 = Button(root1, text='删除信息',command=lambda:newdelete(treeview1,inp1.get(),root))
    btn1.place(relx=0.3,rely=0.7,relwidth=0.3, relheight=0.2)
    
    
    inp1.delete(0, 'end')
    
    
    root1.mainloop()
    sys.exit()
    
def maintainStudentInfomation(root):
    root1 = Toplevel(root)
    root1.geometry('800x600')
    root1.title('学生信息管理')
    db=connectDB()
    s="记录总数："+str(getCount(db))
    lb1 = Label(root1, text=s) 
    lb1.place(relx=0.3, rely=0.01, relwidth=0.25, relheight=0.2)
    
    closeDB(db)
    columns1 = ("学号", "姓名","性别","年龄","所在系","登录名","密码")
    treeview1 = ttk.Treeview(root1, height=100, show="headings", columns=columns1)
    treeview1.column("学号", width=30, anchor='center') 
    treeview1.column("姓名", width=30, anchor='center') 
    treeview1.column("性别", width=30, anchor='center')
    treeview1.column("年龄", width=30, anchor='center') 
    treeview1.column("所在系", width=40, anchor='center') 
    treeview1.column("登录名", width=30, anchor='center') 
    treeview1.column("密码", width=30, anchor='center') 
    treeview1.heading("学号", text="学号")
    treeview1.heading("姓名", text="姓名")
    treeview1.heading("性别", text="性别")
    treeview1.heading("年龄", text="年龄")
    treeview1.heading("所在系", text="所在系")
    treeview1.heading("登录名", text="登录名")
    treeview1.heading("密码", text="密码")
    treeview1.pack(side=LEFT, fill=BOTH)
    treeview1.place(relx=0.065, rely=0.15, relwidth=0.6, relheight=0.7)

    
    btn1 = Button(root1, text='新增', command=lambda:add(root1,treeview1))
    btn1.place(relx=0.8,rely=0.3,relwidth=0.15, relheight=0.1)
    btn3 = Button(root1, text='删除', command=lambda:delete(root1,treeview1))
    btn3.place(relx=0.8,rely=0.45,relwidth=0.15, relheight=0.1)
    btn4 = Button(root1, text='关闭', command=root1.destroy)
    btn4.place(relx=0.8,rely=0.6,relwidth=0.15, relheight=0.1)
    
    db=connectDB()
    table=getStudentTable(db)

    for row in table:
        info = []
        info.append(row[0])
        info.append(row[1])
        info.append(row[2])
        info.append(row[3])
        info.append(row[4])
        info.append(row[6])
        info.append(row[7])
        treeview1.insert('',END,values=info)
    
    closeDB(db)
    
    root1.mainloop()
    sys.exit()
    
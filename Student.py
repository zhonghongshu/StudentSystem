from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from DataBase import getStudent
from DataBase import getStudentScore
from DataBase import getCNAME
from DataBase import getAvg
from DataBase import getName
from DataBase import getTNAME
from DataBase import getCredit
from DataBase import connectDB
from DataBase import closeDB
from DataBase import getcanchoosecourse
from DataBase import getxk
from DataBase import addxk
from DataBase import getxkCount
from DataBase import deletexk
from DataBase import pdd
import datetime

def clear(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)
    
def refresh(root,treeview1,sno):
    clear(treeview1)
    db=connectDB()
    table=getxk(db,sno)
    for row in table:
        info = []
        info.append(row[0])
        info.append(row[1])
        info.append(row[2])
        info.append(row[3])
        info.append(row[4])
        treeview1.insert('',END,values=info)
    closeDB(db)

def choose(root,sno,cno,treeview):
    if not cno:
        tkinter.messagebox.showinfo(message='请输入课程号！！！')
    else:
        db=connectDB()
        num=pdd(db,cno)
        if num==0:
            tkinter.messagebox.showinfo(message='该课程不存在！')
        else:
            try:
                addxk(db,sno,cno)
                tkinter.messagebox.showinfo(message='选课成功！')
            except:
                tkinter.messagebox.showinfo(message='选课失败！该课程已选！')
            refresh(root,treeview,sno)
        closeDB(db)

    
def unchoose(root,sno,cno,treeview):
    if not cno:
        tkinter.messagebox.showinfo(message='请输入课程号！！！')
    else:
        db=connectDB()
        pre=getxkCount(db)
        deletexk(db,sno,cno)
        cur=getxkCount(db)
        closeDB(db)
        if(pre!=cur):
            tkinter.messagebox.showinfo(message='退课成功！')
        else:
            tkinter.messagebox.showinfo(message='退课失败！此课程不存在！')
        refresh(root,treeview,sno)



def showGPA(root,account):
    root1 = Toplevel(root)
    root1.geometry('800x600')
    root1.title('学生成绩单')
    
    db=connectDB()
    s=getName(db,account)
    GPA=getAvg(db,account)
    closeDB(db)
    time=datetime.datetime.now()
    showtime=time.strftime("%Y-%m-%d")
    s=account+"   "+s+"   "+showtime
    
    Gpa="平均成绩："+str(GPA)
    lb1 = Label(root1, text=s) 
    lb1.place(relx=0.5, rely=0.025, relwidth=0.25, relheight=0.2)
    lb2 = Label(root1, text=Gpa,font=('',20)) 
    lb2.place(relx=0.4, rely=0.7, relwidth=0.25, relheight=0.2)
    
    columns1 = ("课程号", "课程名","成绩","学分","教师")
    treeview1 = ttk.Treeview(root1, height=100, show="headings", columns=columns1)
    treeview1.column("课程号", width=30, anchor='center') 
    treeview1.column("课程名", width=30, anchor='center') 
    treeview1.column("成绩", width=30, anchor='center')
    treeview1.column("学分", width=30, anchor='center') 
    treeview1.column("教师", width=30, anchor='center') 
    treeview1.heading("课程号", text="课程号")
    treeview1.heading("课程名", text="课程名")
    treeview1.heading("成绩", text="成绩")
    treeview1.heading("学分", text="学分")
    treeview1.heading("教师", text="教师")
    treeview1.pack(side=LEFT, fill=BOTH)
    treeview1.place(relx=0.065, rely=0.15, relwidth=0.9, relheight=0.6)
    
    db=connectDB()
    
    cname=getCNAME(db,account)
    h1=[]
    for row in cname:
        h1.append(row)
        
    credit=getCredit(db,account)
    h2=[]
    for row in credit:
        h2.append(row)
        
    tname=getTNAME(db,account)
    h3=[]
    for row in tname:
        h3.append(row)
        
    
        
        
    i=0
    result=getStudentScore(db,account)
    for row in result:
        info = []
        info.append(row[1])
        info.append(h1[i])
        info.append(row[2])
        info.append(h2[i])
        info.append(h3[i])
        i=i+1
        treeview1.insert('',END,values=info)
    
    closeDB(db)
    
    root1.mainloop()
    exit()


    
def studentMainWindow(root,account):
    root1 = Toplevel(root)
    root1.geometry('1000x800')
    root1.title('学生选课管理')
         
    lb1 = Label(root1, text='学生详细信息：') 
    lb1.place(relx=0.0125, rely=0.025, relwidth=0.25, relheight=0.2)
    lb2 = Label(root1, text='可选课程：') 
    lb2.place(relx=0.35, rely=0.025, relwidth=0.15, relheight=0.2)
    lb3 = Label(root1, text='请输入课程号：') 
    lb3.place(relx=0.65, rely=0.025, relwidth=0.15, relheight=0.2)
    lb4 = Label(root1, text='已选修课程成绩：') 
    lb4.place(relx=0.0125, rely=0.45, relwidth=0.25, relheight=0.2)
    lb5 = Label(root1, text='已选课程：') 
    lb5.place(relx=0.35, rely=0.45, relwidth=0.15, relheight=0.2)
         
    inp1 = Entry(root1)
    inp1.place(relx=0.775, rely=0.1, relwidth=0.15, relheight=0.05)
    
    columns1 = ("学号", "姓名","年龄","性别","所在系")
    treeview1 = ttk.Treeview(root1, height=100, show="headings", columns=columns1)
    treeview1.column("学号", width=30, anchor='center') 
    treeview1.column("姓名", width=25, anchor='center') 

    treeview1.column("年龄", width=10, anchor='center')
    treeview1.column("性别", width=10, anchor='center') 
    treeview1.column("所在系", width=50, anchor='center') 
    treeview1.heading("学号", text="学号")
    treeview1.heading("姓名", text="姓名")
    treeview1.heading("年龄", text="年龄")
    treeview1.heading("性别", text="性别")
    treeview1.heading("所在系", text="所在系")
    treeview1.pack(side=LEFT, fill=BOTH)
    treeview1.place(relx=0.0125, rely=0.15, relwidth=0.325, relheight=0.2)
    
    columns2 = ("课程号", "课程名","学分","开课系")
    treeview2 = ttk.Treeview(root1, height=100, show="headings", columns=columns2)
    treeview2.column("课程号", width=30, anchor='center') 
    treeview2.column("课程名", width=30, anchor='center') 
    treeview2.column("学分", width=30, anchor='center')
    treeview2.column("开课系", width=30, anchor='center') 
    treeview2.heading("课程号", text="课程号")
    treeview2.heading("课程名", text="课程名")
    treeview2.heading("学分", text="学分")
    treeview2.heading("开课系", text="开课系")
    treeview2.pack(side=LEFT, fill=BOTH)
    treeview2.place(relx=0.35, rely=0.15, relwidth=0.4, relheight=0.25)
    
    columns3 = ("课程号", "课程名","成绩","绩点")
    treeview3 = ttk.Treeview(root1, height=100, show="headings", columns=columns3)
    treeview3.column("课程号", width=30, anchor='center') 
    treeview3.column("课程名", width=40, anchor='center') 
    treeview3.column("成绩", width=30, anchor='center')
    treeview3.column("绩点", width=30, anchor='center') 
    treeview3.heading("课程号", text="课程号")
    treeview3.heading("课程名", text="课程名")
    treeview3.heading("成绩", text="成绩")
    treeview3.heading("绩点", text="绩点")
    treeview3.pack(side=LEFT, fill=BOTH)
    treeview3.place(relx=0.0125, rely=0.6, relwidth=0.35, relheight=0.25)
    
    columns4 = ("课程号", "课程名","学分","开课系","教师名")
    treeview4 = ttk.Treeview(root1, height=100, show="headings", columns=columns4)
    treeview4.column("课程号", width=30, anchor='center') 
    treeview4.column("课程名", width=30, anchor='center') 
    treeview4.column("学分", width=30, anchor='center')
    treeview4.column("开课系", width=30, anchor='center') 
    treeview4.column("教师名", width=30, anchor='center') 
    treeview4.heading("课程号", text="课程号")
    treeview4.heading("课程名", text="课程名")
    treeview4.heading("学分", text="学分")
    treeview4.heading("开课系", text="开课系")
    treeview4.heading("教师名", text="教师名")
    treeview4.pack(side=LEFT, fill=BOTH)
    treeview4.place(relx=0.38, rely=0.6, relwidth=0.4, relheight=0.25)
    
    btn1 = Button(root1, text='选课', command=lambda:choose(root,account,inp1.get(),treeview4))
    btn1.place(relx=0.8,rely=0.3,relwidth=0.15, relheight=0.1)
    btn2 = Button(root1, text='退课', command=lambda:unchoose(root,account,inp1.get(),treeview4))
    btn2.place(relx=0.8,rely=0.45,relwidth=0.15, relheight=0.1)
    btn3 = Button(root1, text='成绩单', command=lambda:showGPA(root1,account))
    btn3.place(relx=0.8,rely=0.6,relwidth=0.15, relheight=0.1)
    btn4 = Button(root1, text='关闭', command=root1.destroy)
    btn4.place(relx=0.8,rely=0.75,relwidth=0.15, relheight=0.1)
    
    db=connectDB()
    
    result=getStudent(db,account)
    info = []
    info.append(result[0][0])
    info.append(result[0][1])
    info.append(result[0][3])
    info.append(result[0][2])
    info.append(result[0][4])
    print(info)
    treeview1.insert('',END,values=info)
    
    result=getStudentScore(db,account)
    cname=getCNAME(db,account)
    h=[]
    for row in cname:
        h.append(row)
    i=0
    for row in result:
        info = []
        info.append(row[1])
        info.append(h[i])
        info.append(row[2])
        info.append(row[3])
        i=i+1
        treeview3.insert('',END,values=info)
    
    result=getcanchoosecourse(db,account)
    for row in result:
        info = []
        info.append(row[0])
        info.append(row[1])
        info.append(row[2])
        info.append(row[3])
        info.append(row[4])
        treeview2.insert('',END,values=info)
        
    result=getxk(db,account)
    for row in result:
        info = []
        info.append(row[0])
        info.append(row[1])
        info.append(row[2])
        info.append(row[3])
        info.append(row[4])
        treeview4.insert('',END,values=info)
    
    closeDB(db)
    
    
    root1.mainloop()
    exit()

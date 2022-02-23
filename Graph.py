from tkinter import *
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Arial Unicode MS','Microsoft YaHei','SimHei','sans-serif']
plt.rcParams['axes.unicode_minus'] = False
from DataBase import connectDB
from DataBase import closeDB
from DataBase import getGrade


import numpy as np
import pandas as pd
 
def showGraph(root1):
    root = Toplevel(root1)
    root.title("成绩分布")
    root.geometry('800x600')
    
    db=connectDB()
    results=getGrade(db)
    closeDB(db)
    data={}
    for i in results:
        data[i[0]]=i[1]
      
    fig, axs = plt.subplots()
    names = list(data.keys())
    values = list(data.values())
    axs.barh(names, values,height=0.4)
    fig.suptitle('成绩分布')
    canvas = FigureCanvasTkAgg(fig, master=root) 
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
     
    quit = Button(root, text='退出',command=root.quit)
    quit.place(relx=0.45,rely=0.95,relwidth=0.03, relheight=0.02)
    
    
    root.mainloop()
    exit()

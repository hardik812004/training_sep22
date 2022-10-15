import pandas as pd
import matplotlib.pyplot as plt
import tkinter as ttk
import seaborn as sns
import numpy as np
app=ttk.Tk()
app.geometry("600x300")
app.title("Treadmill Users Analysis")

# radiobutton
rb1=ttk.Variable(app)
graphs= ttk.Variable(app)
values={'Pair Plot':'sns.pairplot(data=data)','Joint Plot':"sns.jointplot(data=data,x='{col1}',y='{col2}')",
'Bar Plot':"sns.barplot(data=data,x='{col1}',y='{col2}')"}

graphs.set(values['Pair Plot'])
y=10
for key,value in values.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=value).place(x=10,y=y)
    y+=20

# Option 1 menu
col1=ttk.Variable(app)
values=['Select','Product','Age','Gender']
col1.set(values[0])
ttk.Label(app,text='Column 1').place(x=100,y=10)
ttk.OptionMenu(app,col1,*values).place(x=150,y=40)

# Option 2 menu
col2=ttk.Variable(app)
col2.set(values[0])
ttk.Label(app,text='Column 2').place(x=150,y=80)
ttk.OptionMenu(app,col2,*values).place(x=150,y=110)

# Option 3 menu
col3=ttk.Variable(app)
col3.set(values[0])
ttk.Label(app,text='Column 3').place(x=150,y=150)
ttk.OptionMenu(app,col3,*values).place(x=150,y=180)

def show():
    print(col1.get(),col2.get(),col3.get())

ttk.Button(app,text='show',command=show).place(x=400,y=100)
app.mainloop()
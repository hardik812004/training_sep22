import pandas as pd
import matplotlib.pyplot as plt
import tkinter as ttk
import seaborn as sns
import numpy as np
from PIL import ImageTk, Image

data=pd.read_csv("treadmil-users.csv")
app=ttk.Tk()
app.geometry("600x300")
app.title("Treadmill Users Analysis")

# radiobutton
rb1=ttk.Variable(app)
graphs= ttk.Variable(app)
values={'Pair Plot':'sns.pairplot(data=data)','Joint Plot':"sns.jointplot(data=data,x='{col1}',y='{col2}')",
'Bar Plot':"sns.barplot(data=data,x='{col1}',y='{col2}')",'Box Plot':"sns.boxplot(data=data,x='{col1}',y='{col2}')"}

graphs.set(values['Pair Plot'])
y=10
for key,value in values.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=value).place(x=10,y=y)
    y+=20

# Option 1 menu
col1=ttk.Variable(app)
values=['Select']+list(data.columns)
col1.set(values[0])
ttk.Label(app,text='Column 1').place(x=150,y=10)
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

# Canvas
cnv=ttk.Canvas(app,width=250,height=200)
cnv.place(x=300,y=60)

# Label
result=ttk.Variable(app)
ttk.Label(app,textvariable=result).place(x=300,y=300)

def show():
    # print(col1.get(),col2.get(),col3.get())
    global img
    global cnv
    column1=col1.get()
    column2=col2.get()
    column3=col3.get()
    
    g=graphs.get()
    if 'col1' in g:
        if column1 == 'Select':
            result.set('Column 1 must be selected')
            return
    if 'col2' in g:
        if column2 == 'Select':
            result.set('Column 2 must be selected')
            return
    if 'col3' in g:
        if column3 == 'Select':
            result.set('Column 3 must be selected')
            return


    fig=plt.figure(figsize=(5,2))
    eval(graphs.get().format(col1=column1,col2=column2,col3=column3,))
    fig.savefig("graph.png")
    img=ImageTk.PhotoImage(Image.open('graph.png').resize((250,200)))
    cnv.create_image(0,0,anchor=ttk.NW,image=img)
    result.set("Success")

ttk.Button(app,text='show',command=show).place(x=400,y=100)
app.mainloop()
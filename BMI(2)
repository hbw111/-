
# coding: utf-8

# In[1]:


import tkinter as tk

# 创建一个窗口

window = tk.Tk()

# 设置窗口标题、尺寸

window.title('BMI计算器')

window.geometry('400x400')

# 定义4个变量(对应4个输入框)

var1 = tk.StringVar()

var2 = tk.StringVar()

Bmi1 = tk.StringVar()

Bmi2 = tk.StringVar()

# 创建Lable："身高"

label_height = tk.Label(window,text='身高',font=('隶书',20))

label_height.place(x=10,y=15,width=80,height=40)

# 创建身高的输入框:

entry_height = tk.Entry(window,textvariable=var1,font = ('隶书',20))

entry_height.place(x=90,y=15,width=80,height =40)

# 创建Lable:身高单位cm

label_cm = tk.Label(window,text='cm',font = ('隶书',20))

label_cm.place(x=170,y=15,width = 40,height=40)

# 创建Lable："体重"

label_weight = tk.Label(window,text ='体重',font=('隶书',20))

label_weight.place(x=10,y=65,width=80,height=40)

# 创建体重的输入框

entry_weight = tk.Entry(window,textvariable=var2,font=('隶书',20))

entry_weight.place(x=90,y=65,width = 80,height=40)

# 创建Lable:体重单位kg

label_kg = tk.Label(window,text ='kg',font=('隶书',20))

label_kg.place(x=170,y=65,width=40,height=40)

def bmi():

# 公式 BMI=kg/(cm*cm)

    bmi_set = round(float(entry_weight.get())/(float(entry_height.get())*float(entry_height.get()))*10000,2)

    if bmi_set >=30:

        result = (bmi_set)

        abc = ('重度肥胖')

    elif bmi_set >=28:

        result = (bmi_set)

        abc = ('肥胖')

    elif bmi_set >= 24:

        result = (bmi_set)

        abc = ('超重')

    elif bmi_set >= 18.5:

        result = (bmi_set)

        abc = ('正常')

    else:

        result = (bmi_set)

        abc = ('偏瘦')

    Bmi1.set('您的BMI值为：%s'%result)

    Bmi2.set(abc)

# 创建Button按钮，计算

button_bmi = tk.Button(window,text = '计算BMI',font = ('隶书',20),command = bmi)

button_bmi.place(x = 50,y = 125,width = 300,height = 40)

# 创建计算结果的显示框

entry_bmi1=tk.Entry(window,textvariable = Bmi1,font=('隶书',20))

entry_bmi1.place(x = 30,y = 185,width = 340,height = 50)

entry_bmi2=tk.Entry(window,textvariable = Bmi2,font=('隶书',20))

entry_bmi2.place(x = 30,y = 235,width = 340,height = 50)

# 小提示label

label_kg = tk.Label(window,text ='18.5 < BMI <=24 为正常',font=('宋体',12))

label_kg.place(x=50,y=300,width=250,height=40)

# 循环

tk.mainloop()


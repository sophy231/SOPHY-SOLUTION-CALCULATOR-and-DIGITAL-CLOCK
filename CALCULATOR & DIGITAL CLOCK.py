from tkinter import *
import calendar
import time
root = Tk()
root.title('SOPHY SOLUTION CALCULATOR')
root.geometry('650x600+100+200')
root.resizable(0,0)
root.config(bg= "#000000") # Hexadecimal binary color of black




global equation
equation = ""


def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def back_btn():
    global equation
    length = len(equation)
    b = ""
    for i in range(0, length-1):
        b = b+equation[i]
    equation = b
    label_result.config(text=equation)


def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "syntax error"
            equation = ""
    label_result.config(text=result)


label_result = Label(root, width=25, height= 1, text= "", font=('arial',30))
label_result.pack()


def open():
    if click.get() == 'Digital Clock':
        app = Toplevel(root)
        app.title('DIGITAL CLOCK')
        app.geometry('690x150')
        app.resizable(0,0)

        text_font = ('arial', 40, 'bold')
        bg_color = 'GREEN'
        fg_color = 'red'
        border_width = 30

        lbl = Label(app, font = text_font, bg= bg_color, fg= fg_color, bd= border_width)
        lbl.grid(row=0, column=0)

        def dig_clock():
            time_format = time.strftime('%A: %H: %M: %S %p')
            lbl.config(text= time_format)
            lbl.after(1000, dig_clock)

        dig_clock()
        app.mainloop()




options = [
    'options',
    'Digital Clock'

]

click = StringVar()
click.set(options[0])
drop = OptionMenu(root,click, *options).place(x= 10,y=70)

Button(root, text='submit', command=open).place(x=125 ,y=70)

# Creating special_buttons
Button(root, text="C", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#ADD8E6", command= lambda: clear()).place(x=10, y=100) # light blue
Button(root, text="B", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2B3856", command=lambda: back_btn()).place(x=150, y=100)# Dark slate
Button(root, text="/", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2B3856", command=lambda: show("/")).place(x=290, y=100)# Dark slate
Button(root, text="*", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2B3856", command=lambda: show("*")).place(x=430, y=100)# Dark slate

# Creating Numeric_buttons
Button(root, text="7", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("7")).place(x=10, y=200)# Gunmetal
Button(root, text="8", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("8")).place(x=150, y=200)# Gunmetal
Button(root, text="9", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("9")).place(x=290, y=200)# Gunmetal
Button(root, text="-", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2B3856", command=lambda: show("-")).place(x=430, y=200)# Dark slate

Button(root, text="4", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("4")).place(x=10, y=300)# Gunmetal
Button(root, text="5", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("5")).place(x=150, y=300)# Gunmetal
Button(root, text="6", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("6")).place(x=290, y=300)# Gunmetal
Button(root, text="+", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2B3856", command=lambda: show("+")).place(x=430, y=300)# Dark slate

Button(root, text="1", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("1")).place(x=10, y=400)# Gunmetal
Button(root, text="2", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("2")).place(x=150, y=400)# Gunmetal
Button(root, text="3", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("3")).place(x=290, y=400)# Gunmetal
Button(root, text="0", width=11, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show("0")).place(x=10, y=500)# Gunmetal

Button(root, text=".", width=5, height=1, font=('arial',30,'bold'), bd=1, fg="white", bg="#2C3539", command=lambda: show(".")).place(x=290, y=500)# Gunmetal
Button(root, text="=", width=5, height=3, font=('arial',30,'bold'), bd=1, fg="white", bg="#E9AB17", command=lambda: calculate()).place(x=430, y=400)# Bee yellow

root.mainloop()
#!/usr/bin/env python3
from tkinter import *
import random

def logic():
    sc1.set("")
    alpha = list("qwertyuiopasdfghjklzxcvbnm")
    nums = list("1234567890")
    symbols = list(r"!@#$%^&*()+-={}|[];'<>?,./")
    # print(alpha)
    # print(symbols)
    password = []
    m = random.randint(6, 7)
    for i in range(0, m):
        password.append(random.choice(alpha))
        password.append(random.choice(nums))
        password.append(random.choice(symbols))

    # random.shuffle(password)
    # print("".join(password))
    for i in range(5):
        random.shuffle(password)
    password="".join(password)
    sc1.set(password)


if __name__ == '__main__':
    rt=Tk()
    rt.title("<Tk-987656-Password//Generator?-#$%^^%$#>.exe")
    rt.geometry("600x300")
    Label(rt, text="Offline Password Generator", font=("bold", 28)).place(x=40, y=10)
    Label(rt, text="Click on the Generate Button to get a password.", font=("bold", 15)).place(x=40, y=100)
    Label(rt, text="Program will generate a strong password and copy it.", font=("bold", 15)).place(x=40, y=130)
    sc1=StringVar()
    Entry(rt, font=("bold", 28), textvariable=sc1).place(x=50, y=170)
    Button(rt, text="Generate", font=("bold", 30), command=logic).place(x=50, y=230)
    rt.mainloop()


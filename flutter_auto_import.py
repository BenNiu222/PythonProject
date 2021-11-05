import ntpath
import os
from tkinter import *
import tkinter.filedialog
import shutil

root = Tk()


def xz():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        for i in range(0, len(filenames)):
            shutil.copy(str(filenames[i]), 'D:\\Android\\thai59\\assets\\images\\2.0')
            print("- assets/images/"+ntpath.split(str(filenames[i]))[-1])
    else:
        lb.config(text="您没有选择任何文件")


def xz1():
    filenames = tkinter.filedialog.askopenfilenames()
    if len(filenames) != 0:
        for i in range(0, len(filenames)):
            shutil.copy(str(filenames[i]), 'D:\\Android\\thai59\\assets\\images\\3.0')
            print("- assets/images/" + ntpath.split(str(filenames[i]))[-1])
    else:
        lb.config(text="您没有选择任何文件")




lb = Label(root, text='选择文件')
lb.pack()
btn = Button(root, text="选择2.x图片", command=xz)
btn.pack()
btn1 = Button(root, text="选择3.x图片", command=xz1)
btn1.pack()

root.mainloop()

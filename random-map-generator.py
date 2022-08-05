from tkinter import *
from PIL import ImageTk, Image
import random

x = Tk()
x.title('Map Generator')
x.geometry('412x412')

img0 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\blank.png"))
img1 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\up.png"))
img2 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\right.png"))
img3 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\down.png"))
img4 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\left.png"))

gridImg = {'blank':img0, 'up':img1, 'right':img2, 'down':img3, 'left':img4}
img = ['blank', 'up', 'right', 'down', 'left']
pattern = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]


def entropy(i, j):
    n = ''
    if j==0 and i!=0:
        n = pattern[i-1][j-1]
    else:
        n = pattern[i][j-1]
    if i==0:
        if n=='blank':
            return img
        elif n=='left':
            return ['blank', 'right']
        else:
            return ['up', 'left', 'down']
    else:
        if j==0:
            if pattern[i-1][j]=='blank':
                return img
            elif pattern[i-1][j]=='up':
                return ['blank', 'down']
            else:
                return ['up', 'left', 'right']
        else:
            if pattern[i-1][j]==n:
                if n=='up':
                    return ['blank', 'down']
                elif n=='left':
                    return ['blank', 'right']
                elif n=='blank':
                    return img
                else:
                    return ['up', 'left']
            else:
                if pattern[i-1][j]=='up':
                    if n=='left':
                        return ['blank']
                    else:
                        return ['blank', 'down']
                elif pattern[i-1][j]=='down':
                    if n=='left':
                        return ['blank', 'right']
                    elif n=='blank':
                        return ['up', 'right', 'left']
                    else:
                        return ['up', 'left']
                elif pattern[i-1][j]=='left':
                    if n=='blank':
                        return ['up', 'left', 'right']
                    else:
                        return ['up', 'left']
                elif pattern[i-1][j]=='right':
                    if n=='blank':
                        return ['up', 'left', 'right']
                    elif n=='left':
                        return ['blank', 'right']
                    else:
                        return ['up', 'left']
                else:
                    if n=='left':
                        return ['blank', 'right']
                    else:
                        return ['up', 'left', 'down']


for i in range(4):
    for j in range(4):
        if i == 0 and j == 0:
            pattern[i][j] = img[random.randint(0, 4)]
        else:
            options = entropy(i, j)
            pattern[i][j] = options[random.randint(0, len(options)-1)]


lbl1 = Label(image=gridImg[pattern[0][0]])
lbl1.grid(row=0, column=0)

lbl2 = Label(image=gridImg[pattern[0][1]])
lbl2.grid(row=0, column=1)

lbl3 = Label(image=gridImg[pattern[0][2]])
lbl3.grid(row=0, column=2)

lbl4 = Label(image=gridImg[pattern[0][3]])
lbl4.grid(row=0, column=3)

lbl5 = Label(image=gridImg[pattern[1][0]])
lbl5.grid(row=1, column=0)

lbl6 = Label(image=gridImg[pattern[1][1]])
lbl6.grid(row=1, column=1)

lbl7 = Label(image=gridImg[pattern[1][2]])
lbl7.grid(row=1, column=2)

lbl8 = Label(image=gridImg[pattern[1][3]])
lbl8.grid(row=1, column=3)

lbl9 = Label(image=gridImg[pattern[2][0]])
lbl9.grid(row=2, column=0)

lbl10 = Label(image=gridImg[pattern[2][1]])
lbl10.grid(row=2, column=1)

lbl11 = Label(image=gridImg[pattern[2][2]])
lbl11.grid(row=2, column=2)

lbl12 = Label(image=gridImg[pattern[2][3]])
lbl12.grid(row=2, column=3)

lbl13 = Label(image=gridImg[pattern[3][0]])
lbl13.grid(row=3, column=0)

lbl14 = Label(image=gridImg[pattern[3][1]])
lbl14.grid(row=3, column=1)

lbl15 = Label(image=gridImg[pattern[3][2]])
lbl15.grid(row=3, column=2)

lbl16 = Label(image=gridImg[pattern[3][3]])
lbl16.grid(row=3, column=3)

x.mainloop()

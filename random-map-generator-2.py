from tkinter import *
from PIL import ImageTk, Image
import random

x = Tk()
x.title('Map Generator')
n = int(input("Enter map grid size: "))
size = str(100 * n + n * 5) + 'x' + str(100 * n + n * 5)
x.geometry(size)

img0 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\blank.png"))
img1 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\up.png"))
img2 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\right.png"))
img3 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\down.png"))
img4 = ImageTk.PhotoImage(Image.open("D:\\Programming & Coding\\College Python Programming\\map gen\\left.png"))

gridImg = {'blank':img0, 'up':img1, 'right':img2, 'down':img3, 'left':img4}
img = ['blank', 'up', 'right', 'down', 'left']
pattern = []
for i in range(n):
    lst = []
    for j in range(n):
        lst.append(-1)
    pattern.append(lst)


def entropy(i, j):
    s = ''
    if j==0 and i!=0:
        s = pattern[i-1][j-1]
    else:
        s = pattern[i][j-1]
    if i==0:
        if s == 'blank':
            return img
        elif s == 'left':
            return ['blank', 'right']
        else:
            return ['up', 'left', 'down']
    else:
        if j==0:
            if pattern[i-1][j] == 'blank':
                return img
            elif pattern[i-1][j] == 'up':
                return ['blank', 'down']
            else:
                return ['up', 'left', 'right']
        else:
            if pattern[i-1][j] == n:
                if s == 'up':
                    return ['blank', 'down']
                elif s == 'left':
                    return ['blank', 'right']
                elif s == 'blank':
                    return img
                else:
                    return ['up', 'left']
            else:
                if pattern[i-1][j] == 'up':
                    if s == 'left':
                        return ['blank']
                    else:
                        return ['blank', 'down']
                elif pattern[i-1][j] == 'down':
                    if s == 'left':
                        return ['blank', 'right']
                    elif s == 'blank':
                        return ['up', 'right', 'left']
                    else:
                        return ['up', 'left']
                elif pattern[i-1][j] == 'left':
                    if s == 'blank':
                        return ['up', 'left', 'right']
                    else:
                        return ['up', 'left']
                elif pattern[i-1][j] == 'right':
                    if s == 'blank':
                        return ['up', 'left', 'right']
                    elif s == 'left':
                        return ['blank', 'right']
                    else:
                        return ['up', 'left']
                else:
                    if s == 'left':
                        return ['blank', 'right']
                    else:
                        return ['up', 'left', 'down']


for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            pattern[i][j] = img[random.randint(0, 4)]
        else:
            options = entropy(i, j)
            pattern[i][j] = options[random.randint(0, len(options)-1)]

labels = []


def gridBuilder():
    button.pack_forget()
    for i in range(n):
        for j in range(n):
            Label(image=gridImg[pattern[i][j]]).grid(row=i, column=j)


button = Button(x, text='Generate Map', command=gridBuilder)

button.pack()
x.mainloop()

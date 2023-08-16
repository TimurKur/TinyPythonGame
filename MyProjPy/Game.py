import pygame
from tkinter import *
from time import time
import random
from tkinter.messagebox import showinfo

pygame.init()

window = Tk()
window.title('Игра')
window.resizable(width = False, height = False)

c = Canvas(window, width = 500, height = 500, bg = 'white')
c.pack()

def move_kor(event):
    global k_x
    if event.keysym == 'Left' and k_x > 0:
        c.move(kor, -7, 0)
        k_x -= 7
    if event.keysym == 'Right' and k_x < 500:
        c.move(kor, 7, 0)
        k_x += 7

def create_apple():
    #print(1)
    y = 30
    x = random.randint(25, 475)
    apple = c.create_image(x, y, image = imgap)
    apple_id.append(apple)

def move_apple():
    for i in range(len(apple_id)):
        c.move(apple_id[i], 0, 0.1)

def coll():
    ball = 0
    for app in range(len(apple_id) -1, -1, -1):
        x1, y1 = c.coords(kor)
        x2, y2 = c.coords(apple_id[app])
        if x2 > x1 - 140 and x2 < x1 + 140 and y2 > y1:
            ball += 1
            del_app(app)
    return ball

def del_app(i):
    c.delete(apple_id[i])
    del apple_id[i]

def show_score(score):
    c.itemconfig(score_text, text = str(score))

def show_miss(miss):
    c.itemconfig(miss_text, text = str(miss))

def ms_ap():
    miss_ap = 0
    for app in range(len(apple_id) -1, -1, -1):
        x1, y1 = c.coords(kor)
        x2, y2 = c.coords(apple_id[app])
        if y2 > 500:
            miss_ap += 1
            del_app(app)
    return miss_ap

#Переменные
score = 0
k_x = 400
miss = 0
apple_id = list()

img = PhotoImage(file = 'K:\\MyProjPy\\korsina.png')
kor = c.create_image(400, k_x, image = img)

imgap = PhotoImage(file = 'K:\\MyProjPy\\apple.png')
#apple = c.create_image(250, 30, image = imgap)

c.create_text(50, 30, text = 'Поймано', fill = 'Black')
score_text = c.create_text(50, 50, text = str(score), fill = 'Black')
c.create_text(130, 30, text = 'Пропуски', fill = 'Black')
miss_text = c.create_text(130, 50, text = str(miss), fill = 'Black')

c.bind_all('<Key>', move_kor)

#while miss != 5:
create_apple()

while miss != 5:
    if random.randint(1, 1000) == 1:
        create_apple()
    move_apple()
    score += coll()
    miss += ms_ap()
    show_score(score)
    show_miss(miss)
    window.update()

if miss > 4:
    showinfo(title = "Конец", message = "Вы проиграли!")

window.mainloop()

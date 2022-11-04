# импортируем библиотеки
import random
import time
from math import floor
from tkinter import *

# глобальные переменные
size = 20
# W=1200
# H=2160
H = 600
W = 600
H2 = 420
H3 = 180

BLOCK = 0
game = True
Sn = 0


# функция создания яблока
def apple():
    global BLOCK
    posx = size * random.randint(1, (W - size) / size)
    posy = size * random.randint(1, floor((H2 - size) / size))
    BLOCK = c.create_oval(posx, posy,
                          size + posx, size + posy,
                          fill="red")


# Сегмент змейки(то есть один блок)
class Segment(object):
    def __init__(self, x, y):
        self.crt = c.create_rectangle(
            x, y,
            x + size, y + size,
            fill="black",
            outline="red"
        )


# работа Змейки
class Snake(object):
    def __init__(self, s):
        # создаем атрибут метода
        self.s = s
        # направление первоначального движения
        self.vector = (1, 0)

    # вверх
    def dir_up(self):
        self.vector = (0, -1)

    # вниз
    def dir_d(self):
        self.vector = (0, 1)

    # право
    def dir_r(self):
        self.vector = (1, 0)

    # лево
    def dir_l(self):
        self.vector = (-1, 0)

    # Кнопки
    def buttons(self):
        br = Button(f, text="Right", width=50, height=50, command=self.dir_r, bg="red")
        br.place(rely=0.30, relx=0.65, relwidth=0.25, relheight=0.40)

        bl = Button(f, text="Left", width=50, height=50, command=self.dir_l, bg="red")
        bl.place(rely=0.30, relx=0.1, relwidth=0.25, relheight=0.40)

        bu = Button(f, text="Up", width=50, height=50, command=self.dir_up, bg="red")
        bu.place(rely=0.1, relx=0.38, relwidth=0.25, relheight=0.40)

        bd = Button(f, text="Down", width=50, height=50, command=self.dir_d, bg="red")
        bd.place(rely=0.56, relx=0.38, relwidth=0.25, relheight=0.40)

        # добавление сегмента

    # движение змейки
    def motion(self):
        for index in range(len(self.s) - 1):
            segment = self.s[index].crt
            x1, y1, x2, y2 = c.coords(self.s[index + 1].crt)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.s[-2].crt)
        c.coords(self.s[-1].crt,
                 x1 + self.vector[0] * size,
                 y1 + self.vector[1] * size,
                 x2 + self.vector[0] * size,
                 y2 + self.vector[1] * size)
        c.update()
        time.sleep(0.15)

    def add_segment(self):
        last_segment = c.coords(self.s[0].crt)
        x = last_segment[0]
        y = last_segment[1]
        y = y - size
        x = x - size

        self.s.insert(0, Segment(x, y))

    def main(self):
        global game
        if game:
            self.motion()
            # координаты головы
            head_coord = c.coords(self.s[-1].crt)
            # записываем координаты от головы
            x1, y1, x2, y2 = head_coord
            # столкновение со стенкой
            if x2 > W or x1 < 0 or y1 < 0 or y2 > H:

                game = False

            # при съедании яблока
            elif head_coord == c.coords(BLOCK):
                self.add_segment()
                c.delete(BLOCK)
                apple()
            else:
                for index in range(len(self.s) - 1):
                    if head_coord == c.coords(self.s[index].crt):
                        game = False



        # движение змейки - основное




# что будет при проигрыше
def after_die():
    text = c.create_text(W / 2, H2 / 2, text="Game Over", anchor=CENTER, font="Arial 22 bold", fill="black")
    # связка с текстом
    c.tag_bind(text, '<Button-1>', restart)


def start_game():
    global Ssnake
    # создание змейки , то есть объединение сегментов в один список
    Ssnake = [Segment(size, size),
              Segment(2 * size, size),
              Segment(3 * size, size)]
    sn = Snake(Ssnake)
    apple()
    sn.buttons()
    while game:
        c.after(10, sn.main())
    after_die()
    c.update()


# холст и экран
tk = Tk()
c = Canvas(tk,
           width=W, height=H,
           bg='green')
f = Canvas(tk, width=W, height=H3, bg="darkgreen")
# касание
# c.focus_set()
# инициализация экрана
c.place(relx=0.04)
# настройка нижней панели
f.place(rely=0.7, relx=0.04)


# restart
def restart(event):
    global game
    game = True
    c.delete(ALL)
    start_game()


# game name
tk.title("pixdec")
# старт игры
start_game()
# игровой цикл
tk.mainloop()
#Проверочка


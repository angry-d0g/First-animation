from tkinter import *
import time
import pyglet
from colour import Color

tk = Tk()
tk.title('Sound check')
tk.iconphoto(True, PhotoImage(file='Иконка.png'))
window = Canvas(tk, height=500, width=570, background="thistle2")  # задаем размеры окна
window.pack()  # применяем размеры холста
tk.resizable(width=False, height=False)  # неизменяемые размеры окна

# Описываем фигуры
g_arc = 0.5
color_arc = str(Color(rgb=(1, g_arc, 0)))  # цвет для круга
corner = 180
arc = window.create_arc(400, 50, 520, 170, extent=corner, fill=color_arc)

ball = window.create_oval(250, 175, 325, 250, fill="yellow")
window.create_line(30, 50, 60, 50)
rec = window.create_rectangle(0, 450, 75, 470, fill="purple3")

y1 = 150
graph = window.create_rectangle(30, y1, 60, 175, fill="green")


# функция для корректного закрытия программы
def close():
    global running
    running = False


tk.protocol("WM_DELETE_WINDOW", close)

running = True
while running:
    mus = pyglet.resource.media('otskok-myacha.mp3')
    for i in range(50):
        window.move(rec, 5, 0)
        window.move(ball, 0, 4)

        y1 -= 2
        window.coords(graph, 30, y1, 60, 175)

        corner += 3.6
        g_arc -= 0.01
        color_arc = str(Color(rgb=(1, g_arc, 0)))
        window.delete(arc)
        arc = window.create_arc(400, 50, 520, 170, extent=corner, fill=color_arc)
        tk.update()
        if i != 49:
            time.sleep(0.0005)

    mus.play()
    mus = pyglet.resource.media('otskok-myacha.mp3')

    for i in range(50):
        window.move(rec, 5, 0)
        window.move(ball, 0, -4)

        y1 += 2
        window.coords(graph, 30, y1, 60, 175)

        corner -= 3.6
        g_arc += 0.01
        color_arc = str(Color(rgb=(1, g_arc, 0)))
        window.delete(arc)
        arc = window.create_arc(400, 50, 520, 170, extent=corner, fill=color_arc)

        tk.update()
        time.sleep(0.0005)

    for i in range(50):
        window.move(rec, -5, 0)
        window.move(ball, 0, 4)

        y1 -= 2
        window.coords(graph, 30, y1, 60, 175)

        corner -= 3.6
        g_arc += 0.01
        color_arc = str(Color(rgb=(1, g_arc, 0)))
        window.delete(arc)
        arc = window.create_arc(400, 50, 520, 170, extent=corner, fill=color_arc)

        tk.update()
        if i != 49:
            time.sleep(0.0005)

    mus.play()

    for i in range(50):
        window.move(rec, -5, 0)
        window.move(ball, 0, -4)

        y1 += 2
        window.coords(graph, 30, y1, 60, 175)

        corner += 3.6
        g_arc -= 0.01
        color_arc = str(Color(rgb=(1, g_arc, 0)))
        window.delete(arc)
        arc = window.create_arc(400, 50, 520, 170, extent=corner, fill=color_arc)

        tk.update()
        time.sleep(0.0005)

tk.destroy()

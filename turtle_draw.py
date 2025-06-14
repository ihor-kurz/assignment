import tkinter as tk
import turtle

# Створюємо вікно і полотно
root = tk.Tk()
root.title("Turle: Малювання кнопками 🐢")

canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Створюємо turtle в цьому canvas
screen = turtle.TurtleScreen(canvas)
t = turtle.RawTurtle(screen)
t.speed(1)

# ==== Функції ====
def forward():
    t.forward(50)

def backward():
    t.backward(50)

def left():
    t.left(45)

def right():
    t.right(45)

def circle():
    t.circle(30)

def color():
    t.color("red")

def color_blue():
    t.color("blue")

def clear():
    t.clear()

# ==== Кнопки ====
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="⬆ Вперед", command=forward).grid(row=0, column=1)
tk.Button(frame, text="⬅ Вліво", command=left).grid(row=1, column=0)
tk.Button(frame, text="⏺ Коло", command=circle).grid(row=1, column=1)
tk.Button(frame, text="➡ Вправо", command=right).grid(row=1, column=2)
tk.Button(frame, text="⬇ Назад", command=backward).grid(row=2, column=1)

tk.Button(frame, text="🔴 Червоний", command=color).grid(row=3, column=0)
tk.Button(frame, text="🔵 Синій", command=color_blue).grid(row=3, column=2)
tk.Button(frame, text="🧹 Очистити", command=clear).grid(row=3, column=1)

# Запуск
root.mainloop()

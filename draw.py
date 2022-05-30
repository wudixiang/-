import turtle
import time
import threading
from threading import Thread
def drawSnake(rad, angle, len, neckrad):
    for i in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad*2/3)


# 笔画分块
def drawHline(dr, len):
    # 向左画横
    if dr == 0:
        turtle.fd(len)
    # 向右画横
    if dr == 1:
        turtle.backward(len)


def drawVline(dr, len):
    # 向下画竖
    if dr == 0:
        turtle.seth(270)
        turtle.fd(len)
        turtle.seth(0)
    # 向上画竖
    if dr == 1:
        turtle.seth(90)
        turtle.fd(len)
        turtle.seth(0)


def drawTurn(dr, radius, rad):
    turtle.seth(270)
    # 画右撇
    if dr == 0:
        turtle.circle(-radius, rad)
        turtle.seth(0)
    # 画左撇
    if dr == 1:
        turtle.circle(radius, rad)
        turtle.seth(0)


# 进度条
def drawProcess(num, s):
    for i in range(num):
        sign = '#' * i
        time.sleep(s)
        print("\r{} {:2}%".format(sign, i), end=" ")


def init_pen():
    turtle.reset()
    turtle.setup(1300, 800, 0, 0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.pencolor("green")
    turtle.speed(5)
    turtle.seth(0)
    # drawHline(0,50)
    # drawHline(1,50)
    # drawVline(0,50)
    # drawVline(1,50)
    # drawTurn(0,120,60)
    # drawTurn(1,120,60)
    # drawcharacter(50,90,120,-60)
    # turtle.write("翔",move=False, align="left",font=("宋体",30,"normal"))


def drawBig():
    start = time.perf_counter()
    # for i in range(101):
    #   sign='#'*i
    #   print("\r{} {:2}%".format(sign,i), end=" ")
    init_pen()
    drawHline(0, 200)
    turtle.penup()
    turtle.goto(110, 80)
    turtle.pendown()
    drawTurn(0, 280, 50)
    turtle.penup()
    turtle.goto(110, 0)
    turtle.pendown()
    drawTurn(1, 200, 50)
    # turtle.exitonclick()
    # turtle.bye()
    end = time.perf_counter()
    print('运行时间 : %s 秒' % (end - start))
    turtle.done()

def drawBigtime():
  t1 = Thread(target=drawProcess, args=(101, 0.015))
  t2 = Thread(target=drawBig, args=())
  t1.start()
  t2.start()
  threads = []
  threads.append(t1)
  threads.append(t2)
  for t in threads:
      t.join()
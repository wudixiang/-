import turtle
import datetime
color = "black"
font1 = 'Arial'
def init_pen():
    turtle.reset()
    turtle.setup(1300, 2000, -500, 0)
    pythonsize = 5
    turtle.pensize(pythonsize)
    turtle.pencolor(color)
    turtle.speed(5)
    turtle.seth(0)
def drawGap(): # 绘制数码管间隔
   turtle.penup()
   turtle.fd(5)
def drawLine(draw):     #绘制数码管的每一段
    drawGap()
    if(draw):
        turtle.down()
    else:
        turtle.up()

    turtle.fd(40)
    drawGap()
    turtle.right(90)

def drawDigit(i):      #绘制数码管的每个数字
    if i in [2,3,4,5,6,8,9,'A','B','D','E','F']:      #g管
        drawLine(True)
    else:
        drawLine(False)

    if i in [0,1,3,4,5,6,7,8,9,'A','B','D']:  #c管
        drawLine(True)
    else:
        drawLine(False)

    if i in [0,2,3,5,6,8,9,'B','C','D','E']:        #d管
        drawLine(True)
    else:
        drawLine(False)

    if i in [0,2,6,8,'A','B','C','D','E','F']:            #e管
        drawLine(True)
    else:
        drawLine(False)

    turtle.left(90)

    if i in [0,4,5,6,8,9,'A','B','C','E','F']:        #f管
        drawLine(True)
    else:
        drawLine(False)

    if i in [0,2,3,5,6,7,8,9,'A','C','E','F']:    #a管
        drawLine(True)
    else:
        drawLine(False)

    if i in [0,1,2,3,4,7,8,9,'A','D']:    #b管
        drawLine(True)
    else:
        drawLine(False)

    turtle.right(180)
    turtle.penup()
    turtle.fd(20)


def drawData(date):
    for i in date:
        drawDigit(eval(i))

def drawDate(time):     #绘制日期
    for i in time:
        if i == '年':
            turtle.write('年',font=(font1, 30, "normal"))
            turtle.fd(50)
            # turtle.pencolor("green")
        elif i == '月':
            turtle.write('月',font=(font1, 30, "normal"))
            # turtle.pencolor("blue")
            turtle.fd(50)
        elif i == '日':
            turtle.write('日',font=(font1, 30, "normal"))
            turtle.fd(50)
        elif i in ['0','1','2','3','4','5','6','7','8','9']:
            drawDigit(eval(i))
        else:
            print('未按标准格式输入日期，请重新输入')
            drawDate(input('请输入日期：（格式为2021年6月23日）'))
def chooseColor():
    global color
    try:
      color = input('请输入想要的颜色：')
      turtle.pencolor(color)
    except:
        print('没有这种颜色，请重新输入颜色')
        chooseColor()

def chooseFont():
    global font1
    try:
      font1 = input('请输入想要的字体：')
    except:
        print('没有这种字体，请重新输入字体')
        chooseFont()

def showChoiceMenu():

    print('***********七段数码管显示菜单************')
    print('1.显示输入的日期')
    print('2.显示当前系统时间')
    print('3.显示任意数字')
    print('4.调整字体')
    print('5.调整画笔颜色')
    print('*************************************')
    choice = input('请选择-->')
    if choice == '1':
        init_pen()
        drawDate(input('请输入日期：（格式为2021年6月23日）'))
    elif choice == '2':
        init_pen()
        drawDate(datetime.datetime.now().strftime('%Y年%m月%d日'))
    elif choice == '3':
       try:
         num = input("请输入任意个数字：")
         print(num)
         init_pen()
         drawData(num)
       except NameError:
         print("输入错误，请输入数字！")
         num = input("请输入任意个数字：")
         print(num)
         init_pen()
         drawData(num)
    elif choice =='4':
       chooseFont()
       showChoiceMenu()
    elif choice == '5':
       chooseColor()
       showChoiceMenu()
def runSevenDigital():
    showChoiceMenu()

    # init_pen()
    # drawData('1')
    # drawDate(datetime.datetime.now().strftime('%Y年%m月%d日'))
    # turtle.done()
    # turtle.exitonclick()

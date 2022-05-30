import time
from random import random


# 便于交互 打印提示语
def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


# 输入选手的能力值和需要模拟的次数
def getInputs():
    a = eval(input("请输入选手A的能力值（0-1）："))
    b = eval(input("请输入选手A的失误概率（0-1）："))
    c = eval(input("请输入选手B的能力值（0-1）："))
    d = eval(input("请输入选手B的失误概率（0-1）："))
    n = eval(input("模拟比赛的场次："))
    return a, b, c, d,  n

#加入天气因素
def inputWeather():
    weather = 0
    print("模拟比赛天气情况")
    print("1.晴天")
    print("2.雨天")
    print("3.雪天")
    print("4.阴天")
    m = input("请选择模拟比赛的天气情况：")
    if m == '1' :
        weather = 1
    elif m == '2':
        weather = 2
    elif m == '3':
        weather = 3
    elif m == '4':
        weather = 4
    else:
        print("系统目前还没有该天气情况，请重新选择")
        inputWeather()

    return weather

#天气影响对于球员能力的改变
def impactProb(weather,probA, misA, probB, misB):
    if weather == 1:
        misA *= 0.9  #晴天A失误率降低百分之10 有利于A
    elif weather == 2:
        misA *= 1.2   #雨天A失误率提高百分之20，B失误率提高百分之10 有利于B
        misB *= 1.1
    elif weather == 3:
        misA *= 1.2   #雪天A失误率提高百分之20，B失误率提高百分之30，A能力值提高百分之20，B能力值降低百分之10 有利于A
        misB *= 1.3
        probA *= 1.2
        probB *= 0.9
    elif weather == 4:
        probB *= 1.5 #阴天A能力值提高百分之20，B能力值提高百分之50，有利于B
        probA *= 1.2
    else:
        print("敬请期待")

# 输出出模拟的结果
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞赛分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛， 占比{:0.1%}".format(winsB, winsB / n))


# 一场比赛over就是得分15
def gamesOver(a, b):
    return a == 15 or b == 15


# 模拟一次比赛
def gameOneGame(probA, misA, probB, misB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gamesOver(scoreA, scoreB):
        if serving == "A":
            if random() > misA:
                scoreB += 1
            else:
                if random() < probA:
                    scoreA += 1
                else:
                    serving = "B"
        else:
            if random() > misB:
                scoreA += 1
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    serving = "A"
    return scoreA, scoreB


# 模型N次比赛
def simNGames(n, probA, misA, probB, misB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = gameOneGame(probA, misA, probB, misB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


# 主函数
def beginGame():
    printIntro()
    probA, misA, probB, misB, n = getInputs()
    weather = inputWeather()
    impactProb(weather, probA, misA, probB, misB)
    winsA, winsB = simNGames(n, probA, misA, probB, misB)
    printSummary(winsA, winsB)
    time.sleep(3)

# 调用主函数
# beginGame()

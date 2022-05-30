import time

wrong_point = 0 #用于统计出现语法错误个数的总和
def getpath():
    txt = open(r"C:\Users\W\Desktop\现代编程技术\现代编程大作业\所有代码.txt", encoding='utf-8')
    contents = txt.read()
    txt.close()
    return contents

#获取文件中所有关键字
def getKeyword(contents):
    words = contents.split()
    retainwords = ["False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif",
                  "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda",
                  "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"]
    keyword = []
    for word in words:
        if word in retainwords and word not in keyword:
            keyword.append(word)

    return keyword

#查询所有位置
def findAllsit(sun,word):
    listsit = []
    sit = sun.find(word)
    while sit != -1:
        listsit.append(sit)
        sit = sun.find(word, sit + 1)
    return listsit

#for语法检查
def grammarfor(list,sun):
    global wrong_point
    for i in list:
        flag = 0
        #防止出现包含for的单词引起报错
        if sun[i-1] != ' ' and sun[i+3] != ' ':
            continue
        while sun[i] != '\n':
          if sun[i] != ':' and sun[i]!='i' :
              i += 1
          elif sun[i]=='i':
              if sun[i-1] == ' ' and sun[i+1] == 'n' and sun[i+2] == ' ':
                  flag = 1
                  i += 1
              else:
                  i += 1
          elif sun[i] == ':':
              if flag == 1:
                  flag = 2
                  break
        if flag == 0 or flag == 1:
            wrong_point = wrong_point + 1
            print("语法错误")
            print("出错位置在：",i,"出错语法关键词为：for")

#def语法检查
def grammardef(list,sun):
    global wrong_point
    for i in list:
        flag = 0
        if sun[i - 1] != ' ' and sun[i + 3] != ' ':
            continue
        while sun[i] != '\n':
          if sun[i] != ':':
              i += 1
          elif sun[i] == ':':
              flag = 1
              break
        if flag == 0:
            wrong_point = wrong_point + 1
            print("语法错误")
            print("出错位置在：", i, "出错语法关键词为：def")
#if语法检查
def grammarif(list,sun):
    global wrong_point
    for i in list:
        flag = 0
        if sun[i - 1] != ' ' and sun[i + 2] != ' ':
            continue
        while sun[i] != '\n':
            if sun[i] != ':':
                i += 1
            elif sun[i] == ':':
                flag = 1
                break
        if flag == 0:
            wrong_point = wrong_point + 1
            print("语法错误")
            print("出错位置在：", i, "出错语法关键词为：if")
#elif语法检查
def grammarelif(list,sun):
    global wrong_point
    for i in list:
        flag = 0
        if sun[i - 1] != ' ' and sun[i + 4] != ' ':
            continue
        while sun[i] != '\n':
            if sun[i] != ':':
                i += 1
            elif sun[i] == ':':
                flag = 1
                break
        i = i-1
        #看上一个冒号前是不是if
        while sun[i] != ':':
            i -= 1
        while sun[i] != '\n':
            if sun[i] == 'i' and sun[i+1] == 'f' and sun[i-1] == ' ' and sun[i+2] == ' ':
                if flag == 1:
                    flag = 2
                    break
            #如果上一个冒号也是elif
            elif sun[i] == 'e' and sun[i-1] == ' ' and sun[i+1] == 'l' and sun[i+2] == 'i' and sun[i+3] == 'f' and sun[i+4] == ' ':
                if flag == 1:
                    flag = 2
                    break
            else:
                i -= 1
        if flag == 0 or flag == 1:
            wrong_point = wrong_point + 1
            print("语法错误")
            print("出错位置在：", i, "出错语法关键词为：elif")
#else语法检查
def grammarelse(list,sun):
    global wrong_point
    for i in list:
        flag = 0
        if sun[i - 1] != ' ' and sun[i + 4] != ' ':
            continue
        if sun[i+5] == ':':
            flag = 1
        if flag == 0:
            wrong_point = wrong_point + 1
            print("语法错误")
            print("出错位置在：", i, "出错语法关键词为：else")
#try语法检查
def grammartry(list,sun):
    global wrong_point
    for i in list:
        flag = 0
        if sun[i - 1] != ' ' and sun[i + 3] != ' ':
            continue
        while sun[i] != '\n':
            if sun[i] != ':':
                i += 1
            elif sun[i] == ':':
                flag = 1
                break
        i = i+1
        #看下一个冒号前有没有except
        while sun[i] != ':':
            i += 1
        while sun[i] != '\n':
            if sun[i] == 'e' and sun[i+1] == 'x' and sun[i+2] == 'c' and sun[i+3] == 'e' and sun[i+4] == 'p' and sun[i+5] == 't' and sun[i-1] == ' ' and sun[i+6] == ' ':
                if flag == 1:
                   flag = 2
                   break
            else:
                i = i-1
        if flag == 0 or flag == 1:
            wrong_point = wrong_point + 1
            print("语法错误")
            print("出错位置在：", i, "出错语法关键词为：try")


#遍历文件，查找关键字出现的位置,并判断语法是否正确
def findKeyword():
    global wrong_point
    sun = getpath()
    moon = getKeyword(sun)
    for word in moon:
      allsit = findAllsit(sun, word)
      # print(word,":")
      # print(allsit)
      if word =='for':
        grammarfor(allsit, sun)
      if word == 'def':
        grammardef(allsit, sun)
      if word == 'if':
        grammarif(allsit, sun)
      if word == 'elif':
        grammarelif(allsit, sun)
      if word == 'else':
        grammarelse(allsit, sun)
      if word == 'try':
        grammartry(allsit, sun)
    if wrong_point == 0:
      print("非常完美，没有语法错误")
    if wrong_point != 0:
      print("共有",wrong_point,"个错误")
      wrong_point = 0
    time.sleep(2)









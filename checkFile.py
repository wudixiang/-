

def getpath():
    txt = open(r"C:\Users\W\Desktop\现代编程技术\现代编程大作业\所有代码.txt", encoding='utf-8')
    contents = txt.read()
    txt.close()
    return contents


def getRetainword():
    sun = getpath()   #获取文本
    words = sun.split()   #将文本中所有单词分隔开储存到一个列表里
    counts = {}
    statistic = {}
    #将所有保留字放到一个列表里
    retainwords = ["False","None","True","and","as","assert","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","nonlocal","not","or","pass","raise","return","try","while","with","yield"]
    #计算文件中各个单词的个数
    for word in words:
          counts[word] = counts.get(word,0) + 1

    for word in retainwords:
        if word in counts:
            #将保留字出现次数储存到新字典中，并从原字典中删除
            statistic[word] = counts.pop(word)
        else:
            statistic[word] = 0
    item = list(statistic.items())
    item.sort(key=lambda x:x[1], reverse=True)
    for i in range(32):
        word, count = item[i]
        print("{0:<10}{1:>5}".format(word,count))

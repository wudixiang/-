#urllib一个与网址相关的库
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re




def runCrawler0():
    #设定一个网址
  urp = "https://hao.360.com/?a1004"
    #打开这个网址
  resp = urlopen(urp)
    #将网址中内容存储到文件中
  with open("mycrawler.html",mode = "w", encoding='utf-8')as f:
      f.write(resp.read().decode("utf-8"))
  print("OK!爬完了")


#输入搜索内容
def searchUrl():
    q = input("请输入电影排行榜：")
    url = f"https://www.so.com/s?q={q}"

    return url

#此函数用于获取网页的html文档
def getHTMLText(url):

    try:
        #获取服务器的响应内容，并设置最大请求时间为6秒
        res = requests.get(url, timeout = 6)
        #判断返回状态码是否为200
        res.raise_for_status()
        #设置该html文档编码为utf-8
        res.encoding = "utf-8"
        #返回网页HTML代码
        return res.text
    except:
        return '产生异常'


    #获取所有母链接的子链接
def getAlllink(text):
    soup = BeautifulSoup(text, 'html.parser')
    # 模糊搜索HTML代码的所有包含href属性的<a>标签
    a_labels = soup.find_all('a', attrs={'href': True})
    #去重
    a_labels0 = []
    a_labels = set(a_labels)
    return a_labels
#获取有价值的网站进行遍历
def getWorthlink(labels):
    # 获取所有<a>标签中的href对应的值，即超链接
    for a in labels:
      gaokao = a.get('href')
    #筛选出与豆瓣排名有关链接
      if gaokao and 'movie.douban.com' in gaokao:
        print(gaokao)
        return gaokao
        # infor = getHTMLText(gaokao)
        # soup1 = BeautifulSoup(infor, 'html.parser')
        # print(soup1.a)


    #获取子链接中所有有价值链接并遍历获取信息
def getWorthlink1(labels):
    # 获取所有<a>标签中的href对应的值，即超链接
    for a in labels:
      movie = a.get('href')
    #筛选出电影链接并提取影片名字与内容简介输出
      if movie and 'movie.douban.com' in movie and 'subject' in movie :
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        }
        res = requests.get(movie,headers = headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        span0 = soup.find('span',attrs={'property': 'v:itemreviewed'})  #电影名
        span1 = soup.find('span', attrs={'property': 'v:summary'})      #内容简介
        print(span0.text)
        print(span1.text)
        print(movie)



def setLayers():
    layers = eval(input("想要爬取的网络层数:"))
    return layers

def recycleLink(url, layers, layer):
    first = getHTMLText(url)
    all_links = getAlllink(first)
    print(all_links)
    for a in all_links:
        layer += 1
        print(layer)
        if layer > layers:
            break
        else:
            link = a.get('href')
            recycleLink(link, layers, layer)




#爬取电影网各个电影名字，链接即内容简介
def runCrawler1():
    url = searchUrl()
    res = getHTMLText(url)
    son_h = getAlllink(res)
    son_url = getWorthlink(son_h)
    son_ht = getHTMLText(son_url)
    grandson_h = getAlllink(son_ht)
    getWorthlink1(grandson_h)

#爬取设定网络层数所有链接
def runCrawler2():
    url = searchUrl()
    layers = setLayers()
    recycleLink(url, layers, 1)


    # resp = requests.get(url)
    #查看响应状态
    # print(resp)
    # with open("mycrawler.html", mode="w", encoding='utf-8') as f:
    #     f.write(resp.text)
    # read = resp.text
    # for ch in read:
    #     if u'\u4e00' <= ch <= u'\u9fa5':
    #         print(ch, end = " ")
    # #查看页面源代码
    # # print(resp.text)



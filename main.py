import SevenDigital
import draw
import hash
import datetime
import checkFile
import MatchAnalysis
import reptile
import checkGrammar
#由于在选择绘图程序显示进度条时使用双线程并行运行，所以导致重回菜单时无法回到主循环，再次画图将自动退出程序。
#若先进行除2以外选项则不会出现该问题。


def menu():
    print(datetime.datetime.now().strftime('%Y年%m月%d日'))
    print('**************************************')
    print('现代编程技术课程作业')
    print('1.哈希函数')
    print('2.绘图程序')
    print('3.七段数码管显示')
    print('4.统计以上代码中各保留字个数')
    print('5.模拟体育竞技比赛')
    print('6.搜索引擎爬虫程序')
    print('7.简易语法检查器')
    print('8.结束')
    print('**************************************')

def choice():
       while(1):
            menu()
            choice = input('请选择->')
            if choice == '1':
                x = input('请输入需要加密内容：')
                hash.myhash(x)
            elif choice == '2':
                draw.drawBigtime()
            elif choice == '3':
                SevenDigital.showMenu()
            elif choice == '4':
                checkFile.getRetainword()
            elif choice == '5':
                MatchAnalysis.beginGame()
            elif choice == '6':
                reptile.runCrawler1()
            elif choice == '7':
                checkGrammar.findKeyword()
            elif choice == '8':
                print("谢谢使用，下次再见")
                break
            else:
                print("输入无效，请重新选择")
                run()

def run():
    choice()

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
      run()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

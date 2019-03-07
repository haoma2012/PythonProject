# import sys

# Python 支持的格式：Numbers String List Tuple Dictionary
import re
import smtplib
import threading
import time
from email.header import Header
from email.mime.text import MIMEText

var1 = 10
var2 = 20

name = 'Hello,World!'

'''
print str

'''

print(name)
print(name[0])

del var1, var2

# 条件语句
flag = True
xi_name = 'xixi'
if xi_name == 'python':
    flag = False
    print('welcome boss')

else:
    print(xi_name)

# list 列表
myList = [1, 2.0, "a", True]
print(myList[1], myList[1:3], myList[2:], myList[-2])

myList.append('Jay')
# myList.index(2.0, 3)
# delete 删除
del myList[0]
myList.remove('a')
# print(myList.sort(), myList.reverse(), myList.copy())
print(myList)
# 元组 tuple ('a', 'b', 'c') myTuple(0,)
print(tuple(myList))

# 字典 dict
student = {'Alice': '18', 'Beth': '19', 'Lucy': '20'}
print(student['Alice'])
student['Beth'] = '29'
student['DeHao'] = 30

# 集合 set
set1 = set()
set2 = {1, 2, 3, 4, 5, 1}
set2.add(6)
print(6 in set2)
set2.remove(2)
print(6 not in set2)
set3 = set('12345')
for data in set2:
    print(data)

# 编程第一步
print('-------编程第一步-------')
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b
print('迭代器使用')
it = iter(set3)
for x in it:
    print('当前值: ' + x)


class MyNumbers:
    sex = 1

    # def __init__(self, sex):
    #     self.sex = sex
    #     print(sex)

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

    def printinfo(self, name='ddd', age='25'):
        print("姓名：" + name + " age = " + age)

    def print_tuple(self, *var_tuple):
        print("输出元组：")
        for data in var_tuple:
            print(data)

        return

    def test_print(self, test_str):
        print(test_str)
        str(test_str)
        repr(test_str)

    # def func(self, n):
    #     x, y = 0, 1
    #     while n > 0:
    #         n -= 1
    #         yield y
    #         x, y = y, x + y
    def test_execpt(self):
        try:
            result = 1 / 0
        except ZeroDivisionError:
            print("捕捉到除数为0的异常啦！")


myClass = MyNumbers()
myiter = iter(myClass)
print(next(myiter))
# 函数变量 使用
myClass.printinfo("ggg")
myClass.print_tuple(10, 20, 30)
myClass.test_print("hahahah")
# myClass.func(10)
myClass.test_execpt()

# 时间处理
ticks = time.time()
local_time = time.localtime(ticks)
print("当前时间戳是:%s%s", ticks, local_time)

input_str = input("请输入：")
print("你输入的内容是：", input_str)

# 读取文件
# f = open("/Users/yangdehao/Desktop/TinyPng.py", "r")

# file_content = f.read()
# print(file_content)
# f.close()

print(re.match('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span())
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$', '', phone)
print("移除注释：", num)

'''
# 测试SMTP发送邮件
# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "XXXX"  # 用户名
mail_pass = "XXXXXX"  # 口令
sender = "yangdehao@xiaoyouzi.com"  # 发送者
receivers = ['724319417@qq.com']  # 接收者 可以多个 qq邮箱

message = MIMEText('我是python发送的一封邮件：来自美柚yangdehao的邮件 ', 'plain', 'utf-8')
message['From'] = Header("小柚子yang", 'utf-8')
message['To'] = Header("samrt-yang", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP()
    smtpobj
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("发送邮件成功！！！")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
'''

# Python3 多线程threading
exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 5)
        print("退出线程：" + self.name)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadname, delay, counter):
    while counter:
        if exitFlag:
            threadname.exit()
        time.sleep(delay)
        print("%s: %s" % (threadname, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
# thread1.join()
# thread2.join()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()
print("退出主线程")

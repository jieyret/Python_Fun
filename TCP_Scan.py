# -*- coding:utf-8 -*-
# -*- by shackle -*-
#  输入主机名与端口->主机名变为IPV4地址->
import optparse
import socket
import threading

###
# 建立socket连接
def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        print '[+]%d/tcp open'%tgtPort
        connSkt.close()
    except:
        print '[-]%d/tcp closed '% tgtPort



## 定义端口扫描函数
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)

    except:
        print "[-] Cannot resolve '%s': Unknown host" % tgtHost
        return

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP
    socket.setdefaulttimeout(1)
    ### 多线程，多端口
    for tgtPort in tgtPorts:
        print('Scanning port ' + str(tgtPort))
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('use:  –H <target host> -P <target port>')  # 新建paser对象
    parser.add_option('-H', '--host', dest='tgtHost', type='string', help='taget host')
    parser.add_option('-P', '--port', dest='tgtPort', type='int', help='taget port')

    (options, args) = parser.parse_args()
    # 已经定义好了所有的命令行参数，调用 parse_args() 来解析程序的命令行：
    # options，它是一个对象（optpars.Values），保存有命令行参数值。只要知道命令行参数名，如 file，就可以访问其对应的值： options.file 。
    # args，它是一个由 positional arguments 组成的列表。

    tgtHost = options.tgtHost
    tgtPort = options.tgtPort
    args.append(tgtPort)  # 设置端口列表
    if (tgtHost == None) | (tgtPort == None):
        print parser.usage
        exit(0)
    portScan(tgtHost,args)


if __name__ == '__main__':
    main()


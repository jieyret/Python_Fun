# -*- coding:utf-8 -*-
# -*- by shackle -*-
#!/usr/bin/python
from spider import webspider as myspider
import sys, optparse

def crawler(URLs):
        for line in open(URLs, 'r'):
                URL = line.strip()
                links = myspider(b=URL.strip(), w=200, d=5, t=5)
                link_count = len(links[0])
                out = URL+": has a link count of "+str(link_count)
                print "[+] Web Crawl Results for: "+URL
                print out
                for item in links[1]:
                        print item

def main():
# optparse模块允许你通过参数选项来调用那段代码
# 这里我使用 '-r'选项并且内容会保存在URLs变量里面
# 当使用-r参数的使用脚本会去读取指定的文件夹
        parser = optparse.OptionParser(sys.argv[0]+' '+ \
        '-r <file_with URLs>')
        parser.add_option('-r', dest='URLs', type='string', \
                help='specify target file with URLs')
        (options, args) = parser.parse_args()
        URLs=options.URLs

        if (URLs == None):
                print parser.usage
                sys.exit(0)
        else:
                crawler(URLs)

if __name__ == "__main__":
      main()
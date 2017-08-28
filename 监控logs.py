# -*- coding:utf-8 -*-
# -*- by shackle -*-

#!/usr/local/bin/python3.5
###Destription: 实时读取log信息
###Author: Danny Deng
###Datetime: 2016-11-17

import re,time,subprocess,os,linecache
#####定义log文件
file_name = "/usr/local/nginx/logs/error.log"
file_number = "/usr/local/zabbix_agent/number.txt"
j = int(0)
seek = int(0)
##判断过程：文件是否存在---判断存储日志大小的文件是否存在---判断number size 与 filesize的大小
###定义函数按行读取文件内容
def readline():
####if判断 seek是否大于0，大于则赋值，否则初始为0
    while True:
######定义文件，根据seek值进行每行读取，每次tell赋值给seek
    with open(file_name,'r') as f:
global seek
#seek = seek
f.seek(seek)
data = f.readline()
if data:
seek = f.tell()
yield data
else:
######Python变量转换为shell变量
global file_number
os.environ['seek'] = str(seek)
os.environ['file_number'] = str(file_number)
os.system('echo $seek > $file_number')
os.system('chown zabbix.zabbix $file_number')
return
def func_for():
j = int(0)
for i in readline():
f_find = re.findall(r"check time out", i,flags=re.IGNORECASE)
if "check time out" in f_find:
j += 1
#####没有输出0，有值输出出现error匹配到的次数值
try:
print(j)
except NameError:
print(int("0"))
###判断日志文件是否存在
if os.path.isfile(file_name):
###判断存储文件内容大小的文件是否存在
if os.path.isfile(file_number):
####存在则读取文件size大小，赋值给seek_number
seek_number = int(linecache.getline(file_number, 1))
####然后继续判断存储的文件大小与现在文件大小(确定文件是否是重新生成的)
if os.path.getsize(file_name) >= seek_number and seek_number > 0:
seek = seek_number
func_for()
###若为新文件则，seek 赋值为0
else:
#open(arg1, "a+").write("0")
#seek = int(linecache.getline(file_number, 1))
seek = int(0)
func_for()
####file_number 不存在则新建，并赋值seek变量为0
else:
#open(file_number, "a+").write("0")
#seek = int(linecache.getline(file_number, 1))
os.environ['file_number'] = str(file_number)
os.system('echo 0 > $file_number')
os.system('chown zabbix.zabbix $file_number')
func_for()
else:
print("Error")
quit()
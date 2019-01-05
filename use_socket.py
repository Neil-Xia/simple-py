#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_socket.py
@Time    :   2019/01/04 15:01:25
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import socket

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))

# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据:
buffer = []
while True:
    #每次最多接受1k字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()
#可以使用\r\n\r\n区分头部？
header, html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#把接收到数据写入文件
with open('sina.html','wb') as f:
    f.write(html)
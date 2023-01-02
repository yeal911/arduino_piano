import socket
import time

import data as data

notes:list = ['LOW33', 'MID33', 'MID23', 'MID0', 'MID2', 'MID4', 'MID5', 'MID7', 'MID9', 'MID11', 'HIG0', 'HIG1']

# 创建socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# # 绑定本机的IP和接口
# s.bind(('127.0.0.1', 8888))

for tmp in notes:
    # 发送数据
    s.sendto(tmp.encode("utf-8"), ('127.0.0.1', 8888))
    time.sleep(0.1)
    print(tmp)

# 关闭socket
s.close()
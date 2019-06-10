import socket
tcp_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字
tcp_socket.connect(('172.27.35.26',8080))#建立连接
tcp_socket.send('你好'.encode('gbk'))#发送信息并转码
ret=tcp_socket.recv(1024)#接受信息并解码
print(ret.decode('gbk'))
tcp_socket.close()#关闭套接字
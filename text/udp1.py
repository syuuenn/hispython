import socket
if __name__ == '__main__':
    udp1_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp1_socket.bind(("",9000))
    udp1_socket.sendto('你好'.encode('gbk'), ('172.27.35.26', 9000))
    udp1_socket.close()

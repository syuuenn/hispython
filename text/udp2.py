import socket
if __name__ == '__main__':
    udp2_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp2_socket.bind(("", 9000))
    data = udp2_socket.recvfrom(1024)
    data = data.decode('gbk')
    print(data)

    udp2_socket.close()
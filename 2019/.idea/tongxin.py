import socket
if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while 1:
        udp_socket.sendto('hello java'.encode('gbk'),("172.27.35.26",8080))
    udp_socket.close()

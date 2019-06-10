import socket


if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",10000))

    rs=input('请输入:')
    udp_socket.sendto(rs.encode('gbk'),('172.27.35.26',8080))

    data,address=udp_socket.recvfrom(1024)

    data=data.decode('gbk')
    print(data)
    udp_socket.close()

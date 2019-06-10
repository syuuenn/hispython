import threading
import socket
udp_socket=None

def send():
    while True:
        rs = input('请输入:')
        udp_socket.sendto(rs.encode('gbk'), ('172.27.35.26', 8080))
def recv():
    while True:
        data, address_info= udp_socket.recvfrom(1024)
        data = data.decode('gbk')
        print(data)
def main():
    global udp_socketni
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   # udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    udp_socket.bind(("", 7500))

    send_thread = threading.Thread(target=send)
    recv_thread = threading.Thread(target=recv)
    send_thread.start()
    recv_thread.start()

if __name__ == '__main__':
    main()
#修改中


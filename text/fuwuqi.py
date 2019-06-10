import socket
import threading
def recv_data(new_socket):
        while 1:
            data=new_socket.recv(1024)
            if data:
                senddata()
                print(data.decode('gbk'))
            else:
                break
def senddata(new_socket):
    new_socket.send("已收到！谢谢！".encode('gbk'))
if __name__ == '__main__':
    create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    create_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    create_socket.bind(("", 8080))
    create_socket.listen()
    while 1:
        new_socket = create_socket.accept()

    recv_thread = threading.Thread(target=recv_data,args=(new_socket,))
    recv_thread.start()
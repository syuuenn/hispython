import socket
import threading


def recv_data(new_socket):
    try:
        while 1:
            data=new_socket.recv(1024)
            if data:
                print(data.decode('gbk'))
            else:
                break
    except Exception as e:
        print(e)
    finally:
        new_socket.close()

#def senddata():
    # while 1:
    #     sendinfo=input('收到消息：')
    #     r=new_socket.send(sendinfo.encode('gbk'))
    #     print("收到消息的返回值：",r)
# new_socket.close()
# tcp_socket.close()#两个套接字都要关闭


if __name__ == '__main__':
    create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    create_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    create_socket.bind(("", 8080))
    create_socket.listen()
    while 1:
        new_socket = create_socket.accept()
        # new_socket,client_address=tcp_socket.accept()


   # sendthread = threading.Thread(target=senddata)
    recv_thread = threading.Thread(target=recv_data,args=(new_socket,))


    #sendthread.start()
    recv_thread.start()


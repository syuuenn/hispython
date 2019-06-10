import socket
import chardet
import threading
import sys

class MainServer(object):
    def __init__(self,port):
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)#回收端口
        self.server_socket.bind(('',8000))
        self.server_socket.listen()



    def start(self):
        while 1:
            handler_socket,address=self.server_socket.accept()
            thread_handler_socket=threading.Thread(target=self.handler_client,args=(handler_socket,))
            thread_handler_socket.start()

    def handler_client(self,handler_socket):
        recv_data=handler_socket.recv(1024).decode()
        request_datas = recv_data.split('\r\n')
        # print(request_datas)
        request_data=request_datas[0]
        data=request_data.split(' ')
        # print(data)

        # responsebody=''
        # status=''
        try:
            request_path=data[1]

        except:
            # print(request_path)
            request_path='/'
        else:
            if request_path=='/':
                status = '200 ok'
                responsebody = 'hello world!'
            elif request_path == '/index.html':
                status = '200 ok'
                with open('index.html','rb') as f:
                    responsebody = f.read()
                # responsebody = response_data.encode()
            elif request_path == '/login':
                status = '200 ok'
                with open('login.jpg','rb') as f:
                    responsebody = f.read()

            else:
                status='404 not found'
                with open('err.html') as f:
                    responsebody = f.read()


        responseHeader = 'HTTP/1.1 '+status+' \r\n'
        responseHeader += '\r\n'
        try:
            chardet.detect(responsebody)
        except:
            response = responseHeader + responsebody
            response = response.encode()
        else:
            response = responseHeader.encode() + responsebody

        handler_socket.send(response)
def main():
    try:
        port=int(sys.argv[1])
    except:
        port=8000
    finally:
        server_object=MainServer(port)
        server_object.start()



if __name__ == '__main__':
    main()
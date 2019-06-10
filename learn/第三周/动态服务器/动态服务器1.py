import socket
import chardet
import threading
import sys

class MainServer(object):
    def __init__(self,port,app):
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server_socket.bind(('',port))
        self.server_socket.listen()
        self.response_data=None
        self.app=app

    def handler_client(self,handler_socket):
        recv_data=handler_socket.recv(1024).decode()
        request_datas = recv_data.split('\r\n')
        # print(request_datas)
        request_data=request_datas[0]
        data=request_data.split(' ')
        # print(data)


        try:
            request_path=data[1]

        except:
            # print(request_path)
            request_path='/'
        environ = {'path': request_path}
        if request_path.endswith('.exe'):
            # 交给动态资源处理框架去做
            # 第一步调用框架的接口
            response_body = self.app(environ, self.start_response)
            data = self.response_data + response_body
            handler_socket.send(data.encode('gbk'))
            handler_socket.close()
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
            response = response.encode('gbk')
        else:
            response = responseHeader.encode('gbk') + responsebody

        handler_socket.send(response)

    def start_response(self,status,header_list):
        response_header = 'HTTP/1.1 %s\r\n'%status
        reponse_header = ''
        for header_key,header_value in header_list:
            reponse_header += ('%s:%s\r\n'%(header_key,header_value))

        self.response_data = response_header + reponse_header + '\r\n'

    def start(self):
        while True:
            handler_socket, addressinfo = self.server_socket.accept()
            thread_handler_socket = threading.Thread(target=self.handler_client, args=(handler_socket,))
            thread_handler_socket.start()

def main():

    try:
        port=int(sys.argv[1])
        framing_name=sys.argv[2]
    except:
        port=8000
        framing_name = 'application_list:app'
    finally:
        interface_list=framing_name.split(':')
        module_name=interface_list[0]
        app_name=interface_list[1]
        interface_object=__import__(module_name)
        app=getattr(interface_object,app_name)


        server_object=MainServer(port=port,app=app)
        server_object.start()



if __name__ == '__main__':
    main()
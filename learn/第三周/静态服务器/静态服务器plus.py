import socket
import chardet
def main():
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('',8000))
    server_socket.listen()
    while 1:
        handler_socket,address=server_socket.accept()
        recv_data=handler_socket.recv(1024).decode()
        request_datas = recv_data.split('\r\n')
        # print(request_datas)
        request_data=request_datas[0]
        data=request_data.split(' ')
        # print(data)

        responsebody=''
        status=''
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


if __name__ == '__main__':
    main()
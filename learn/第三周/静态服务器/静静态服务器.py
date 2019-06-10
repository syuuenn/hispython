'''这个程序实现的是一个静态服务器'''
import socket
import re


def main():
    '''主函数，实现逻辑'''
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(('',8000))

    server_socket.listen()
    while True:
        handler_socket,address = server_socket.accept()
        data = handler_socket.recv(1024).decode() #字节流文件--字符串
        print(data)
        #切割字符串
        request_datas_list = data.split('\r\n')
        print(request_datas_list)
        first_line = request_datas_list[0]
        ret = re.search('GET (/.*?) HTTP/1.1',first_line)
        # 判断是否有ret值，如果没有，说明是一个非法请求
        if not ret:
            handler_socket.close()
            return
        request_path = ret.group(1)

        print('**********************')

        responseHeader = 'HTTP/1.1 200 ok123\r\n'
        responseHeader += '\r\n'
        if request_path == '/':
            strtt = 'hello world!'
            responsebody = strtt.encode()
        elif request_path == '/index.html':
            with open('index.html') as f:
                response_data = f.read()
            responsebody = response_data.encode()
        elif request_path == '/login':
            with open('login.jpg','rb') as f:
                responsebody = f.read()
        else:
            with open('err.html') as f:
                responsebody = f.read()

        reponse = responseHeader.encode()+responsebody
        handler_socket.send(reponse)



if __name__ == '__main__':
   main()
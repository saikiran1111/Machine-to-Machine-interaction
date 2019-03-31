import socket
import os
import subprocess
def ping_result(ip_add):
    ping_output = {}
    proc = subprocess.Popen(["ping", "-w", "1", ip_add], shell=False)
    proc.wait()
    if proc.returncode == 0:
        ping_output[ip_add] = True
    else:
        ping_output[ip_add] = False
    return ping_output

def client_program():
    print("1.english \n 2.german \n 3.prochagese 4.spanish ")
    m=raw_input("enter the choice")
    
    try:
        while(m == "english" or m=="1"):
            port=5000
            host = "192.168.1.79"  # as both code is running on same pc
            a=ping_result(host)
            if a[host]:   
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the ser # connect to the server

                message = raw_input(" -> ")  # take input

                while message.lower().strip() != 'bye':
                    client_socket.send(message.encode())  # send message
                    data = client_socket.recv(1024).decode()  # receive response
                    print('Received from server: ' + data)  # show in terminal

                    message = raw_input(" -> ")  # again take input

                client_socket.close()
                # close the connection
            else:
                port=5000
                host = "192.168.1.79"  # as both code is running on same pc
                a=ping_result(host)
                if a[host]:   
                    client_socket = socket.socket()  # instantiate
                    client_socket.connect((host, port))  # connect to the ser # connect to the server

                    message = raw_input(" -> ")  # take input

                    while message.lower().strip() != 'bye':
                        client_socket.send(message.encode())  # send message
                        data = client_socket.recv(1024).decode()  # receive response
                        print('Received from server: ' + data)  # show in terminal

                        message = raw_input(" -> ")  # again take input

                    client_socket.close()
                    # close the connection
                else:
                    port=5000
                    host = "192.168.1.79"  # as both code is running on same pc
                    a=ping_result(host)
                    if a[host]:   
                        client_socket = socket.socket()  # instantiate
                        client_socket.connect((host, port))  # connect to the ser # connect to the server

                        message = raw_input(" -> ")  # take input

                        while message.lower().strip() != 'bye':
                            client_socket.send(message.encode())  # send message
                            data = client_socket.recv(1024).decode()  # receive response
                            print('Received from server: ' + data)  # show in terminal

                            message = raw_input(" -> ")  # again take input

                        client_socket.close()
                    # close the connection
        while(m == "german" or m=="2"):
            port=5000
            host = "192.168.1.79"  # as both code is running on same pc
            a=ping_result(host)
            if a[host]:   
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the ser # connect to the server

                message = raw_input(" -> ")  # take input

                while message.lower().strip() != 'bye':
                    client_socket.send(message.encode())  # send message
                    data = client_socket.recv(1024).decode()  # receive response
                    print('Received from server: ' + data)  # show in terminal

                    message = raw_input(" -> ")  # again take input

                client_socket.close()
                # close the connection
            else:
                port=5000
                host = "192.168.1.79"  # as both code is running on same pc
                a=ping_result(host)
                if a[host]:   
                    client_socket = socket.socket()  # instantiate
                    client_socket.connect((host, port))  # connect to the ser # connect to the server

                    message = raw_input(" -> ")  # take input

                    while message.lower().strip() != 'bye':
                        client_socket.send(message.encode())  # send message
                        data = client_socket.recv(1024).decode()  # receive response
                        print('Received from server: ' + data)  # show in terminal

                        message = raw_input(" -> ")  # again take input

                    client_socket.close()
                    # close the connection
                else:
                    port=5000
                    host = "192.168.1.79"  # as both code is running on same pc
                    a=ping_result(host)
                    if a[host]:   
                        client_socket = socket.socket()  # instantiate
                        client_socket.connect((host, port))  # connect to the ser # connect to the server

                        message = raw_input(" -> ")  # take input

                        while message.lower().strip() != 'bye':
                            client_socket.send(message.encode())  # send message
                            data = client_socket.recv(1024).decode()  # receive response
                            print('Received from server: ' + data)  # show in terminal

                            message = raw_input(" -> ")  # again take input

                        client_socket.close()
                    # close the connection
                    
        while(m == "prochagese" or m=="3"):
            port=5000
            host = "192.168.1.79"  # as both code is running on same pc
            a=ping_result(host)
            if a[host]:   
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the ser # connect to the server

                message = raw_input(" -> ")  # take input

                while message.lower().strip() != 'bye':
                    client_socket.send(message.encode())  # send message
                    data = client_socket.recv(1024).decode()  # receive response
                    print('Received from server: ' + data)  # show in terminal

                    message = raw_input(" -> ")  # again take input

                client_socket.close()
                # close the connection
            else:
                port=5000
                host = "192.168.1.79"  # as both code is running on same pc
                a=ping_result(host)
                if a[host]:   
                    client_socket = socket.socket()  # instantiate
                    client_socket.connect((host, port))  # connect to the ser # connect to the server

                    message = raw_input(" -> ")  # take input

                    while message.lower().strip() != 'bye':
                        client_socket.send(message.encode())  # send message
                        data = client_socket.recv(1024).decode()  # receive response
                        print('Received from server: ' + data)  # show in terminal

                        message = raw_input(" -> ")  # again take input

                    client_socket.close()
                    # close the connection
                else:
                    port=5000
                    host = "192.168.1.79"  # as both code is running on same pc
                    a=ping_result(host)
                    if a[host]:   
                        client_socket = socket.socket()  # instantiate
                        client_socket.connect((host, port))  # connect to the ser # connect to the server

                        message = raw_input(" -> ")  # take input

                        while message.lower().strip() != 'bye':
                            client_socket.send(message.encode())  # send message
                            data = client_socket.recv(1024).decode()  # receive response
                            print('Received from server: ' + data)  # show in terminal

                            message = raw_input(" -> ")  # again take input

                        client_socket.close()
        while(m == "spanish" or m=="4"):
            port=5000
            host = "192.168.1.79"  # as both code is running on same pc
            a=ping_result(host)
            if a[host]:   
                client_socket = socket.socket()  # instantiate
                client_socket.connect((host, port))  # connect to the ser # connect to the server

                message = raw_input(" -> ")  # take input

                while message.lower().strip() != 'bye':
                    client_socket.send(message.encode())  # send message
                    data = client_socket.recv(1024).decode()  # receive response
                    print('Received from server: ' + data)  # show in terminal

                    message = raw_input(" -> ")  # again take input

                client_socket.close()
                # close the connection
            else:
                port=5000
                host = "192.168.1.79"  # as both code is running on same pc
                a=ping_result(host)
                if a[host]:   
                    client_socket = socket.socket()  # instantiate
                    client_socket.connect((host, port))  # connect to the ser # connect to the server

                    message = raw_input(" -> ")  # take input

                    while message.lower().strip() != 'bye':
                        client_socket.send(message.encode())  # send message
                        data = client_socket.recv(1024).decode()  # receive response
                        print('Received from server: ' + data)  # show in terminal

                        message = raw_input(" -> ")  # again take input

                    client_socket.close()
                    # close the connection
                else:
                    port=5000
                    host = "192.168.1.79"  # as both code is running on same pc
                    a=ping_result(host)
                    if a[host]:   
                        client_socket = socket.socket()  # instantiate
                        client_socket.connect((host, port))  # connect to the ser # connect to the server

                        message = raw_input(" -> ")  # take input

                        while message.lower().strip() != 'bye':
                            client_socket.send(message.encode())  # send message
                            data = client_socket.recv(1024).decode()  # receive response
                            print('Received from server: ' + data)  # show in terminal

                            message = raw_input(" -> ")  # again take input

                        client_socket.close()
                    # close the connection
        
    except:
        pass


if __name__ == '__main__':
    client_program()

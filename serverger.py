import socket

from  chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000 

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    bot = ChatBot('Bot')
    bot.set_trainer(ListTrainer)


    for files in os.listdir('C:\Users\sappy\Desktop\Major project\data\german/'):
        dat = open('C:\Users\sappy\Desktop\Major project\data\german/' + files,'r').readlines()
        bot.train(dat)
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        message = data
        if message.strip() !='bye':
            reply = bot.get_response(message)
        #print('ChatBot:',reply)
        #print(type(reply))
        if not data:
            # if data is not received break
            break
        #print("from connected user: " + str(data))
        
        conn.send(str(reply).encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()


import pygame
from pgui import *
from norpher import NORPH
import socket
import threading
import random

import time
def create_checksum(num):
    a = random.randrange(1,num//2)
    return f'{num-a}+{a}={num}'

def receive(data,connection:socket.socket,key,eq):
    
    encrypted_data = NORPH(str(data.decode()),key,eq)
    
    print('data thing:'+encrypted_data)
    
    connection.send(encrypted_data.encode())
    other_decrypt = connection.recv(1024).decode()
    raw = NORPH(str(other_decrypt),key,eq)
    
    csin = raw.find('checksum:')
    checksum = raw[csin:]
    parts = checksum.split('=')
    if str(eval(parts[0])) == parts[1]:
        return raw, True
    else:
        return '', False

def send(data:str,connection:socket.socket,key,eq):
    data+=f'checksum:{create_checksum(random.randrange(100,10000))}'
    _d = NORPH(data,key,eq).encode()
    connection.send(_d)
    
    
def client_program():
     host = input("What is the host name?")  # as both code is running on same pc
     port = int(input("What is the server's port?"))  # socket server port number



     conn = socket.socket()  # instantiate
     conn.connect((host, port))  # connect to the server

     message = input(" -> ")  # take input
     

     while message.lower().strip() != 'bye':
          send(message,conn,'mngtrpail','abs(x**3 - 3*x**2 + 63)')
          data = receive(conn,'mngtrpail','abs(x**3 - 3*x**2 + 63)')  # receive response
          


          print('boxoserv: ' + data)  # show in terminal
          print(' ')
          message = input(" -> ")  # again take input
          print(' ')

     conn.close()  # close the connection


def server_program():
     # get the hostname
     host = socket.gethostname()
     print(host)
     port = int(input("Enter port: "))  # initiate port no above 1024

     server_socket = socket.socket()  # get instance
     # look closely. The bind() function takes tuple as argument
     server_socket.bind((host, port))  # bind host address and port together

     # configure how many client the server can listen simultaneously
     server_socket.listen(2)
     conn, address = server_socket.accept()  # accept new connection
     print("Connection from: " + str(address))
     while True:
          # receive data stream. it won't accept data packet greater than 1024 bytes
          data = receive(conn,'boxo','tan(x**2)')
          
          if not data:
               # if data is not received break
               break
          print("boxouser: " + str(data))
          print(' ')
          data = input(' -> ')
          print(' ')
          send(data,conn,'boxo','tan(x**2)')

     conn.close()  # close the connection






pygame.init()
a = pygame.display.get_desktop_sizes()[0]
dis = pygame.display.set_mode(a)

global msg_array
msg_array = []



serv = input("Hosting? ").lower()
if serv == 'y' or serv == 'yes' or serv.startswith('y'):
    HOSTING=True
    host = socket.gethostname()
    print(host)
    port = int(input("Enter port: "))  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
else:
    HOSTING=False
    host = input("What is the host name?")  # as both code is running on same pc
    port = int(input("What is the server's port?"))  # socket server port number

    conn = socket.socket()  # instantiate
    conn.connect((host, port))  # connect to the server



handler=Handler()




def s():
    inp_opts = handler.collate_textinput_inputs()
    
    mes = inp_opts.get('mesg')
    print("SENDING " + mes)
    if mes:
        if HOSTING:
            send(mes,conn,'boxo','tan(x**2)')
        else:
            send(mes,conn,'mngtrpail','abs(x**3 - 3*x**2 - 63)')
    
def _(_):
    pass


M = GUIobj([0,0],a,'message')
M.move_window = _


mesgbox = TextInput([0,0],'',None,None,'mesg')
tbut = Button([0,0],'Send',None,None,s)

USE = DisplayColumns([
            mesgbox, tbut
        ])



M.add_content(
    DisplayRows([
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        USE
    ])
)

def coll2():
    while True:
        if HOSTING:
            data = conn.recv(1024)
            dec = data.decode()
            this = NORPH(dec,'boxo','tan(x**2)')
            
            
            
            
            if this.find('checksum') == -1:
                conn.send(this.encode())
                
                
            else:
                outp=NORPH(data.decode(),'boxo','tan(x**2)')
                outp=outp[:len(outp)-2]
                msg_array.append(outp)
                print('logging')
                
        else:
            
            data = conn.recv(1024)
            dec = data.decode()
            this = NORPH(dec,'mngtrpail','abs(x**3 - 3*x**2 - 63)')
            
            
            
            if NORPH(data.decode(),'mngtrpail','abs(x**3 - 3*x**2 - 63)').find('checksum:') == -1:
                conn.send(NORPH(data.decode(),'mngtrpail','abs(x**3 - 3*x**2 - 63)').encode())
                print('sending again:'+ data.decode())
                
            else:
                outp=NORPH(data.decode(),'mngtrpail','abs(x**3 - 3*x**2 - 63)')
                outp=outp[:len(outp)-2]
                msg_array.append(outp)
                print('logging')
                

    
handler.add(M)

x,y = pygame.mouse.get_pos()


threading.Thread(target=coll2).start()


while 1:
    
    

    
    
    for event in pygame.event.get():
        handler.handle_event(event,x,y)
        x,y = pygame.mouse.get_pos()
        
    handler.display(dis)
    
    pygame.display.flip()
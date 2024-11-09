import pygame
from pgui import *
from norpher import NORPH
import socket
import _thread
import random

def create_checksum(num):
    a = random.randrange(1,num//2)
    return f'{num-a}+{a}={num}'

def receive(connection:socket.socket,key,eq):
    data = connection.recv(1024)
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
        return ''

def send(data:str,connection:socket.socket,key,eq):
    data+=f'checksum:{create_checksum(random.randrange(100,10000))}'
    encrypted_data = NORPH(data, key,eq)
    connection.send(encrypted_data.encode())
    other_encrypt = connection.recv(1024).decode()
    decrypted_this_side = NORPH(str(other_encrypt),key,eq)
    connection.send(decrypted_this_side.encode())

def client_program():
     host = input("What is the host name?")  # as both code is running on same pc
     port = int(input("What is the server's port?"))  # socket server port number



     client_socket = socket.socket()  # instantiate
     client_socket.connect((host, port))  # connect to the server

     message = input(" -> ")  # take input
     

     while message.lower().strip() != 'bye':
          send(message,client_socket,'mngtrpail','abs(x**3 - 3*x**2 + 63)')
          data = receive(client_socket,'mngtrpail','abs(x**3 - 3*x**2 + 63)')  # receive response
          


          print('boxoserv: ' + data)  # show in terminal
          print(' ')
          message = input(" -> ")  # again take input
          print(' ')

     client_socket.close()  # close the connection


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

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server



handler=Handler()




def s():
    inp_opts = handler.collate_textinput_inputs()
    
    mes = inp_opts.get('mesg')
    print("SENDING " + mes)
    if mes:
        if HOSTING:
            send(mes,conn,'boxo','tan(x**2)')
        else:
            send(mes,client_socket,'mngtrpail','abs(x**3 - 3*x**2 - 63)')
    
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
    if HOSTING:
        data,b = receive(conn, 'boxo','tan(x**2)')
    else:
        data,b = receive(client_socket, 'mngtrpail','abs(x**3 - 3*x**2 - 63)')

    

    print(data)

def collect():
    global msg_array
    if HOSTING:
        while True:
            data = receive(conn, 'boxo','tan(x**2)')
            print(data)
            msg_array.append(data)
            
            if len(msg_array) > 10:
                msg_array = msg_array[:10]
            
            c2 = [None]*(10-len(msg_array)) if len(msg_array) < 10 else []
            
            c2.extend(
                [
                    Text(
                        [0,0],
                        msg_array[i],
                        TextType.h3
                    ) 
                    for i in range(len(msg_array))
                    
                ]
            )
            c2.append(USE)
            M.content = [
                DisplayRows(c2)
            ]
            handler.GUIobjs_array[0]=M
            handler.display(dis)
            
    else:
        while True:
            data = receive(client_socket, 'mngtrpail','abs(x**3 - 3*x**2 - 63)')
            print(data)
            msg_array.append(data)

            if len(msg_array) > 10:
                msg_array = msg_array[:10]
            
            c2 = [None]*(10-len(msg_array)) if len(msg_array) < 10 else []
            
            c2.extend(
                [
                    Text(
                        [0,0],
                        msg_array[i],
                        TextType.h3
                    ) 
                    for i in range(len(msg_array))
                    
                ]
            )
            c2.append(USE)
            M.content = [
                DisplayRows(c2)
            ]
            handler.GUIobjs_array[0]=M
            handler.display(dis)
    
handler.add(M)

x,y = pygame.mouse.get_pos()


    

while 1:
    
    if HOSTING:
        
    
    
    
    
    for event in pygame.event.get():
        handler.handle_event(event,x,y)
        x,y = pygame.mouse.get_pos()
        
    handler.display(dis)
    
    pygame.display.flip()
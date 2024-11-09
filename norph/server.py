import socket
from norpher import NORPH


def receive(connection:socket.socket,key,eq):
     data = connection.recv(1024)
     encrypted_data = NORPH(str(data.decode()),key,eq)
     connection.send(encrypted_data.encode())
     other_decrypt = connection.recv(1024).decode()
     raw = NORPH(str(other_decrypt),key,eq)
     return raw

def send(data:str,connection:socket.socket,key,eq):
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


if __name__ == '__main__':
     host_or_not = input("Are you hosting the server? ").lower()

     if host_or_not == 'yes' or host_or_not == 'y':
          try:
               server_program()
          except ConnectionResetError:
               print("Could not connect.")
     else:
          try:
               client_program()
          except ConnectionResetError:
               print("Could not connect.")
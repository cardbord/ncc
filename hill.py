import numpy as np


def keyc(key):
    keymat = [[0]*3 for n in range(3)]
    k = 0
    for i in range(3):
        for j in range(3):
            keymat[i][j] = ord(key[k]) % 65
            k+=1
    return keymat

def translate_letter(message_vector,key):
    
    ciphermat = [[0] for n in range(3)]
    for i in range(3):
        for j in range(1):
            ciphermat[i][j] = 0
            for x in range(3):
                ciphermat[i][j] += (key[i][x] * message_vector[x][j])
            ciphermat[i][j] = ciphermat[i][j] % 26
            
    return ciphermat

def encrypt(message,key):
    mesmat = [[0] for n in range(3)]
    keymat = keyc(key)
    
    for i in range(3):
        mesmat[i][0] = ord(message[i]) % 65
    
    key_translate = translate_letter(mesmat,keymat)
    ciphertext = ""
    for i in range(3):
        ciphertext+=chr(key_translate[i][0] + 65)
    
    return ciphertext

key = "ABCDEFGHIJ"

message = "helloguysimsocoolthisisahillcipher"

emessage = encrypt(message,key)
print(emessage)


def decrypt(ciphertext,key):
    mesmat = [[0] for n in range(3)]
    keymat = keyc(key)
    keymat = np.array(keymat)
    plaintext = ""
    keymat = np.linalg.inv(keymat)

    mesmat = np.array(mesmat)
    
    for char in range(0,len(ciphertext),2):
        
        for i in range(3):
            
            mesmat[i] = ord(char)-65
            
    
    
    plaintextmat = np.matmul(keymat,mesmat)
    
    

    
    for i in range(0,len(ciphertext)):
        plaintext += chr(ord(ciphertext[0])-65)

    
    return plaintext

print(decrypt(emessage,key))


def bruteforce(ciphertext):

    cipher_matrix = [[0,0,],
                     [0,0,]]
    for row in range(2):
        for val in range(2):
            for n in range(500):
                cipher_matrix[row][val] = n
                mat = np.array(cipher_matrix)
                print(mat)
                try:
                    a = np.linalg.inv(mat)
                    for x in a:
                        for val in x:
                            val%=26
                    
                    print(a)
                    for twochars in range(0,len(ciphertext),2):
                        column_vec = [[ord(ciphertext[twochars])%65],[ord(ciphertext[twochars])%65]]
                        res = np.dot(a,column_vec)
                except np.linalg.LinAlgError:
                    pass




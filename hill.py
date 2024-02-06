import numpy as np


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

bruteforce("AABBCCDDEEFFGG")
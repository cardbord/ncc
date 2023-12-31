from string import ascii_lowercase
from PyDictionary import PyDictionary
from time import sleep
from math import gcd

def inverse_a(x,m):
    possible_a = [a for a in range(1,27) if gcd(a,26)==1]
    for i in possible_a:
        if (x*i)%m==1:
                return i
    return 0


def find_as_dict(text): #will implement in decoded_parser.py later, this could be really handy for checking solutions
                pdict = PyDictionary()
                new_ss = remove_punc(text)
                wcount = 0
                for word in new_ss.split(' '):
                    
                    if pdict.meaning(word,True) != None:
                        wcount+=1
                if wcount >= len(new_ss.split(' '))//2:
                    print('POSSIBILIY')
                    sleep(0.5)


def remove_punc(text):
    punc = ['.',';',':',',','-','/','?','#']
    for p in punc:
        text = text.replace(p,'')
    return text

def convert_from_affine(text):
    text = text.lower()
    text_arr = []
    
    de = ascii_lowercase
    possible_a = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    punc = [' ','.',';',':',',','-','/','?','#',"'",'"','’','(',')','!']
    for a in possible_a:
        for b in range(1,27):
            if inverse_a(a,26) != 0:
                new_str = ''
                for char in text:
                    
                    if not char in punc:
                        
                        index = de.index(char)
                        
                        
                        value = (inverse_a(a,26)*(index-b))%26
                        
                        new_str+=de[value]
                    else:
                        new_str+=char
                text_arr.append(f'{a},{b} ')
                text_arr.append(new_str+'\n')
                
            else:
                pass
    if len(text_arr) > 0:
        
        with open(f'{text[:3]}.decoded','w') as writable:
            writable.writelines(text_arr)
            print(f'{writable.name} written.')
                   
            
            

def convert_affine_ab(text,a,b):
    text=text.lower()
    new_str = ''
    de = ascii_lowercase
    punc = [' ','.',';',':',',','-','/','?','#',"'",'"','’']
    for char in text:
        
        if not char in punc:
            
            index = de.index(char)
            value = (inverse_a(a,26)*(index-b))%26
            new_str+=de[value]
        else:
            new_str+=char
            
        
    print(new_str)
    print(' ')

convert_from_affine(input('ciphertext (please use a single line) >>>'))

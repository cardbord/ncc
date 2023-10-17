from string import ascii_lowercase
from PyDictionary import PyDictionary
from time import sleep
def remove_punc(text):
    punc = ['.',';',':',',','-','/','?','#']
    for p in punc:
        text = text.replace(p,'')
    return text

def convert_from_affine(text):
    pdict = PyDictionary()
    de = ascii_lowercase
    possible_a = [1,3,5,7,9,11,13,15,17,19,21,23,25]
    punc = [' ','.',';',':',',','-','/','?','#']
    for a in possible_a:
        for b in range(1,27):
            new_str = ''
            for char in text:
                if char not in punc:
                    index = de.index(char)
                    value = (a*(index-b))%26
                    new_str+=de[value]
                else:
                    new_str+char
            print(new_str)
            new_ss = remove_punc(new_str)
            wcount = 0
            for word in new_ss.split(' '):
                
                if pdict.meaning(word,True) != None:
                    wcount+=1
            if wcount >= len(new_ss.split(' '))//2:
                print('POSSIBILIY')
                sleep(0.5)


convert_from_affine('xn')
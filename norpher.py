from math import *
import pyperclip

def keycircle(key,len_text):
    circled_key = ""
    if len_text < len(key):
        return key[:len_text].lower()
    for i in range(0,len_text,len(key)):
        circled_key+=key
    if len(circled_key) > len_text:
        circled_key = circled_key[:len_text]
        print(len(circled_key),len_text)
    return circled_key.lower()

print('\n')
text = input("text>>>")
if text=='':
    text=pyperclip.paste()
key = input("key>>>")

eq = input("polynomial (in terms of 'x')>>>")
if eq != '':
    adV = []
    for _ in range(len(text)):
        v = eval(eq.replace('x',str(_)))
        _v = (floor(100*v) if isinstance(v,float) else v)
        _v = bin(_v).replace('0b','')
        if len(_v) > 7:
            _v = _v[:7]
        adV.append(_v)

key = keycircle(key,len(text))

print(text,key)

aT = [bin(ord(c)).replace('0b','') for c in list(text)]
aK = [(bin(ord(c)).replace('0b',''))[::-1] for c in list(key)]

if eq != '':
    f=int(aK[len(aK)-1],2)
    for val in range(len(aK)):
        f = -int(aK[len(aK)-1-val]) * f
        print(f)
        if val % 2 == 0:
            sn = bin(abs(int(aK[val],2) + int(adV[val],2) + f)).replace('0b','')
        else:
            sn = bin(abs(int(aK[val],2) * (int(adV[val],2) + f))).replace('0b','')
        aK[val] = sn[len(sn)-7:]

for sW in range(len(aT)):
    if len(aT[sW]) < 7:
        aT[sW] = ''.join(['0' for _ in range((7-len(aT[sW])))]) + aT[sW]
        
for sW in range(len(aK)):
    if len(aK[sW]) < 7:
        aK[sW] = ''.join(['0' for _ in range((7-len(aK[sW])))]) + aK[sW]
        

cT = []
for n in range(len(aT)):
    s = aT[n]
    k = aK[n]
    indT = ''
    if len(s) > len(k):
        print(s,k, text[n], key[n])
    for char in range(len(s)):
        
        if s[char] != k[char]: #XOR gate (triggers if not 00, 11)
            indT+='1'
        else:
            indT+='0'
    cT.append(indT)
    

print(aT,aK)
print(' ')
print(cT)

for char in cT:
    f = int(char, 2)
    bA = f.to_bytes().decode()
    print(bA,end='')

kl = ''.join([int(a,2).to_bytes().decode() for a in cT])
pyperclip.copy(kl)
print('\n')
print(kl)
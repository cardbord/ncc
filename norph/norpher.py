from math import *
import pyperclip, base64, sys
from utils import add_b64, conv_b64, keycircle
    
def NORPH(text:str,key:str,eq:str) -> str:
    _temp = add_b64(text)
    _temp = _temp.encode('ascii')
    doNOTRETURNb64=False
    try:
        
        if base64.b64encode(base64.b64decode(_temp)) == _temp: #isbase64
            text=conv_b64(text)
            doNOTRETURNb64 = True
    except:
        pass



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

    

    bT = [bin(ord(c)).replace('0b','') for c in list(text)]
    bK = [(bin(ord(c)).replace('0b',''))[::-1] for c in list(key)]

    if eq != '':
        f=int(bK[len(bK)-1],2)
        for val in range(len(bK)):
            f = -int(bK[len(bK)-1-val]) * (ceil(f/10) + int(adV[val],2)) 
            
            if val % 2 == 0:
                sn = bin(abs(int(bK[val],2) + int(adV[val],2) + f)).replace('0b','')
            else:
                sn = bin(abs(int(bK[val],2) * (int(adV[val],2) + f))).replace('0b','')
            bK[val] = sn[len(sn)-7:]

    for sW in range(len(bT)):
        if len(bT[sW]) < 7:
            bT[sW] = ''.join(['0' for _ in range((7-len(bT[sW])))]) + bT[sW]
            
    for sW in range(len(bK)):
        if len(bK[sW]) < 7:
            bK[sW] = ''.join(['0' for _ in range((7-len(bK[sW])))]) + bK[sW]
            

    cT = []
    for n in range(len(bT)):
        s = bT[n]
        k = bK[n]
        indT = ''
        if len(s) > len(k):
            print(s,k, text[n], key[n])
        for char in range(len(s)):
            
            if s[char] != k[char]: #XOR gate (triggers if not 00, 11)
                indT+='1'
            else:
                indT+='0'
        cT.append(indT)
        

    kl = ''.join([int(a,2).to_bytes().decode() for a in cT])

    
    



    if doNOTRETURNb64 == False:
        kl=kl.encode('ascii')
        kl=base64.b64encode(kl)
        kl=kl.decode('ascii')
        kl=kl.replace('=','')

    return kl


if __name__ == '__main__':
    if len(sys.argv) < 3:

        print('\n')
        text = input("text>>>")


        if text=='':
            text=pyperclip.paste()
        key = input("key>>>")
        eq = input("polynomial (in terms of 'x')>>>")
    else:
        text = sys.argv[1]
        key = sys.argv[2]
        eq = sys.argv[3] if len(sys.argv) > 4 else ''


    kl = NORPH(text,key,eq)
    print(kl)
    pyperclip.copy(kl)
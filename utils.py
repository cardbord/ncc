import base64

def add_b64(text:str): #to add padding back to trimmed base64
    if len(text) % 4 != 0:
        nexthighest = (len(text)//4 * 4) + 4
        text = text + '='*(nexthighest-len(text))
        return text
    else:
        return text
    
def conv_b64(text:str): #to convert base64 back to plaintext
    if text.isprintable() or text.isalpha() or text.isnumeric(): #is b64
        text=add_b64(text)
    
        t=text.encode('ascii')
        deT = base64.b64decode(t)
        t=deT.decode('ascii')
        return t

    else:
        return text
    
def keycircle(key,len_text):
    circled_key = ""
    if len_text < len(key):
        return key[:len_text].lower()
    for i in range(0,len_text,len(key)):
        circled_key+=key
    if len(circled_key) > len_text:
        circled_key = circled_key[:len_text]
    return circled_key.lower()
alpha = "abcdefghijklmnopqrstuvwxyz" #we alpha instead, since %26 returns the alphabetical position, not ASCII (i'm stupid!)

def keycircle(key,len_text):
    circled_key = ""
    if len_text < len(key):
        return key[:len_text].upper()
    for i in range(0,len_text,len(key)):
        circled_key+=key
    if len(circled_key) > len_text:
        circled_key = circled_key[:len_text]
        print(len(circled_key),len_text)
    return circled_key.upper()

def b(key,position):
   return key[position]


#so we convert to ascii first?
def encrypt(text,key):
    
    text=text.upper()
    ciphertext=""
    key = keycircle(key,len(text))
    print(text)
    for letter in range(len(text)):
        
        ciphertext+=alpha[(ord(text[letter]) + ord(key[letter])) %26]
        
    return ciphertext.upper()

def decrypt(ciphertext,key):
    plaintext=""
    key = keycircle(key,len(ciphertext))
    for letter in range(len(ciphertext)):
        toDecode = alpha[(ord(ciphertext[letter]) - (ord(key[letter])) % 26) % 26]
        plaintext+=(toDecode)
    return plaintext

text_to_encode = "boxociphersuperool"

print(keycircle("boxo",len(text_to_encode)))
a = encrypt("boxociphersupercool","boxo")
print(a)

print(decrypt(a,"boxo"))

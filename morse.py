morse_alpha_dict = {"a": ".-" , "b": "...-" , "c": "-.-." , "d": "-.." , "e": "." , "f": "..-." , "g": "--." , "h": "...." , "i": ".." , "j": ".---" , "k": "-.-" , "l": ".-.." , "m": "--" , "n": "-." , "o": "---" , "p": ".--." , "q": "--.-" , "r": ".-." , "s": "..." , "t": "-" , "u": "..-", "v": "...-" , "w": ".--" , "x": "-..-" , "y": "-.--" , "z": "--.."}

def find_in_dict(mval):
    a = [a for a in morse_alpha_dict]
    for i in a:
        if morse_alpha_dict[i] == mval:
            return i
    

def encode(plaintext:str):
    morse_text = ""
    for char in list(plaintext):
        if char == " ":
            morse_text+="/"
        else:
            morse_text+=morse_alpha_dict[char]  + " "
    return morse_text
    
def decode(morse_text:str):
    plaintext = ""
    for char_group in morse_text.split("/"):
        for char in char_group.split(" "):
            plaintext+=find_in_dict(char)

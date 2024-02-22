morse_alpha_dict = {

                    #ALPHABET
                    "a": ".-" , "b": "...-" , "c": "-.-." , "d": "-.." , "e": "." , "f": "..-." , "g": "--." , "h": "...." , "i": ".." , "j": ".---" , "k": "-.-" , "l": ".-.." , "m": "--" , "n": "-." , "o": "---" , "p": ".--." , "q": "--.-" , "r": ".-." , "s": "..." , "t": "-" , "u": "..-", "v": "...-" , "w": ".--" , "x": "-..-" , "y": "-.--" , "z": "--..",
                    
                    #NUMBERS
                    '0': '-----',  '1': '.----',  '2': '..---',
                    '3': '...--',  '4': '....-',  '5': '.....',
                    '6': '-....',  '7': '--...',  '8': '---..',
                    '9': '----.',
                    
                    #SYMBOLS
                    ', ': '--..--',
                    '?': '..--..',
                    '(': '-.--.',
                    ')': '-.--.-',                
                    '=': '-...-',
                    '+':'.-.-.',
                    '!':'-.-.--',
                    ':':'---...',
                    ';':'-.-.-.'
                    }
alpha_morse_dict = {value:key for key,value in morse_alpha_dict.items()}


    

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
            plaintext+=alpha_morse_dict[char] + " "

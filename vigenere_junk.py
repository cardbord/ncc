from vigenere import encrypt, decrypt
from pynput import keyboard
from pyperclip import paste
from time import sleep
v_key = input("ENter key>>>")


ctrl = keyboard.Controller()
halt_spaces = False
def repEngVigenere(key:keyboard.Key):
    if isinstance(key,keyboard.KeyCode) and key.char == "`":
        ctrl.tap(keyboard.Key.backspace)
        ctrl.tap(keyboard.Key.home)
        ctrl.press(keyboard.Key.shift_l)
        ctrl.tap(keyboard.Key.end)    
        ctrl.release(keyboard.Key.shift_l)
        ctrl.press(keyboard.Key.ctrl)
        ctrl.tap("x")
        ctrl.release(keyboard.Key.ctrl)
        sleep(0.2)
        text = paste()
    
        plaintext = decrypt(text.replace(" ","").upper(),v_key)
        ctrl.type(plaintext)
    
    elif key == keyboard.Key.delete:
        ctrl.tap(keyboard.Key.home)
        ctrl.press(keyboard.Key.shift_l)
        ctrl.tap(keyboard.Key.end)    
        ctrl.release(keyboard.Key.shift_l)
        ctrl.press(keyboard.Key.ctrl)
        ctrl.tap("x")
        ctrl.release(keyboard.Key.ctrl)
        sleep(0.2)
        text = paste()
        
        ciphertext = encrypt(text.replace(" ","").upper(),v_key)
        ctrl.type(ciphertext.lower())
        
        
    

with keyboard.Listener(on_press=repEngVigenere) as listen:
    listen.join()
    
    

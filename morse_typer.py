from morse import morse_alpha_dict
from pynput import keyboard

ctrl = keyboard.Controller()
halt_spaces = False
def repEngMorse(key:keyboard.KeyCode):
    
    global halt_spaces
    if isinstance(key,keyboard.KeyCode) and key.char.isalpha():
        halt_spaces = True
        ctrl.tap(keyboard.Key.backspace)
        ciphertext = morse_alpha_dict.get(key.char.lower())
        ctrl.type(ciphertext+" ")
        halt_spaces = False
    if isinstance(key,keyboard.Key) and key == keyboard.Key.space:

        if not halt_spaces:
            ctrl.type("/")
    

with keyboard.Listener(on_press=repEngMorse) as listen:
    listen.join() 
from morse import encode
from pynput import keyboard

ctrl = keyboard.Controller()
def repEngMorse(key:keyboard.KeyCode):
    try:
        ciphertext = encode(key.char)
        ctrl.tap(keyboard.Key.backspace)
        ctrl.type(ciphertext)
    except:
        pass

with keyboard.Listener(on_press=repEngMorse) as listen:
    listen.join() 
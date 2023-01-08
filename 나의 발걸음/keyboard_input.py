from pynput.keyboard import Listener, Key

keys = ''

def on_press(key):
    global keys
    
    if key == Key.enter:
        print(keys)
        keys = ''
    else:
        keys += str(key).replace("'", "")
    
with Listener(on_press=on_press) as Listener:
    Listener.join()

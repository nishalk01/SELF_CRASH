from pynput import keyboard
from pynput.keyboard import Key, Controller
from get_frame import get_frames
import numpy as np
training_data=[]
def do_something(a):
    output=[0,0,0]
    img=get_frames()
    print(img)
    if(a=='a'):
        output[0]=1
    elif(a=='w'):
        output[1]=1
    else:
        output[2]=1
    print("===============================================")
    print(output)
    print("===============================================")
    training_data.append([img,output])
    if(len(training_data)%10==0):
    	print("saving_data[]")
    	np.save("d.npy",training_data)
    	print(len(training_data))


current = set()


def on_press(key):
    keys=[]
    if(key==keyboard.KeyCode(char='a')):
        keys='a'
        do_something(keys)
    if(key==keyboard.KeyCode(char='w')):
        keys='w'
        do_something(keys)
    if(key==keyboard.KeyCode(char='d')):
       keys='d'
       do_something(keys)
    current.add(key)
       

def on_release(key):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

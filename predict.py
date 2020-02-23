from PIL import ImageGrab
import cv2
import numpy as np
import tensorflow as tf
from pynput.keyboard import Key, Controller
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller
keyboard = Controller()
print("[]pass")
json_file = open("model_try_car30sc.json", 'r')
loaded_model_json = json_file.read()
json_file.close()
model =tf.keras.models.model_from_json(loaded_model_json)
model.load_weights("model_try_car30sc.h5")
def left():
    keyboard.press('a')
    time.sleep(0.01)
    keyboard.release('a')
    print("left")
def right():
    keyboard.press('d')
    time.sleep(0.01)
    keyboard.release('d')
    print("right")
def brake():
    keyboard.press('s')
    keyboard.release('s')
    print("brake")
def forward():
    keyboard.press('w')
    time.sleep(0.4)
    keyboard.release('w')
    print("forward ")
while(True):
    im = ImageGrab.grab((0,40,800,640))
    im=np.array(im)
    im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    img=cv2.resize(im,(80,60))
    imag=img.reshape(-1,80,60,1)
    wat=model.predict(imag)
    #print(wat)
    moves = list(np.around(wat))
    print(moves)
    print(moves[0][2])
    #break
    #val=moves[0]
   # print(val)
    if(moves[0][0]==1):
       left()
       forward()
       
       print("==========================")
    elif(moves[0][1]==1):
        forward()
       # time.sleep(1)
    elif(moves[0][2]==1):
        right()
        forward()
    #time.sleep(1)
    elif(moves[0][3]==1):
        pass
    else:
        pass
        #print("apuji")
    cv2.imshow("s",im)
    if cv2.waitKey(25)&0xFF==ord('q'):
                 cv2.destroyAllWindows()
                 break 

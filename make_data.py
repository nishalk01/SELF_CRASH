import numpy as np
import cv2
from get_keys import key_check 
from get_frame import get_frames
training_data=[]
def key_data(keys):
  output=[0,0,0]
  if 'A' in keys:
            output[0]=1
  elif 'W' in keys:
           output[1]=1
  elif 'D' in keys:
           output[2]=1
  #print(output)
  return output
          
def data():
 while (True):
   img=get_frames()
   keys=key_check()
   outkey=key_data(keys)
   training_data.append([img,outkey])
   if(len(training_data)%10==0):
             np.save("one-file.npy",training_data)
             print(len(training_data))
             print("[]Saving....")

data()  
   
         





# we can automate the famous google dinosaur game using this code.
import pyautogui
from PIL import Image,ImageGrab
import time
from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def iscollide(data):
    for i in range(670,750):
        for j in range(300,362):
            if data[i,j]<100:
                return True
    return False

if __name__=="__main__":
    print("Dino game to start in 3 seconds....")
    time.sleep(3)
    hit("up")
    print("welcome player")
    while True:
        image=ImageGrab.grab().convert('L')        
        data=image.load()
        if iscollide(data):
            hit("up")
        # # print(asarray(image))
        # for i in range(670,750):
        #     for j in range(300,362):
        #         data[i,j] = 0
        # image.show()
        # break


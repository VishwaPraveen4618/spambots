import pyautogui
import time
f=open("script 2.txt",'r')
time.sleep(5)
for word in f:
    pyautogui.typewrite(word,interval=0.000001)
                
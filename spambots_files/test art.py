import pyautogui,time
time.sleep(2)

pyautogui.click(293,65,duration=1)
pyautogui.click(762,59,duration=0.5)
pyautogui.moveTo(760,265,duration=1)
pyautogui.drag(100,100,duration=1)
pyautogui.hotkey("alt","shift")
pyautogui.hotkey("alt","shift")
f=open("sinhala.txt",'r')
for word in f:
              pyautogui.typewrite(word)
pyautogui.click(762,221,duration=0.5)

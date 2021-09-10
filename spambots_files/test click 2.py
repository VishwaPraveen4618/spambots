import pyautogui,time
a = pyautogui.locateOnScreen('windows button.png',confidence=0.9)
b=pyautogui.center(a)
x,y=b
pyautogui.click(x, y)
time.sleep(0.5)
pyautogui.write('paint',0.5)
a = pyautogui.locateOnScreen('paint.png',confidence=0.9)
b=pyautogui.center(a)
x,y=b
pyautogui.click(x, y)
a = pyautogui.locateOnScreen('close.png',confidence=0.9)
b=pyautogui.center(a)
x,y=b
pyautogui.click(x, y)
a = pyautogui.locateOnScreen('minimize.png',confidence=0.9)
b=pyautogui.center(a)
x,y=b
pyautogui.click(x, y)

import pyautogui
a = pyautogui.locateOnScreen("windows button.png",confidence=0.9)
b=pyautogui.center(a)
x,y=b
pyautogui.click(x, y,duration=2)

h = pyautogui.locateOnScreen("minimize.png",confidence=0.9)
j=pyautogui.center(h)
n,m=j
pyautogui.click(n, m,duration=2)


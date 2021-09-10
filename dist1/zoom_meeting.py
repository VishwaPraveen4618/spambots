import pyautogui,time
def type(id):
    pyautogui.typewrite(id)
def click(picture):
    a = pyautogui.locateOnScreen(picture,confidence=0.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    b=pyautogui.center(a)  
    x,y=b
    pyautogui.click(x, y)
def sleep(seconds):
    time.sleep(seconds)
input1=pyautogui.prompt("Enter meeting's id","Zoom meeting 🎦🎦")
input2=pyautogui.prompt("Enter meeting's password","Zoom meeting 🎦🎦")
input3=int(pyautogui.prompt("Enter first meeting's duration","Zoom meeting🎦🎦"))

click("zoom.png")
sleep(3)

click("join.png")
sleep(4)

click("id.png")
type(input1)
sleep(1)

click("join 2.png")
sleep(4)

click("pass.png")
type(input2)
sleep(1)

click("join 3.png")

#1st session
sleep(input3*60)

#2nd session
click("ok.png")
sleep(2)

click("join.png")
sleep(4)

click("id.png")
type(input1)
sleep(1)

click("join 2.png")
sleep(4)

click("pass.png")
type(input2)
sleep(1)

click("join 3.png")

sleep(2460)

#3rd session

click("ok.png")
sleep(2)

click("join.png")
sleep(4)

click("id.png")
type(input1)
sleep(1)

click("join 2.png")
sleep(4)

click("pass.png")
type(input2)
sleep(1)

click("join 3.png")

sleep(2460)

click("ok.png")

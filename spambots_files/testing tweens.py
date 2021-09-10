import pyautogui
a=pyautogui.confirm("love","hi",["A","B","C"])
if a=="A":
          print("well done")
elif a=="B":
           print("good")

else:
     print("Not good")


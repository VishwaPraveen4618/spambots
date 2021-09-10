import pyautogui,time
marks=0
start=pyautogui.alert([" Hi   welcome   to   friendship   examination   !  ,  Are  you  want  to  enter  to  this ?"],'Friendship examination',"Start")
input=pyautogui.prompt("Enter your name please!","Friendship examination")
first_quest=pyautogui.confirm(f'Hi {input}, What is my name ? -- |  1.Vishwa  |  2.Yasitha  |  3.Supun  |  4.Navitha  |',"First question",['1','2','3','4'])
if first_quest=="1":
    pyautogui.alert("🔰⭐⭐✅ You are correct ! 🔰⭐⭐✅","First question answer","Ok")
    marks+=1
    
    
elif first_quest=="2":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 1.Vishwa 👎❌❌❎","First question answer","Ok")
elif first_quest=="3":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 1.Vishwa 👎❌❌❎","First question answer","Ok")
elif first_quest=="4":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 1.Vishwa 👎❌❌❎","First question answer","Ok")   
else: 
    time.sleep(0.5)
        

second_quest=pyautogui.confirm("What is my age ? -- |  1.14  |  2.15  |  3.16  |  4.17  |","Second question",[1,2,3,4])
if second_quest=="1":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 3.16 👎❌❌❎","Second question answer","Ok")
elif second_quest=="2":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 3.16 👎❌❌❎","Second question answer","Ok")
elif second_quest=="3":
    pyautogui.alert("🔰⭐⭐✅ You are correct ! 🔰⭐⭐✅","Second question answer","Ok")
    marks+=1
elif second_quest=="4":
     pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 3.16 👎❌❌❎","Second question answer","Ok")    
else:
    time.sleep(0.5)


third_quest=pyautogui.confirm("What is my age ? -- |  1.14  |  2.15  |  3.16  |  4.17  |","Third question",[1,2,3,4])
if third_quest=="1":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 3.16 👎❌❌❎","Third question answer","Ok")
elif third_quest=="2":
    pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 3.16 👎❌❌❎","Third question answer","Ok")
elif third_quest=="3":
    pyautogui.alert("🔰⭐⭐✅ You are correct ! 🔰⭐⭐✅","Third question answer","Ok")
    marks+=1
elif third_quest=="4":
     pyautogui.alert("👎❌❌❎ You are incorrect.Correct answer is 3.16 👎❌❌❎","Third question answer","Ok")    
else:
    time.sleep(0.5) 
pyautogui.confirm(f"Thank you ! ,Your got {marks} marks.","Result")     

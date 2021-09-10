msg=input("Enter the text that you need to find length: ")
a=len(msg)
print(f'Length of your text is {a} words.')

msg=input("Enter the text that you need in upper case: ")
print(f'Your Capitalized text is {msg.upper()}.')

msg=input("Enter the text that you need in lower case: ")
print(f'Your lower cased text is {msg.lower()}.')

msg=input("Enter the text that you want to make first letter of each word capitalized and others simpled: ")
print(f'Your first letter capitalized text is {msg.title()}.')

msg=input("Enter the text that you need to find a text already included in it: ")
find=input("Enter your wanted text in above text: ")
print(f'Your wanted texts position is {msg.find(find)}.')

msg=input("Enter the text that you want to replace a word in it: ")
replace=input("Enter the word that you want to replace from above text: ")
new=input("Enter your new word: ")
print(f'Your new text is "{msg.replace(replace,new)}".')

msg=input("Enter the text that you want to check whether a word which was typed later is included in that text or not:  ")
later_text=input("Enter the word that you want to check whether it included in above text or not: ")
print(f'Status of inclusion: "{later_text in msg}"')








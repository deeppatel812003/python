Letter = '''Dear <|Name|>
You are selected!
Have agreat day!
Thanks
Date: <|Date|>'''
name = input("Enter your name\n")
date = input("Enter Date\n")
Letter= Letter.replace("<|Name|>",name)
Letter= Letter.replace("<|Date|>",date)
print(Letter)


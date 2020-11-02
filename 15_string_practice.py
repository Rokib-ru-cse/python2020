name = input("enter ur name\n")
date = input("enter date\n")



letter = '''Dear <|NAME|>,
you are selected!

Date: <|DATE|>  
'''
letter = letter.replace('<|NAME|>',name)
letter = letter.replace('<|DATE|>',date)



print(letter)


st = '''Dear Harry, \n\tthis python course is nice ! \nthanks!''' 
print(st)
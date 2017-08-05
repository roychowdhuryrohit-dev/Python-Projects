# I will use Regular Expression to detect the expressions in this project

import re

if __name__  ==  '__main__':
    print("We will detect the email address in any line:")
    line  =  input("Enter the line:")
    res  =  re.findall("[^ ]+@.+?\.com",line)
    print('the Detected emails are :' ,res)


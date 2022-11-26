#Generate password project
import random
import string
'''The password consist of 4 parts  : lower letters with 30% 
capital letters with 30%  , digits with 30% , punctuate with 10%'''
l_case = list(string.ascii_lowercase)
u_case = list(string.ascii_uppercase)
d = list(string.digits)
punc = list(string.punctuation)
random.shuffle(l_case)
random.shuffle(u_case)
random.shuffle(d)
random.shuffle(punc)

'''your password must be at least 6 characters'''
while True :
   try: 
    charc_num = int(input("Enter the number of characters of your password : "))
    if charc_num < 6 :
        print("Try again your password must be at least 6 caracters !")
    elif charc_num > 20 :
        print("Try again your password is too long make it at most 20 !")   
    else :
        break 
   except:
    print("you have to enter an integer number for your characters ")    
part1 =round(0.3*charc_num) 
part2 =round(0.1*charc_num)
password =[]
for i in range(part1) :
    password.append(l_case[i])
    password.append(u_case[i])
    password.append(d[i])
for i in range(part2) :
    password.append(punc[i])  
random.shuffle(password)  #shuffling the characters to increase its difficulty
password = ''.join(password)  
print(f"We generate a strong password for you  : {password}  ")  



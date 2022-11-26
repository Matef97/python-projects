#ِATM
import time
users = [{"name":"Ahmed","balance":4400,"code":1234},
{"name":"Mostafa","balance":44000,"code":1567},
{"name":"Sayed","balance":5786,"code":5789},
{"name":"Andrew","balance":4578,"code":1444},
{"name":"Alaa","balance":4698123,"code":9645},
{"name":"Nancy","balance":2557,"code":1762},
{"name":"Aya","balance":44,"code":3333}]

current_user = {}
pincode = 0
def load():
    for i in range(1,5) :
      print('loading.......'+i*'.')
      time.sleep(1)

def init_screen():
    global current_user
    load()
    print('           ***********************             ')
    print('            Welcome to Tefa Bank ATM            ')
    print('           ***********************             ')
    print('        Please Enter your 4 digit Pin Code             ')
    pincode = int(input( ))
    
        
    for user in users :
        if user['code'] == pincode :
            current_user = user
            print('Welcome  ',user['name'])     
        

def select_screen():
  if current_user != {} :  
   print(" 1- cash withdrawal           2- balance inquiry   ")
   print(" 3- transfer                  4- bill payment   ")
   print(" 5- settings                  6- donate  ")
   print("please choose the number of your transaction from 1-6 ")
   num = int(input())
   while True :
    if num == 1 :
     cashwithdrawal()
     break
    elif num == 2 :
     balance_inquiry() 
     break
    elif num == 3 :
     transfer()
     break
    elif num == 4 : 
     bill_payment()
     break
    elif num == 5 :
     setting()
     break
    elif num == 6 : 
     donate()  
     break
    else:
     print("you entered a wrong number ")   
     print("please choose the number of your transaton from 1-6 ")
     num = int(input())


def cashwithdrawal():
    amount = int(input('Please enter the amount that you want : '))
    if amount < current_user["balance"] :
        current_user["balance"] = current_user["balance"]- amount
        print('your process is done perfectly')
        final = input('Do you want another process ? y or n : ').lower()
        if final == 'y' :
            select_screen()
        else :
            print('Thank you for using Tefa ATM Services ') 
    else:
        print("Sorry your current balance isn't enough to witdrawl this amount ")
        time.sleep(3)
        select_screen()           

def balance_inquiry():
    print("your current balance is   ",current_user["balance"],"EGP")
    final = input('Do you want another process ? y or n : ').lower()
    if final == 'y' :
            select_screen()
    else :
            print('Thank you for using Tefa ATM Services ') 
def transfer():
    amount = int(input('Please enter the amount that you want to transfer : '))
    if amount < current_user["balance"] :
        current_user["balance"] = current_user["balance"]- amount
        print('your process is done perfectly')
        final = input('Do you want another process ? y or n : ').lower()
        if final == 'y' :
            select_screen()
        else :
            print('Thank you for using Tefa ATM Services ') 
    else:
        print("Sorry your current balance isn't enough to transfer this amount ")
        time.sleep(3)
        select_screen() 
def bill_payment():
    pass
def setting():
    pass
def donate():
    pass

init_screen()
select_screen()

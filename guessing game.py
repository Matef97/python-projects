#Gusseing game project
my_secret_word = "Tefa"
trial = 3
guess = ''
while guess!= my_secret_word :
    print(f"you have {trial} tries left")
    guess = input("Enter your guess : ")
    trial-=1
    if trial == 0 :
        print("you spent all of your tries\nGAME OVER")
        break
else :
    print("you got the correct guess\nYOU WIN")    



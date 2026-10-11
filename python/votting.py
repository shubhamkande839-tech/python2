age = int(input("Enter your age- "))
isVoterIDAvailable = bool(input("1 or 0:-"))

if(age>18 and isVoterIDAvailable==1):

    print("you are able to vote ")
else:
    if(age<18 and isVoterIDAvailable==False):
        print("you are not able to vote because you are underage")
    elif(age>18 and isVoterIDAvailable==False):
        print("you are not able to vote because you dont have voter id yet !!")
import random

user=0
com=0
loop =1 
while loop<5:       
    random_choice=random.randint(1,3)

    
    user_choice=int(input("Enter your choice:"))
    print(f" Computer choice:{random_choice}")


    if random_choice== user_choice:
            print("Good Job!!😮‍💨 Draw")
            continue

    elif random_choice==1 and user_choice==2:
            print("User wins🎉💃!!")
            user+=1

    elif random_choice==1 and user_choice==3:
            print("Computer Wins😅!!")
            com+=1

    elif random_choice==2 and user_choice==1:
            print("Computer Wins😅!!")
            com+=1 

    elif random_choice==2 and user_choice==3:
            print("User wins🎉💃!!")
            user+=1

    elif random_choice==3 and user_choice==1:
            print("User wins🎉💃!!")
            user+=1 

    elif random_choice==3 and user_choice==2:
            print("Computer Wins😅!!")
            com+=1

    else:
            print("Invalid number")
            continue
    loop+=1
print("")
if user>com:
    print(f"User won by {user} takes")
else:
    print(f"Computer won by {com} takes")

        



        







import random
choice=['stone','paper', 'scissor']
U,C=0,0


while True:
    user=input("Enter stone, paper or scissor: ").lower()
    if user == 'exit':
        break
    
    comp=random.choice(choice)
    print(f"You : {user}\t | \tcomputer : {comp}")
    
    if user == comp:
        print("It's a tie!")
    elif user == 'stone':
        if comp=='paper':
            print("YOU LOSE!!")
            C+=1
        else:
            print("YOU WIN!")
            U+=1

    elif user == 'paper':
        if comp=='stone':
            print("YOU WIN!")
            U+=1
        else:
            print("YOU LOSE!!")
            C+=1

    elif user == 'scissor':
        if comp=='paper':
            print("YOU WIN!")
            U+=1
        else:
            print("YOU LOSE!!")
            C+=1
    else:
        print("wrong input")
    print(f"""
            SCORECARD
    User = {U} \t Computer = {C}
          """)
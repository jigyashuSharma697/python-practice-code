"""
WORKFLOW OF PROJECT:
1- Input from user(Rock,Paper,Scissor)
2- Computer choice (Computer will choice randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B - Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C - Scissor 
Scissor - Scissor = Tie
Scissor - Rock = Rock tie
Scissor - Paper = Scissor win

"""

import random
itemList = ["Rock", "Paper", "Scissor"]

userChoice = input("Enter your move = Rock , Paper, Scissor = ")
compChoice = random.choice(itemList)

print(f"User choice = {userChoice}, Computer Choice = {compChoice}")

if userChoice == compChoice:
    print("Both chooese same: Match tie")
    
elif userChoice ==  "Rock":
    if compChoice == "Paper":
     print("Paper covers Rocks = Computer")
    
    else:
        print("Rock smashes Scissor = You win")
        
elif userChoice == "Paper":   
    if compChoice == "Scissor":
        print("Scissor cuts Paper, Computer win")
        
    else:
        print("Paper cover rock, You win")
        
elif userChoice == "Scissor":
    if compChoice == "Paper":
     print("Scissor cuts paper, You win")
     
else:
    print("Rock smashes scissor , Computer win")

     
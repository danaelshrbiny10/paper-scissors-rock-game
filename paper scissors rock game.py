import random
print("Welcome In My Game ...!")
print("If You Wanna Close The Game Write exit ...")

names = ["rock" , "paper" , "scissors"]

player = input("please enter your choice : ")

computer = random.choice(names)


if player == computer:
    print("The Output Is Same ,Please Try Again")

elif player > computer:
    print("player is win ...! ")


elif player < computer:
    print("computer is win ...! ")


while player == "exit":
        print("Closing The Game ...!")
        print("Thanks ....!")
        break

# output = "Your Choice is {} And Computer Choice is {}"
# print(output.format(player , computer))


#--------------------------------------------------------------------------------------

## Another Solution :
'''
import random
print("Welcome In My Game ...!")
print("If You Wanna Close The Game Write exit ...")

names = ["rock" , "paper" , "scissors"]

player = input("please enter your choice : ")

computer = random.choice(names)

class Game:
    def __init__(self):
        print("Welcome In My Game ...!")

    def Choices():
        if player == computer:
            print("The Output Is Same ,Please Try Again")

        elif player > computer:
            print("player is win ...! ")

        elif player < computer:
            print("computer is win ...! ")
    Choices()

    # output = "Your Choice is {} And Computer Choice is {}"

    # print(output.format(player , computer))

    def Exit():
        while player == "exit":
            print("Closing The Game ...!")
            print("Thanks ....!")
            break
    Exit()
'''
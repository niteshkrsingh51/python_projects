import random

#function to create a rangeList as per user inputs
def rangeList(starting_range,ending_range):
    res = []
    for i in range(starting_range,ending_range+1):
        res.append(i)
    return res

#taking user inputs for creating range
starting_range, ending_range = input("Enter the starting and ending range: ").split()
guessed_number = int(input("Enter The Your Guess Number: "))
chances = 7

#creating a range list as per given inputs
rangeList_1 = rangeList(int(starting_range),int(ending_range))

#creating a random number from the range list
random_number = random.choice(rangeList_1)

#guessing_game_algorithm
while(True):
    if chances != 0:
        if guessed_number == random_number:
            print("Congrats... You Guessed The Number Right")
            break
        else:
            if guessed_number in rangeList_1:
                if guessed_number > random_number:
                    print("Your Guess Is Higher Than The Number")
                    guessed_number_1 = int(input("Enter Again The Your Guess Number: "))
                    guessed_number = guessed_number_1
                    chances -= 1
                elif guessed_number < random_number:
                    print("Your Guess Is Lower Than The Number")
                    guessed_number_2 = int(input("Enter Again The Your Guess Number: "))
                    guessed_number = guessed_number_2
                    chances -= 1         
            else:
                print("Sorry... But The Number Entered Is Out Of Range. Try Again..!!")
                guessed_number_3 = int(input())
                guessed_number = guessed_number_3
                chances -= 1
    else:
        print("Sorry.. You Lost The Guessing Game As Number Of Chances Has Been Exhusted..!!")
        break

    




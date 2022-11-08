"""A number-guessing game."""
import random
# Put your code here
name = input("Howdy, what's your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
moreRounds = "y"
scores = []
def guessing():
    low = 1
    high = 100
    fix_number = random.randint(low, high)
    print(fix_number)
    count = 1
    guess_number = int(input("Your guess? "))
    while (guess_number != fix_number):
       #midpoint = int((low + high) / 2)
       if (guess_number > fix_number):
            #low = midpoint
            #print(low)
            print("Your guess is too high, try again.")
            count += 1
            guess_number = int(input("Your guess? "))        
       else:
            #high = midpoint
            #print(high)
            print("Your guess is too low, try again.")
            count += 1
            guess_number = int(input("Your guess? "))
    print(f"Well done, {name}! You found my number in {count} tries!")
    scores.append(count)
    moreRounds = input("Do you want to continue play? Y for yes and N for no ")
    return moreRounds
    
while moreRounds.lower() == "y":
    moreRounds = guessing()
if moreRounds.lower() == "n":
    print(scores)
    bestScore = min(scores)
    print(f"Congrats! Your best score is {bestScore} tries!")
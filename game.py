"""A number-guessing game."""
import random
# Put your code here
name = input("Howdy, what's your name? ")
print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
moreRounds = "y"
scores = []
maxCount = 5
def guessing():
    low = int(input("Choose your start number: "))
    high = int(input("Choose your end number: "))
    mynumber = random.randint(low, high)
    print(mynumber)
    count = 1
    guess_number = int(input("Your guess? "))
    guessed = True
    while (guess_number != mynumber):
       #midpoint = int((low + high) / 2)
        if (guess_number > mynumber):
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
        if count > maxCount:
            print("Too many tries")
            guessed = False
            break
    if guessed:
        print(f"Well done, {name}! You found my number in {count} tries!")
        scores.append(count)
    moreRounds = input("Do you want to continue play? Y for yes and N for no ")
    return moreRounds

    
while moreRounds.lower() == "y":
    moreRounds = guessing()
if moreRounds.lower() == "n":
    bestScore = min(scores)
    print(f"Congrats! Your best score is {bestScore} tries!")
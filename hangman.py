import random, os, time

listOfWords = ["taipei", "food", "weather", "traffic", "mountain", "buildings", "technology", "semiconductor", "elections"]

#The three variables below are to generate a (pseudo) random word from the list above
myWord = random.choice(listOfWords)
lettersChosen = []
counter = []
#print(myWord)

print()
print()

#Function to change the colour of the text on the screen
def changeColour(colour):
  if colour=="red":
    return ("\033[31m")
  elif colour=="white":
    return("\033[0m")
  elif colour=="blue":
    return("\033[0;34m")
  elif colour=="yellow":
    return("\033[1;33m")

#Intro to the game, which incorporates a few of the features of python I have learned about so far
title = f"{changeColour('red')}={changeColour('white')}={changeColour('blue')}={changeColour('yellow')}Zig's Hangman Game{changeColour('blue')}={changeColour('white')}={changeColour('red')}="
print(f"{title:^80}")
print(f"{changeColour('white')}")
print("""Hey Everyone,
      
This is the first game that I've completed using 🐍python🐍. 

I hope you can take the time to test it and see if it works. 

If you have any ideas for improvements or suggestions please reach out to me.

The game will start automatically in a few seconds.

Enjoy!!""")

#Keeps the above text on the screen for 12 seconds and then clears the screen to make the UI more appeasing for the user
time.sleep(12)
os.system("clear")
print()
print()

#Give the user the option of choosing from one of three difficulty levels, which will give them more or less guesses accordingly
while True:
    print()
    lives = input("Do you want to play the easy, medium, or hard version of this game? (please reply with e, m, or h) ➡️  ")
    if lives == "e":
        counter = 6
        time.sleep(0.5)
        os.system("clear")
        break
    elif lives == "m":
        counter = 5
        time.sleep(0.5)
        os.system("clear")    
        break
    elif lives  == "h":
        counter = 4
        time.sleep(0.5)
        os.system("clear")
        break
while True:
    print()
    print()
    
    #Automatically converts any letter they type into a lowercase letter
    letter = input("Choose a letter: ").lower()
    time.sleep(0.5)
    os.system("clear")
    
    #Ensures that the user selects a single letter and not something else 
    lowerLetter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    if letter not in lowerLetter:
        print("You can only select a letter. Please try again!")
        
    else:
        #Bug fix to stop the user losing another life if they have already chosen that letter
        if letter in lettersChosen:
            print(f"\033[31m""That letter has already been selected before. 😕" "\033[0m")
            #print(f"You have", counter, "lives remaining")
            
        #adds the letter chosen to the empty list we created at the start
        lettersChosen.append(letter)
        
        #Let the user know whether they were successful or not choosing a letter
        if letter in myWord:
            print(f"\033[32m""You found a letter! 😀""\033[0m")
        else:
            print("\033[31m""Nope, unfortunately that letter is not in there. 😕""\033[0m")
            counter -=1
            
        print(f"You have", counter, "lives remaining")
        #print()

        #what will be displayed depending on whether the users guesses a letter correctly or not. Also modified the default function of creating a new line
        guessedCorrect = True
        print()
        for i in myWord:
            if i in lettersChosen:
                print(i, end="")
            else:
                print("_", end="")
                guessedCorrect = False
    
        #Let the user know they have won and also the amount of lives remaining     
        if guessedCorrect:
            print()
            print()
            print(f"\033[32m""You won! The correct answer was" "\033[1;3m",myWord, sep=" ", end=". " "\033[0m" "\033[32m")
            print()
            print(f"And you still had",counter, sep=" ", end=" " "lives remaining. Awesome!""\033[0m")
            break
            
        #Let the user know they have run out of lives and what the correct word was
        if counter <=0 :
            print()
            print()
            print(f"\033[31m""You ran out of lives. The word you were looking for was" "\033[1;3m",myWord, sep=" ", end="." "\033[0m")
            break
        
        
        

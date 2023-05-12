# Quiz-Game.Py

## What to expect:

In this project I created a in computer quiz game. Using only python. 

### First:

We start with Printing "Welcome to my Quiz" within the command line. /

```
playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
    
print("Cool! Let's Play :) ")
    ```
This line of text basically tells the computer, "Hey, if player selects yes, / 
they'd like to play then print 'Cool! Let's Play :)' if player inouts no, or anything /
aside from yes, then quit the game. The "lower" basically lets the computer now, that /
no matter how the player types 'Yes', yes will always return lowercase. (to avoid, player /
needing to exactly match the way yes is written.

## Next:

```
score = 0

answer = input("How many Zodiac signs are there in Western Astrology? ")
if answer == "12" or "twelve" or "Twelve":
    print("YAY! Correct!")
    score += 1
else: 
    print("Sorry, Incorrect!")

answer = input("What Zodiac sign represents the lion? ")
if answer.lower() == "Leo" or "leo":
    print("YAY! Correct!")
    score += 1
else: 
    print("Sorry, Incorrect!")

answer = input("What element is the Zodaic sign Aries know for? ")
if answer.lower() == "Fire" or "fire":
    print("YAY! Correct!")
    score += 1
else: 
    print("Sorry, Incorrect!")

answer = input("What Zodiac sign is known as 'The Virgin'? ")
if answer.lower() == "Virgo" or "virgo":
    print("YAY! Correct!")
    score += 1
else: 
    print("Sorry, Incorrect!")

answer = input("What Zodiac sign is a Earth Sign? (please input only one answer) ")
if answer == "Capricorn" or "capricorn" or "Taurus" or "taurus" or "virgo" or "Virgo" or "Sagittarius" or "sagittarius":
    print("YAY! Correct!")
    score += 1
else: 
    print("Sorry, Incorrect!")
    ```

We now create the questionnarie for the quiz game itself. /
Thes starting score is 0, hence the variable 'score=0'. /
After you answer each question, 'score += 1' tells the computer,/
for every right answer the player gets correct, print 'YAY! Correct' /
and add 1. 'Else' print "Sorry, Incorrect" and add no "point". 

## Lastly: 

```
print("Hey! You got " + str(score) + " questions correct! Thanks for playing! ")
print("You got " + str((score/5) * 100) + "%!")
```

The game is now complete. This following code tells the computer, /
"Hey, tally up each 'score' (from the variable we created earlier, adding /
=+ 1, for every correct answer) and print "Hey, You got 'X' questions correct! /
Thanks for playing!  :)" along with the percentage player has gotten correct. 

THANK YOU

 

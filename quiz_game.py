print("Welcome to my Quiz")


playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Cool! Let's Play :) ")

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

print("Hey! You got " + str(score) + " questions correct! Thanks for playing! ")
print("You got " + str((score/5) * 100) + "%!")

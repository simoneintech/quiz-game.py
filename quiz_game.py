print("Welcome to my Quiz")


playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Cool! Let's Play :) ")

answer = input("How many Zodiac signs are there in Western Astrology? ")
if answer == "12" or "twelve":
    print("YAY! Correct!")
else: 
    print("Sorry, Incorrect!")

answer = input("What Zodiac sign represents the lion? ")
if answer == "Leo" or "leo":
    print("YAY! Correct!")
else: 
    print("Sorry, Incorrect!")

answer = input("What element is the Zodaic sign Aries know for? ")
if answer == "Fire" or "fire":
    print("YAY! Correct!")
else: 
    print("Sorry, Incorrect!")

answer = input("What Zodiac sign is known as 'The Virgin'? ")
if answer == "Virgo" or "virgo":
    print("YAY! Correct!")
else: 
    print("Sorry, Incorrect!")

answer = input("What Zodiac sign is a Earth Sign? (please input only one answer) ")
if answer == "Capricorn" or "capricorn" or "Taurus" or "taurus" or "virgo" or "Virgo" or "Sagittarius" or "sagittarius":
    print("YAY! Correct!")
else: 
    print("Sorry, Incorrect!")



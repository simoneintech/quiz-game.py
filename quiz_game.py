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

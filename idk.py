import ascii_magic

answer = input("Would you like to play? (yes/no)")

if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads, would you like to go (left/right?)").lower().strip()
    if answer == "left":
        answer = input("You encounter a scammer, would you like to run or trust?")

        if answer == "trust":
            print("That was not the greatest idea! Your computer has virus!")
            
        elif answer ==("run"):
            print("Good choice, you made it away safely!")
            answer = input ("You now have a choice, would you like to, (camp/hunt)")

            if answer == ("camp"):
                print("You died of coldness, nice try!")

            elif answer ==("hunt"):
                print("Good job! You got food and survived the night!")
                my_art = ascii_magic.from_image_file('moon.jpg')
                ascii_magic.to_terminal(my_art)

            else:
                print("You couldn't pick your choice, so you died of hunger")

        if answer =="right":
            print("You fell off a cliff, good job buckaroo.")

    else:
        print("Invalid choice, you lost!")

else:
    print("Thats too bad!")
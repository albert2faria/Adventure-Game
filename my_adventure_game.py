import time
import random


items = []
heavy_object = ["fridge", "piano", "car", "laundy machine",
                "elevator", "truck", "container"]


def print_pause(message):
    print(message)
    time.sleep(0.5)


def backpack():
    print_pause("The items on your backpack are: " + str(items) + ".")


def try_again():
    play_again = input("Do you want to play again? (yes/no)\n").lower()
    if play_again == "yes":
        play_game()
    elif play_again == "no":
        print_pause("Thanks for playing.")
    else:
        print_pause("Answer yes or no.\n")
        try_again()


def intro():
    print_pause("You are the famous cartoon the Coyote.")
    print_pause("And once again you find yourself in the hunt "
                "of the Road Runner.")
    print_pause("After weeks of research and data gathering,")
    print_pause("you know finally the places he will run through.")
    print_pause("The time for action is today.\n")


def path1():
    print_pause("The Coyote goes back home.")
    if "Scissors" in items:
        print_pause("There is nothing left in the cave.")
    elif "Matches" in items:
        print_pause("You light up a match to see in the darkness.")
        print_pause("In there you find a pair of scissors.")
        cave_items = input("Will you take them? (yes/no)\n")
        if cave_items == "yes":
            print_pause("The Coyote grabs the tools for his big plan.\n")
            items.append("Scissors")
        elif cave_items == "no":
            print_pause("The Coyote takes nothing.\n")
        else:
            print_pause("Wrong input, try again.\n")
            path1()
    else:
        print_pause("It's too dark and you can't see anything.\n")
    backpack()
    cartoon_travel()


def path2():
    print_pause("The Coyote arrives at the main road.")
    print_pause("You find a fuse hidden behind a bush. ")
    if "Map" in items:
        print_pause("The dynamite didn't work...")
        print_pause("You already took the map.\n")
    elif "Matches" in items:
        print_pause("You see how the Road Runners is approaching fast.")
        boom = input("Will you light up the fuse? (yes/no)\n")
        if boom == "yes":
            print_pause("The Coyote lights up the fuse.")
            print_pause("You see how the fuse is connected to a "
                        "pack of dynamite in the distance.")
            print_pause("The Road Runner is really close.\n")
            print_pause("BOOOOOMMMMMM!!!!!!!!!!\n")
            print_pause("The Coyote starts celebrating his succesfull hunt.\n")
            print_pause("Out of the smoke a shadow creeps out at top speed.")
            print_pause("BEEP BEEP!!")
            print_pause("The Road Runner screams as he runs away.\n")
            print_pause("Coyote goes back screaming "
                        "and cursing.")
            print_pause("The Coyote realizes he will need"
                        " to end this in the tunnel.\n")
            print_pause("You go back to the bushes and find a"
                        " map of the Tunnels.\n")
            items.append("Map")
        elif boom == "no":
            print_pause("You see the Road Runner in the distance "
                        "and getting closer.")
            print_pause("The Road Runner sees you and runs away.\n")
            print_pause("The Coyote realizes he will need to end "
                        "this in the tunnel.\n")
            print_pause("You go back to the bushes and find a map "
                        "of the Tunnels.\n")
            items.append("Map")
        else:
            print_pause("Wrong input, try again.\n")
            path2()
    else:
        print_pause("You need matches to light up the fuse.\n")
    backpack()
    cartoon_travel()


def path3():
    print_pause("The Coyote finds a hole hidden in the middle of the desert.")
    if "Matches" in items:
        print_pause("You find a pack of matches hidden.")
        print_pause("You already cleared the Secret Stash.")
    else:
        hole_items = input("Will you take them? (yes/no)\n")
        if hole_items == "yes":
            print_pause("The Coyote grabs the tools for his big plan.\n")
            items.append("Matches")
        elif hole_items == "no":
            print_pause("The Coyote takes nothing.\n")
        else:
            print_pause("Wrong input, try again.\n")
            path3()
    backpack()
    cartoon_travel()


def path4():
    object1 = random.choice(heavy_object)
    object2 = random.choice(heavy_object)
    print_pause("The Coyote arrives at the end of the tunnel.")
    if "Map" in items:
        print_pause("You use the map to travel through the tunnels.")
        print_pause("You see two ropes attached at two of the "
                    "exits of the tunnel.")
        print_pause("You inspect the ropes and realize the"
                    " first is supporting a " + object1 + ".")
        print_pause("while the second supports a " + object2 + ".")
        print_pause("both are supported right over the exits.\n")
        if "Scissors" in items:
            print_pause("As the Coyote is waiting for his prey.")
            print_pause("You listen a BEEEP BEEEEP!!!!!")
            print_pause("The Road Runner is nearby but you don't "
                        "know which exit he will be using.\n")
            print_pause("It's now or never!!!!")
            rope = input("Will you cut the first or "
                         "second rope? (first/second)\n")
            if rope == "first":
                print_pause("The Coyote quickly cuts the first rope.")
                print_pause("the rope is cut and the " + object1 +
                            " quickly drops.\n")
                print_pause("PUFF!!!")
                print_pause("As a cloud of dust blocks your vision,")
                print_pause("you listen the BEEP BEEP!!!! as the "
                            "Road Runner runs away through the other exit.")
                print_pause("The Coyote while crying approaches "
                            "the other exit.")
                print_pause("Once he crosses the tunnel you see"
                            " the Road Runner on the other exit besides"
                            " the second rope.")
                print_pause("You look over you and see " + object2 +
                            " hanging above you.")
                print_pause("BEEP BEEP!!")
                print_pause("The Road Runner screams as he cuts the rope.")
                print_pause("PUFF!!!")
                print_pause("The " + object2 + " smashes you flat!!\n")
                print_pause("YOU HAVE LOST")
            elif rope == "second":
                print_pause("The Coyote quickly cuts the second rope.")
                print_pause("the rope is cut and the " + object1 +
                            " quickly drops.\n")
                print_pause("PUFF!!!")
                print_pause("As a cloud of dust blocks your vision,")
                print_pause("for the first time since the hunt "
                            "started you listen to nothing but silence.")
                print_pause("You approach the cloud of dust "
                            "and discover the smashed Road Runner.")
                print_pause("The Coyote screams and celebreates"
                            " for a succesfull hunt!\n")
                print_pause("CONGRATULATIONS, YOU HAVE WON!")
            else:
                print_pause("Wrong input, try again.\n")
                path4()
        else:
            print_pause("You can't cut the rope.")
            backpack()
            cartoon_travel()
    else:
        print_pause("You can't go inside without a map, you could get lost.\n")
        backpack()
        cartoon_travel()


def cartoon_travel():
    print_pause("You find yourself in the middle of the desert.")
    print_pause("Time is ticking.")
    print_pause("Where will you go?\n")
    path = input("1. The Coyote Cave.\n"
                 "2. The Main Road.\n"
                 "3. The Secret Stash.\n"
                 "4. The Tunnel.\n\n").lower()
    if path == "1":
        path1()
    elif path == "2":
        path2()
    elif path == "3":
        path3()
    elif path == "4":
        path4()
    else:
        print_pause("Enter a number from 1 to 4.")
        cartoon_travel()


def play_game():
    intro()
    cartoon_travel()
    try_again()


play_game()

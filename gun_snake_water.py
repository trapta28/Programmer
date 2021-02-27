leg = ["snake", "water", "gun"]
n = 3
you_win = 0
you_loose = 0
draw = 0
while(n>0):
    you_win = 0
    you_loose = 0
    draw = 0
    import random

    random_number = random.choice([0, 1, 2])
    foot = leg[random_number]
    pucho = input("kahiye SNAKE ki WATER ki GUN : ")
    print(pucho)
    print(foot)
    if n > 0:
        n = n-1
        if pucho == "snake":
            if foot == "snake":
                print("sorry we matched")
                print("no. of times draw")
                draw =+1
            elif foot == "water":
                print("you win")
                you_win =+ 1
                print("no. of times you win:" , n )
            else:
                print("you loose")
                you_loose=+ 1
                print("no. of times you loose" ,n)
        elif pucho == "water":
            if foot == "water":
                print("sorry we matched")
                draw=+ 1
                print("no. of times draw")
            elif foot == "gun":
                print("you win")
                you_win =+ 1
                print("no. of times you win:",)
            else:
                print("you loose")
                you_loose=+ 1
                print("no. of times you loose",)
        elif pucho == "gun":
            if foot == "gun":
                print("sorry we matched")
                draw=+ 1
                print("no. of times draw", )
            elif foot == "snake":
                print("you win")
                you_win=+ 1
                print("no. of times you win:")
            else:
                print("you loose")
                you_loose=+ 1
                print("no. of times you loose")
        else:
            print("sorry we don't know ")
            break
    else:
        break
if you_loose > you_win and draw<=2:
    print("you loose the game")
elif you_loose == you_win and draw<=2:
    print("it's draw")
elif draw< 2:
    print("it's draw")
else:
    print("you win")
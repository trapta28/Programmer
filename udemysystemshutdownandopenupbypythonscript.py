#systen shutdown and restart using python script

import os

def systemOffRestart():
    print("Enter r for restart")
    print("Enter s for shutdown")
    print("Enter any key for exit")

    option = input("Enter you option :")
    if option=='r':
        os.system('shutdown /r')
    elif option =='s':
        os.system('shutdown /s')
    else:
        exit()


systemOffRestart()
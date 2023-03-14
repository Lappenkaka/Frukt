import random 
Frukter = ("Banan","Melon","citron","kiwi","Vindruva")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + Frukter[fnr-1 + "kommer här! \n"])

while looping:
    go = input("vill du välja en frukt till? j/n ")
    print("\n")

    if(go == "n"):
        break

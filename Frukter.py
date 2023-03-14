import random 
Frukter = ("Banan","Melon","citron","kiwi","Vindruva")
looping = True

def print_fruit(userinput):
    fnr = int(userinput)
    print("\n" + Frukter[fnr-1] + "kommer här! \n")


while looping:

    print("---------------------------------------")
    print("\n-:fruktAutomat.-\n")
    i=1



    for frukt in Frukter:
        print(str(i) + ": " + frukt)
        i+=1

    frukter = input("\nMata in nr på frukt du vill ha: ")

    print_fruit(frukter)



    go = input("vill du välja en frukt till? j/n ")
    print("\n")

    if(go == "n"):
        break

    print("-------------------------")
    print("Du får en frukt till")
    slumpfrukt = random.randint(1, 5)
    print_fruit(slumpfrukt)
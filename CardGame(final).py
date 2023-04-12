import random as ra

cards = ["Serce","Żołądź","Romb","Wino"]
all = []
p1 = []
p2 = []
decide_cards = 0
end1 = 1000

for num in range(2,15):
    for type in range(1,5):
        temp = str(num)
        temp+=str(type)
        all.append(temp)

##print(all, end="\n\n\n")

##for x in all:
##    print(x[:-1]+"    |    "+cards[int(x[-1])-1])

ra.shuffle(all)

def echo(uk_table):
    for x in uk_table:
        print(x[:-1]+"    |    "+cards[int(x[-1])-1])


def walidate(card):
    return(card[0][:-1]+" "+cards[int(card[0][-1])-1])

def win():
    if len(p1) < 3:
            print("Pierwszemu graczowi zabrakło kard")
            return()
    elif len(p2) < 3:
            print("Drugiemu graczowi zabrakło kard")
            return()
    for i in range(0,3):
        war.append(p1[0])
        war.append(p2[0])
        p1.pop(0)
        p2.pop(0)
    if int(war[-1][:-1]) == int(war[-2][:-1]):
        print("_____________________________________")
        print("Kolejna Wojna!!!!!!!!")
        print("_____________________________________")
        win()
    elif int(war[-1][:-1]) > int(war[-2][:-1]):
        print("[--------------------------]")
        print("Karty 'Puste' : "+str(war[-3][:-1]+" i ")+str(war[-4][:-1]))
        print(war[-1][:-1] +" VS "+ war[-2][:-1])
        print("Wygrywa gracz 1")
        print("[--------------------------]")
        for wr in war:
            p1.append(wr)
    elif int(war[-1][:-1]) < int(war[-2][:-1]):
        print("[--------------------------]")
        print("Karty 'Puste' : "+str(war[-3][:-1])+" i "+str(war[-4][:-1]))
        print(war[-1][:-1] +" VS "+ war[-2][:-1])
        print("Wygrywa gracz 2")
        print("[--------------------------]")
        for wr in war:
            p2.append(wr)


##echo(all)


for pl in all:
    if(decide_cards % 2 == 0):
        p1.append(pl)
    else:
        p2.append(pl)

    decide_cards += 1

echo(p1)
print("_____________________________________")
echo(p2)

while end1 != 0:
    print("_____________________________________")
    print("             Ilość kart gracza 1 : "+ str(len(p1)))
    print("             Ilość kart gracza 2 : "+ str(len(p2)))
    if len(p1) == 0:
        print("-----==================================================-----\n")
        print("                 Koniec ! Wygrywa gracz 2\n")
        print("-----==================================================-----")

        break
    elif len(p2) == 0:
        print("-----==================================================-----\n")
        print("                 Koniec ! Wygrywa gracz 1\n")
        print("-----==================================================-----")
        break
    elif int(p1[0][:-1]) > int(p2[0][:-1]):
        print("     --=={{{{{}}}}}==--")
        print("     "+walidate(p1)+" VS "+walidate(p2))
        print("     --=={{{{{}}}}}==--")
        p2.append(p2[0])
        p2.append(p1[0])
        p2.pop(0)
        p1.pop(0)
        print("[--------------------------]")
        print("Większą karte miał gracz : 1")
        print("[--------------------------]")
    elif int(p1[0][:-1]) < int(p2[0][:-1]):
        print("     --=={{{{{}}}}}==--")
        print("     "+walidate(p1)+" VS "+walidate(p2))
        print("     -=={{{{{}}}}}==--")
        p1.append(p2[0])
        p1.append(p1[0])
        p1.pop(0)
        p2.pop(0)
        print("[--------------------------]")
        print("Większą karte miał gracz : 2")
        print("[--------------------------]")
    elif int(p1[0][:-1]) == int(p2[0][:-1]):
        war = []
        print("_____________________________________")
        print("    ----==== WOJNA ====----")
        print("     "+walidate(p1)+" VS "+walidate(p2))
        print("_____________________________________")
        if len(p1) < 3:
            print("[--------------------------]")
            print("Pierwszemu graczowi zabrakło kard")
            print("[--------------------------]")
            break
        elif len(p2) < 3:
            print("[--------------------------]")
            print("Drugiemu graczowi zabrakło kard")
            print("[--------------------------]")
            break
        else:
            win()

    end1 -= 1
        
        
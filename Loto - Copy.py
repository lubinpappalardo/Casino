import time
from random import *


def menu():
    print("Vous avez plusieurs options:\n"
          "1 - Roue de la fortune\n"
          "2 - Mise en jeu extreme\n"
          "3 - Pariez sur le bon nombre\n"
          "4 - Quitter la partie avec votre argent.")


print("Bienvenue au loto !\n"
      "Vous commençez avec 100 points. Vous pouvez jouer ces points tant que vous voulez.\n"
      "Mais attention, si vous tombez à 0 points, c'est perdu.")
pts = 100


while True:
    menu()
    print("Vous avez " + str(pts) + " points !")
    choice = input("Votre choix: ")

    if choice == "1":
        print("Roue de la fortune\n"
              "Nous allons générer 3 chiffres au hazard, si se sont les mêmes, vous gagnez 1000 points.\n"
              "Prix de jeux : 5 points")
        fchoice1 = input("Voulez jouer ? ")
        if fchoice1 == "oui":
            pts -= 5
            num1 = randint(1, 10)
            num2 = randint(1, 10)
            num3 = randint(1, 10)
            time.sleep(0.2)
            print(num1)
            time.sleep(0.2)
            print(num2)
            time.sleep(0.2)
            print(num3)
            time.sleep(0.7)
            if num1 == num2 == num3:
                print("Vous avez gagné !")
                pts += 1005
            if num2 == num1 + 1 & num3 == num2 + 1:
                print("Vous avez gagné le secret jackpot !")
                pts += 2005
            else:
                print("Perdu !")
            time.sleep(2)

    if choice == "2":
        print("Mise en jeu extreme\n"
              "Misez ce que vous voulez, soit vous gagnez le double,\n"
              "soit vous perdez le double.")
        fchoice2 = input("Voulez vous jouer ? ")
        if fchoice2 == "oui":
            smej = int(input("Quelle somme voulez-vous miser ? "))
            if smej > pts:
                print("Vous ne pouvez pas miser plus de points que vous avez.")
            if smej <= pts:
                result2 = randint(0, 1)
                if result2 == 1:
                    pts = pts + 2 * smej
                    print("Vous avez gagné !")
                else:
                    pts = pts - 2 * smej
                    print("Perdu...")
            time.sleep(2)

    if choice == "3":
        print("Pariez sur le bon nombre !\n"
              "Un nombre entre 1 et 5 est genere,\n"
              "devinez lequel pour gagner 100 points !\n"
              "Prix du jeux : 10 points")
        fchoice3 = input("Voulez vous jouer ? ")
        if fchoice3 == "oui":
            nbet = int(input("Sur quel nombre misez-vous ? "))
            result3 = randint(0, 5)
            print(result3)
            time.sleep(0.5)
            if result3 == nbet:
                pts += 100
                print("Vous avez gagné !")
            else:
                pts -= 10
                print("Perdu...")
            time.sleep(2)

    if choice == "4":
        fchoice4 = input("Voulez-vous quittez ? ")
        if fchoice4 == "oui":
            print("Vous repartez avec " + str(pts) + " points !")
            exit()

    if pts == 0:
        print("Vous n'avez plus de points !\n"
              "Vous avez perdu !")
        exit()
    if pts < 0:
        print("Vous avez perdu !\n"
              "Vous devez " + str(pts) + " points !")
        exit()

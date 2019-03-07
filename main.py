from zawodnik import Zawodnik
import csv
import random

def losowanie_druzyn():
    druzyny = []
    f = open('druzyny.txt', 'r')
    while True:
        line = f.readline()
        l = line.strip('\n')
        if not line:
            f.close()
            break
        druzyny.append(l)
    d1 = random.randint(0,3)
    d2 = random.randint(0,3)
    while d1==d2:
        d2 = random.randint(0,3)

    return druzyny[d1],druzyny[d2]

def przeciwnicy():
    team1sq = []
    team2sq = []
    sparing = losowanie_druzyn()
    team1 = sparing[0]
    team2 = sparing[1]
    with open('zawodnicy.txt', newline='') as f:
        zawodnicy = csv.reader(f, delimiter = ',')

        for zawodnik in zawodnicy:
            nowy = Zawodnik(zawodnik[0], zawodnik[1], zawodnik[2], zawodnik[3], zawodnik[4], zawodnik[5], zawodnik[6])
            if (nowy.druzyna == team1):
                team1sq.append(nowy)
            elif (nowy.druzyna == team2):
                team2sq.append(nowy)
    return [team1sq,team2sq]



def tabela(array):
    for el in array:
        print("==========================")
        for x in range(0,4):
            print(el[x].imie," | ",el[x].druzyna," | ",el[x].zawartosc_butelki)


def gra(teams):
    zaczynajacy = random.randint(0,1)
    if(zaczynajacy == 1):
        zaczynajacy = teams[1]
    else:
        zaczynajacy = teams[0]
    return zaczynajacy



def main():
    grajacy = przeciwnicy()
    gra(grajacy)
    while True:
        grajacy[0][0].rzut()
        print(tabela(grajacy))
        if len(grajacy[0])==0:
            print("wygrywa druzyna ",grajacy[0].druzyna)
        elif len(grajacy[1])==0:
            print("wygrywa druzyna ",grajacy[0].druzyna)


#tabela(grajacy)

main()
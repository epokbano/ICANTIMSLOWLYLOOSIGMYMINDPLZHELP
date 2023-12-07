ksiazka_badhumoursorry = {
    "strona": [1,2,3,4,5],
    "SEKS": None
}

     

ksiazka_badhumoursorry["strona",(1)] = "CHAPTER NAMED: kavasaki"
def wers1():
        inp = int(input("teraz wers wybierz (1,2,3)"))
        while inp not in [1, 2, 3]:
            inp = int(input("teraz wers wybierz (1,2,3)"))
        if inp == 1:
            print("idk the end :D")
        if inp == 2:
            print("ppdj")
        if inp == 3:
            print("papiez to pedal")

ksiazka_badhumoursorry["strona",(2)] = "CHAPTER NAMED: cago"
def wers2():
        inp = int(input("teraz wers wybierz (1,2,3)"))
        while inp not in [1, 2, 3]:
            inp = int(input("teraz wers wybierz (1,2,3)"))
        if inp == 1:
            print("awooga")
        if inp == 2:
            print("awooga")
        if inp == 3:
            print("awooga")
ksiazka_badhumoursorry["strona",(3)] = "CHAPTER NAMED: krico"
def wers3():
        inp = int(input("teraz wers wybierz (1,2,3)"))
        while inp not in [1, 2, 3]:
            inp = int(input("teraz wers wybierz (1,2,3)"))
        if inp == 1:
            print("awooga")
        if inp == 2:
            print("awooga")
        if inp == 3:
            print("awooga")
ksiazka_badhumoursorry["strona",(4)] = "CHAPTER NAMED: estriper"
def wers4():
        inp = int(input("teraz wers wybierz (1,2,3)"))
        while inp not in [1, 2, 3]:
            inp = int(input("teraz wers wybierz (1,2,3)"))
        if inp == 1:
            print("awooga")
        if inp == 2:
            print("awooga")
        if inp == 3:
            print("awooga")
ksiazka_badhumoursorry["strona",(5)] = "CHAPTER NAMED: my fucking cancer"
def wers5():
     print(" Le monde n'est qu'une scene.\n Il vaut mieux rire que pleurer, \n car le rire est le propre de l'homme. \n Riez de tout cela, ne vous inquietez pas. \n profitos d'aujourd'hui.")
    
print("los penguinos me la van a mascar")
inp1 = int(input("please end my life (what page do you want? 1 - 5)"))
while inp1 not in ksiazka_badhumoursorry["strona"]:
    print("naw fam")
    inp1 = int(input("please end my life (what page do you want? 1 - 5)"))
if inp1 == 1:
    print(ksiazka_badhumoursorry["strona",(1)])
    wers1()
elif inp1 == 2:
    print(ksiazka_badhumoursorry["strona",(2)])
    wers2()
elif inp1 == 3:
    print(ksiazka_badhumoursorry["strona",(3)])
    wers3()
elif inp1 == 4:
    print(ksiazka_badhumoursorry["strona",(4)])
    wers4()
else:
    print(ksiazka_badhumoursorry["strona",(5)])
    wers5()


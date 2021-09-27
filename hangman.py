import random

#változók

correctg=[] #helyes tippek
incorrectg=[] #helytelen tippek
acsik=[]

#szólista megnyitása
source=open("wordbank.txt").read().splitlines()

#a szólistából kiválasztja a random generált sorszámú szót
solution=random.choice(source)
print(solution)

#a választott szó hossza
wlength=len(solution)
for i in range(wlength):
    acsik.append("_")
for elem in acsik:
    print(elem, end=" ")
print("\n")

#találgatás
while True:
    if "_" in acsik:
        #felhasználótól bekért betű > csere az acsikban
        uin=input("Guess a letter: ")
        #a játékos beírja a megoldást
        if uin==solution:
            print("Congrats! You have found the solution!")
            break
        if len(uin)>1 and uin!=solution:
            print("Wrong tipp!")
        #hosszáadja a megfelelő listához
        if uin in solution:
            correctg.append(uin)
        else:
            incorrectg.append(uin)
        print("Correct guesses:")
        for elem in correctg:
            print(elem, end="\t")
        print("\nIncorrect guesses:")
        for elem in incorrectg:
            print(elem, end="\t")

        #a felhasználó tippje hanyadik betű a megoldásban
        corpl=[] #a betű indexeinek tárolása
        for i in range(len(solution)):
            if solution[i]==uin:
                corpl.append(i)
        #print(corpl)
        #az acsikban kicseréli az uinra a corpl-ban lévő indexű elemeket
        for i in range(len(solution)):
            if i in corpl:
                acsik[i]=uin
        print("\n")
        #print(acsik)
        for elem in acsik:
            print(elem, end=" ")
        print("")
    else:
        print("Congrats! You have found the solution!")
        break


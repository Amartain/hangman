import random

#welcome text
print("Welcome to our game! ")
print("Remember, you can only guess by writing full words 3 times incorrectly, so use these wisely.")

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

guess=0

#találgatás
while True:
    if "_" in acsik:
        #felhasználótól bekért betű > csere az acsikban
        uin=input("Guess a letter or the whole word: ")
        #a játékos beírja a megoldást
        if uin==solution:
            print("Congrats! You have found the solution!")
            break
        if len(uin)>1 and uin!=solution:
            print("Wrong guess!")
            guess+=1
        if guess==3:
            print("You haven't got more chance.")
            break
        #hosszáadja a megfelelő listához
        if uin not in correctg and uin not in incorrectg:
            if uin in solution:
                correctg.append(uin)
            else:
                incorrectg.append(uin)
        else:
            print("You have already tried this letter.")
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


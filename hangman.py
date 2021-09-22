import random

#helyes/helytelen tipp lista létrehozása
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


#felhasználótól bekért betű > csere az acsikban
uin=input("Guess a letter: ")


#hosszáadja a megfelelő listához

if uin in solution:
    correctg.append(uin)
else:
    incorrectg.append(uin)
for elem in correctg:
    print(elem, end="\t")
print("\n")
for elem in incorrectg:
    print(elem, end="\t")

#a felhasználó tippje hanyadik betű a megoldásban
corpl=[] #a betű indexeinek tárolása
for i in range(len(solution)):
    if solution[i]==uin:
        corpl.append(i)
print(corpl)

acsik=[]

for i in range(len(solution)):
    if i in corpl:
        acsik.append(uin)
        #print(uin, end=" ")
    else:
        acsik.append("_")
        #print("_", end=" ")
#print(acsik)
for elem in acsik:
    print(elem, end=" ")


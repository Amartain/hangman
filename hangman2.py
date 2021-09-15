
import random

## 1. feladat - solution generálása
#megnyitja a könyvtárat - elolvassa - minden sornál megáll
wordbank=open("wordbank.txt").read().splitlines()
solution =random.choice(wordbank)
print(solution)

## 2. feladat - _ _ _ _ _
# 2.1. - megnézni milyen hosszú a line
#nl - number of letters
nol=len(solution)
acsik="_"*nol
print(acsik)

## 3.uin bekért betű cseréje _ az acsikban + correct incorrect besorolás
#lista
corg=[]
incorg=[]
corpl=[]

#3.1. besorolás corg, incorg

uin=input("Guess a letter: ")
if uin in solution:
    corg.append(uin)    # ez hozzáadja a correct listához - append
    print("ok")
else:
    incorg.append(uin)

for elem in corg:
    print(elem)
for elem in incorg:
    print(elem)

# 3.2. corg hanyadik elem uin a solutionben

for i in range(len(solution)): # len csak szám range az meg végigmegy rajta
    if solution[i]==uin: # i. elem a solutionben egyezik e
        corpl.append(i)
print(corpl)

# 3.3. csere
for i in range(len(solution)):
    if i in corpl:
        print(uin, end=" ")
    else:
        print("_", end=" " )
"""
mennyi = int(input("Hány állatot szeretnél hozzáadni? "))
allatok = []
szam = 1
for a in range(mennyi):
    allat = input(f"Add meg az {szam}. állat nevét: ")
    szam += 1
    pont = int(input(f"Add meg {allat} pontszámát: "))
    allatok.append((allat, pont))
    
megjel = input("Szeretnéd látni az összes állatot? (igen/nem): ")
if megjel == "igen":
    print(*allatok)
 
atlag = input("Szeretnéd tudni az átlagos pontszámot? (igen/nem): ")
ossz = 0
for i in allatok:
    ossz += i[1]
if atlag == "igen":
    print(f"Az átlagos pontszám: {ossz / mennyi}")

nagykicsi = input("Szeretnéd tudni a legmagasabb és a legalacsonyabb pontszámot? ")
nagy = 0
kicsi = 999999999999999999999999999999999999999990
for allat, pont in allatok:
    if pont > nagy:
        nagy = pont
    if pont < kicsi:
        kicsi = pont
print(f"Legmagasabb pontszám: {nagy}\nLegalacsonyabb pontszám: {kicsi}")
        
elt = input("Szeretnél eltávolítani egy állatot? (igen/nem): ")
kit = input("Add meg az állat nevét, akit el szeretnél távolítani: ")
if elt == "igen":
    for allat in allatok:
        if allat[0] == kit:
            allatok.remove(allat)
            
osz = input("Szeretnéd látni az összes állatot? (igen/nem): ")
if osz == "igen":
    print(allatok)
"""
"""
1. Feladat: Osztás nullával
	Leírás: Írj egy programot, amely két számot kér be a felhasználótól, és elvégzi a második szám osztását az elsővel. Ha a második szám nullával egyenlő, a program ne omoljon 	össze, hanem írjon ki egy hibaüzenetet, hogy nullával nem lehet osztani.

	Használd a try-except blokkot a ZeroDivisionError hibára.
"""
"""
szam1 = int(input("Adj meg egy számot: "))
szam2 = int(input("Adj meg egy másik számot: "))
try:
    print(szam1 // szam2)
except ZeroDivisionError:
    print("nm")
"""
"""
2. Feladat: Helytelen adattípus
	Leírás: Készíts egy programot, amely egy számot kér be a felhasználótól, és kiírja annak négyzetét. Ha a felhasználó nem számot ad meg, a program figyelmeztessen, hogy 	helytelen adattípust adott meg.
"""
"""
szam3 = int(input("Adj meg egy számot: "))

try:
    print(szam3 ** 2)
except ValueError:
    print("2sefse")
"""
"""
3. Feladat: Fájl olvasása
	Leírás: Írj egy programot, amely megpróbál megnyitni és beolvasni egy data.txt nevű fájlt. Ha a fájl nem található, a program írja ki, hogy a fájl nem létezik.
"""
"""
try:
    adat = open(data.txt)
except:
    print("awf")
"""
"""
4. Feladat: Lista elem lekérése index alapján
	Leírás: Készíts egy programot, amely egy listából kér le elemeket egy megadott index alapján. Kérj be egy indexet a felhasználótól, és próbáld meg kiolvasni az adott indexű 	elemet a listából. Ha az index kívül esik a lista határain, kezelje a program a hibát.
"""
"""
ind = int(input("Adj meg egy indexet: "))
lis = [1, 2, 3, 4, 5]
print(list[ind])
"""

"""
1. Feladat: Egyszerű Osztály Definiálása
	Leírás: Hozz létre egy Dog nevű osztályt, amely a kutyák nevét és életkorát tárolja. Az osztálynak legyen egy metódusa, amely kiírja a kutya adatait.

	Feladat:

	Készíts egy osztályt, amelynek van egy __init__ metódusa (konstruktor), amely a kutya nevét és életkorát tárolja.

	Hozz létre egy metódust display_info() néven, amely kiírja a kutya nevét és életkorát.

	Példányosítsd az osztályt, és hívd meg a metódust.
"""

class Dog:
    def __init__(self, nev, kor):
        self.nev = nev
        self.kor = kor

    def display_info(self):
        print(self.nev, self.kor)
        
dog1 = Dog("Szar", 2)
dog2 = Dog("Répa", 5)

dog1.display_info()
dog2.display_info()


"""
2. Feladat: Banki Számla Osztály

	Leírás: Hozz létre egy BankAccount nevű osztályt, amely banki számlákat reprezentál. Az osztály képes legyen befizetést és pénzfelvételt végrehajtani, valamint a számla 	egyenlegét lekérdezni.

	Feladat:

	Hozz létre egy osztályt, amely egy balance változót tárol.

	Készíts metódusokat:

	deposit(amount): hozzáadja az összeget az egyenleghez.

	withdraw(amount): levonja az összeget az egyenlegből, ha van elég pénz a számlán.

	get_balance(): visszaadja az aktuális egyenleget.

	Példányosítsd az osztályt, és végezz rajta befizetést, pénzfelvételt, és kérdezd le az egyenleget.
"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, egyenplussz):
        self.balance += egyenplussz
        
    def withdraw(self, egyenmin):
        self.balance -= egyenmin
    
    def get_balance(self):
        return self.balance
    
    
ember1 = BankAccount("Tóni", 2000)        
ember2 = BankAccount("Móni", 2000)    


"""
3. Feladat: Diák Osztály és Átlag Számítása
	Leírás: Készíts egy Student nevű osztályt, amely tárolja a diák nevét és jegyeit, és legyen képes kiszámolni az átlagukat.

	Feladat:

	Az osztály tárolja a diák nevét és egy jegyek listáját.
	Legyen egy metódus add_grade(grade), amely hozzáad egy jegyet a listához.
	Legyen egy metódus get_average(), amely kiszámolja és visszaadja az átlagot.
	Példányosíts egy diákot, adj hozzá jegyeket, és számold ki az átlagát.
"""

class Student:
    def __init__(self, nev, jegy)
























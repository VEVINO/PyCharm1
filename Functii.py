def printGreeting():
    print("Buna ziua ! Bine ati venit")

def printGreetingByName(nume, prenume):
    print(F'Buna ziua {nume} {prenume}')

def mediaNR(a, b, c):
    return (a + b + c) / 3

def piValue():
    return  3.14
   ## print('abc')        ## daca este scris dupa return nu va fi executat
# exercitiu
# daca numarul este pozitiv returnati True altfel False( daca persoana este majora)
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

 ### zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Vasile', 'Mocanu' )
printGreetingByName('Nicoleta', 'Mocanu' )
printGreetingByName('Sofia', 'Mocanu' )
print(mediaNR(3, 3, 4))
print(piValue())

print(verificareMajor(18))            ## pentru exercitiu

# vse ia varsta utilizatorului
age = int(input('introduceti varsta Dvs :'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie')     ## puterea metodelor
else:
    print('Nu ai varsta necesara (18) pentru a paria')

## OOP  >> Variabile : Atribute, proprieteti sau fields
## functii : metode
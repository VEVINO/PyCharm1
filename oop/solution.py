# class Car:
#     make = 'Dacia'
#     model = None
#     year = 2022
#     color = None
#     viteza = 0
#
#     def accelarate(self):
#         self.viteza = self.viteza + 10
#         print('vrumm')
#
#     def print_self(self):
#         print(self.make, self.year, self.viteza)
#
#     def stop(self):
#         self.viteza = self.viteza + 10
#         print('STOP!!')
#
#
# dictionar = {
#     "make": 'Dacia',
#     "model": None
# }
#
# lista1 = list
#
# car1 = Car()
# car2 = Car()
# print(car1.make, car1.year)
# print(car2.make, car2.year)
# car1.accelarate()
# car1.stop()
# car2.accelarate()
# car2.stop()
# print(car2.viteza)
# print(car1.viteza)
# print(car1.print_self())
# car1.print_self()
##  Exercitiu
# class Client:
#     user = "dasda"
#     parola = "oiahsid"
#
#     def ascunde_parola(self):
#         self.parola = len(self.parola) * '*'
#
#     def afiseaza_parola(self):
#         print(self.user, self.parola)
#
#
# print(Client.user)
# print(Client.parola)
# client1 = Client()
# client1.ascunde_parola()
# client1.afiseaza_parola()
# print()
# from datetime import date
#
#
# # class Om:
#     nume = None  ## exercitiu explicat in clasa..
#     varsta = None
#     Inaltime = None
#     greutate = None
#     data_nastere = None
#
#     def __init__(self, nume, varsta, greutate, data_nastere):
#         self.nume = nume
#         self.varsta = varsta
#         self.greutate = greutate
#         self.data_nastere = data_nastere
#         print(f' am atribuit {nume} {varsta} {greutate} {data_nastere} lui self')
#
#     def print_self(self):
#         print(self.nume, self.varsta, self.greutate, self.data_nastere)
#
#     def __str__(self):
#         return f"{self.nume}, {self.data_nastere}"
#
#
# om1 = Om("Daniel", 0, 3.200, date.today())
# om2 = Om("Rares", 0, 3.00, date.today())
# om1.print_self()
# om2.print_self()

# 1.Clasa Cerc
# Atribute: rază, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()
# class Cerc:
#     raza = None
#     culoare = None
#     diametru = None
#     circumferinta = None
#
#     def __init__(self, raza, culoare, diametru, circumferinta):
#         self.raza = raza
#         self.culoare = culoare
#         self.diametru = diametru
#         self.circumferinta = circumferinta
#
#     def descrie_cerc(self):
#         print(f'Acest Cerc are raza de {self.raza} m si este de culoarea {self.culoare},
#         diametrul de {self.diametru}m si circumferinta de {self.circumferinta} m.')
#
#     def aria(self):
#         pass
#
#     def diametru(self):
#         return 2 * self.raza
#
#     def circumferinta(self):
#         return 2 * 2 * self.raza


# 2. Clasa Dreptunghi
# Atribute: lungime, lățime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
# self.culoare. Poți verifica schimbarea culorii prin apelarea metodei
# descrie().


# class Dreptunghi:
#     lungime = None
#     latime = None
#     culoare = None
#
#     def __init__(self: lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def descrie(self):
#         print(f'Acest Dreptunghi are lungimea de {self.lungime} m si este de culoarea {self.culoare},
#         si latime de {self.latime} m')
#
#     def aria(self):
#         return self.latime * self.lungime
#
#
#     def perimetrul(self):
#         return 4 * (self.latime + self.lungime)
#
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
# Exemplu de variabila constanta( ce nu se schimba pe parcursul programului)
# DATABASE_URL = "http://mydb.com"
# class Dreptunghi:
#     lungime = None
#     latime = None                    ## EXERCITIU DE VERIFICAT(ERONAT).
#     culoeare = None
#
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     def decrie(self):
#         print(f"Printeaza culoarea {self.culoare}, L {self.latime},"
#               f" l {self.lungime} ale dreptunghiului")
#
#     def aria(self):
#         aria = self.latime * self.lungime
#         return aria
#
#     def perimetru(self):
#         perimetru = 2 * self.lungime + 2 * self.latime
#         return perimetru
#
#     def schimba_culoarea(self, noua_culoare):
#         self.culoare = noua_culoare
#         return noua_culoare
#
#
# lungime = float(input(" Care este:  L"))
# latime = float(input("Care este:  l"))
# culoare = input("Care este culoarea  "))
# my_dreptunghi = Dreptunghi(
#     lungime=lungime,
#     latime=latime,
#     culoare=culoare)
# my_dreptunghi.descrie()
# print("aria este : ", my_dreptunghi.aria())
# print("perimetrul este : ", my_dreptunghi.perimetru())
# my_dreptunghi.schimba_culoarea(
#     noua_culoare=input("spune-mi noua culoare a dreptunghiului de mai sus:  ")




#  exercitiu CERC  facut de DORIAN

import math
# r= float(input("Enter the radius of the circle::\n"))
# culoare = input('Culoare preferata?')

# class Circle:
#     raza = None
#     culoare = None
#
#     def __init__(self,raza,culoare):
#         self.raza = raza
#         self.culoare = culoare
#
#     def print_self(self):
#         print(self.raza, self.culoare)
#
#     def diametru(self):
#         d = 2 * self.raza
#         return d
#
#     def circumferinta(self):
#         c = 2 * math.pi * self.raza
#         return c
#
#     def aria(self):
#         a = math.pi * (self.raza * self.raza)
#         return a
#
#
# my_circle = Circle(raza=r,culoare=culoare)
# my_circle.print_self()
#
# print(my_circle.circumferinta())
# print(my_circle.diametru())
# print(my_circle.aria())




#
# DATABASE_URL = "https://mydb.com"
# USER = ""
# PAROLA = ""
#
#
# class Om:
#     nume = None
#     varsta = None
#     inaltime = None  # Corrected attribute name
#     greutate = None
#     data_nastere = None
#
#     def __init__(self, nume, varsta, inaltime, greutate, data_nastere):  # Added 'inaltime' parameter
#         self.nume = nume
#         self.varsta = varsta
#         self.inaltime = inaltime
#         self.greutate = greutate
#         self.data_nastere = data_nastere
#
#     def print_self(self):
#         print("sunt in functia print self \n")
#         print(self.nume, self.varsta, self.inaltime, self.greutate, self.data_nastere)
#
#     def __str__(self):
#         return f"{self.nume}, {self.data_nastere}"
#
#
# class Chef(Om):
#     def make_salad(self):
#         print("I made salad")
#
#     def make_fries(self):
#         print("I made fries")
#
#     def make_dishes(self):
#         print("I washed the dishes")
#
#
# class JapaneseChef(Chef):
#     sushi_level = None
#
#     def __init__(self, nume, varsta, inaltime, greutate, data_nastere, sushi_level):
#         super().__init__(nume, varsta, inaltime, greutate, data_nastere)
#         self.sushi_level = sushi_level
#
#     def make_sushi(self):
#         print("sushi")
#
#
# class ItalianChef(Chef):
#     def make_pizza(self):
#         print("pizza")
#
#
# bucatar = Chef(nume="dddd", varsta="88", inaltime="180", greutate="88", data_nastere="3.3.03")
# bucatar.print_self()
#
# om = Om('', ',', ',', ',', '')  # You need to provide actual values
#
# japan_chef = JapaneseChef(nume="Jiro", varsta="60", inaltime="170", greutate="70", data_nastere="1.1.1960", sushi_level="Master")
# japan_chef.print_self()

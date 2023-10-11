# from datetime import date
# from FormeGeometrice import Om
#
# om1 = Om("Daniel", 0, 3.200, date.today())
# om2 = Om("Rares", 0, 3.00, date.today())
# om3 = Om("Ioana", 0, 3.50, date.today())
# om4 = Om("Dorel", 0, 2.67, date.today())
#
# numar = str(10)  # str este functie a lui int
# maternity = [om1, om2, om3, om4]
# for element in maternity:
#      print(element)
#
# print(str(om1))
# print(str(om2))
# print(str(om3))
# print(str(om4))

# 1.Clasa Cerc
# Atribute: rază, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()


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



# import math
# from solution import Cerc
# cerc1 = Cerc(5, 'albastra',5, 5)
# cerc1.descrie_cerc()
# print(f'Aria cercului este {cerc1.aria()}')
# print(f"diametrul este de {cerc1.diametru}")
# print(f'circumferinta cercului este de {cerc1.circumferinta}')

# from solution import Dreptunghi
# dreptunghi1= Dreptunghi(5,'negru')
# dreptunghi1_descrie()

from datetime import date
# EXERCITIU DREPTUNGHI
# class Om:
#     nume = None
#     varsta = None
#     greutate = None
#     data_nastere = None
#
#
#     def __init__(self, nume, varsta, greutate, data_nastere):
#         self.nume = nume
#         self.varsta = varsta
#         self.greutate = greutate
#         self.data_nastere = data_nastere
#
#     def print_self(self):
#         print("sunt in functia print self \n")
#         print(self.nume, self.data_nastere, self.greutate, self.varsta)
#
#     def __str__(self):
#         return f"{self.nume}, {self.data_nastere}"
#
# # exemplu de variabila CONSTANTA(ce nu se schimba pe parcursul programului)
# DATABASE_URL = "https://mydb.com"
# USER = ""
# PAROLA = ""
#
#
# class Dreptunghi:
#     # atribute
#     lungime = None
#     latime = None
#     culoare = None
#
#     #constructor
#     def __init__(self, lungime, latime, culoare):
#         # self ne ajuta sa assignam valori atributelor obiectului curent
#         # (obiectelor viitoare)
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#
#     # metodele clasei
#     def descrie(self):
#         """printeaza toate atributele din obiectul curent(self)"""
#         print(f"Lungime: {self.lungime} "
#               f"Latime {self.latime} "
#               f"Culoare {self.culoare}")
#
#     def aria(self):
#         aria = self.lungime * self.latime
#         return aria
#
#     def perimetru(self):
#         perimetru = 2 * self.lungime + 2 * self.latime
#         return perimetru
#
#     def schimba_culoarea(self, noua_culoare):
#         """
#         Această metodă nu returneaza nimic. Ea va lua ca și parametru o nouă
#         culoare și va suprascrie atributul self.culoare.
#         Poți verifica schimbarea culorii prin apelarea metodei descrie().
#         """
#         self.culoare = noua_culoare
#
# # aceste variabile le folosim pentru a creea un dreptunghi
# lungime = float(input("Give me Lungime: "))
# latime = float(input("Give me Latime: "))
# culoare = input("Give me culoare: ")
#
# # suntem in viitor. in clasa dreptunghi variabilele lungime, latime si culoare
# # vor ajunge in self.lungime, self.latime respectiv self.culoare
# #acestea prin intermediul "self" apartin variabilei "my_dreptunghi"
# my_dreptunghi = Dreptunghi(
#     lungime=lungime,
#     latime=latime,
#     culoare=culoare
# )
# my_dreptunghi.descrie()
#
# # functia print afiseaza rezultatul functiei aria() apelata prin intermediul
# # my_dreptunghi
# print("aria este: ", my_dreptunghi.aria())
#
# # functia print afiseaza rezultatul functiei perimetru() apelata prin intermediul
# # my_dreptunghi
# print("perimetrul este: ", my_dreptunghi.perimetru())
#
#
# # apelam functia
# my_dreptunghi.schimba_culoarea(
#     noua_culoare=input("Spune-mi noua culoare a dreptunghiului de mai sus: ")
# )
#
# my_dreptunghi.descrie()







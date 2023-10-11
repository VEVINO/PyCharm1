# 5. Modernizează parcul de mașini:
#
# Crează o listă goală, masini_vechi.
# Iterează prin mașini.   se foloseste INDEX
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.
#
# masini = ['Lada', 'Lastun', 'Dacia_1100', 'Trabant', 'Citroen',
#                 'Audi', 'Volvo', 'Fiat', 'Opel']
# print(masini)
# masini_vechi = []
# print(list(enumerate(masini)))         # enumerare = obtinem indexul din lista parcursa
# wanted = ['Lastun', 'Trabant']
# for index, masina in enumerate(masini):
#     # if masina == 'Lastun' or masina == 'Trabant':        # varianta 1 de exercitiu
#     if masina in wanted:  # varianta 2 de exercitiu
#         masini_vechi.append(masini[index])         # index numara de la 0 = cu primul din lista la >>>>
#         masini[index] = 'Tesla'
# print(masini)
# print(masini_vechi)


# # 6. Având dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# for key, value in pret_masini.items():
#     if value <= 15000:
#
#         print(f"Puteti alege masina {key}")
# # Vine un client cu un buget de 15000 euro.
# #
# # Prezintă doar mașinile care se încadrează în acest buget.
# # Iterează prin dict.items() și accesează mașina și prețul.
# # Printează Pentru un buget de sub 15000 euro puteți alege mașină xLastun
# # Iterează prin listă.

#   7 . Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).


# counter = 0
# 7.
# for nr in numere:
#     if nr == 3:
#         counter += 1
#     print(counter)
# 8.
# min = 10000
# for nr in numere:
#     if nr < min:
#         min = nr
# print(min)
# 9.

# #10...
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# print(numere)
# for index, nr in enumerate(numere):
#     if nr > 0:
#         numere[index] = nr * -1          # valoare folosita inlocuire valoare negativa
# print(numere)


# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# pare = []  #  %2 == 0
# impare = []  #  %2 !1= 0
# pozitive = []   # > 0
# negative = []  #  <  0
#
# for nr in alte_numere:
#     if nr % 2 ==0:
#         pare.append(nr)
#     else:
#         # nr % 2 != 0:
#         impare.append(nr)       #  else folosit
#     if nr > 0:
#         pozitive.append(nr)
#     else:
#         # nr < 0:                # folosit doar if la toate <<
#         negative.append(nr)
# print(pare)
# print(impare)
# print(negative)
# print(pozitive)

# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final
#


# problema de SORTARE , cautare

"""
BUBBLE SORT
pas 1 :
compar elementul cu indexul 0 cu tot ce urmeaza dupa el, pana la finalul listei.
pas2 :
compar elementul cu indexul 1 cu tot ce urmeaza dupa el pana la finalul listei.
pas 3 :
compar elementul cu indexul 2 cu tot ce urmeaza dupa el pana la finalul listei.
Pana la len(lista)
.
.
.
.
pana la len(lista)
"""

# a = 1
# b = 2
# aux = 0
#
# aux = a             # metoda bubble  de interschimba 2 variabile
# a = b
# b = aux
# def suma_lista(lista):      exercitiu functii
#     suma = 0
#     for nr in lista:
#         suma += nr
#         return suma
#
#
# s = suma_lista(alte_numere)
# print(s)


# # pasii 0,1,2,3,4,5,6,7,8,9,
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)):
#     for j in range(i+1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             aux = alte_numere[i]
#             alte_numere[i] = alte_numere[j]
#             alte_numere[j] = aux
# print(alte_numere)
# 13. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!
# import random
#
# numar_secret = random.randint(1, 30)
# numar_ghicit = None
# while numar_secret != numar_ghicit:          # ex. echipa....
#     numar_ghicit = (input('numar:  '))
#     if int(numar_ghicit) > numar_secret:
#         print(f'Numarul introdus este prea mare')
#     elif int(numar_ghicit) < numar_secret:
#         print(f'Numarul introdus este prea mic')
#     else:
#         print('Felicitari ai gasit NR: ')






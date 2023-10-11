# numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# temp = -1
# for j in range(len(numere)):               ## exercitiu Danicel
#     for i in range(len(numere)):
#         if i+1 < len(numere) and numere[i] > numere[i+1]:
#             temp = numere[i+1]
#             numere[i+1] = numere[i]
#             numere[i] = temp
# print(numere)


## FUNCTII    SIMPLE   PARAMETRII   RETURN   PARAMETRI SI RETURN

#
# cars = ['Lada', 'Lastun', 'Dacia_1100', 'Trabant', 'Citroen',
#         'Audi', 'Volvo', 'Fiat', 'Opel']
# def print_cars(cars=["masina1", 'masina2']):
#     print(cars)
#
# def print_cars_reversed(cars):
#     print('lista masini: ', cars[::-1])
#
# lista = ['Lada', 'Lastun', 'Dacia_1100', 'Trabant', 'Citroen',
#          'Audi', 'Volvo', 'Fiat', 'Opel']
#
# print_cars(cars=lista)
# print_cars_reversed(cars)


# def sum2nr(a, b):
#     # print("lista masini: " cars)
#     # print(a + 1)
#     # print(b + 1)
#     #   print(a+b)
#     suma = a + b
#     return suma
# suma = sum2nr(5, 8)
# print(suma)

# def print_cars_reversed(cars):
#     print("lista masinii:", cars[::-1])

# print_cars_reversed()
# sum2nr(1, 2)
# EXERCITII

# def sum_2_nr(nr1, nr2):
#     suma = nr1 +nr2
#     return suma
#
# a = int(input("introdu nr1: "))
# b = int(input("introdu nr2: "))
# print(sum_2_nr(a, b))
# print(sum_2_nr(1, 8))
# print(sum_2_nr(5, 37))
# print(sum_2_nr(1234, 1234))
# print(sum_2_nr(4444, 4444))
# def is_par(nr):
# if nr % 2 == 0:
#     return True
# else:
#     return False
# print(is_par(23))
# print(is_par(24))
# print(is_par(25))

# def aria_dreptunghiului(lungime, latime):
#     aria = lungime * latime
#     return aria
# print(aria_dreptunghiului(50, 100))


# def total_chars(nume, prenume, nume_mijlociu):
#     total= len(nume) + len(prenume) + len(nume_mijlociu)
#     return total
#
# t = total_chars(            # bullshit nu am inteles nimic
#     nume="paun",
#     prenume="daniel",
#     nume_mijlociu="ion"
# )
# print()

# def sum_2_nr(nr1, nr2):
#     suma = nr1 + nr2
#     return suma
# print(sum_2_nr(200, 400))


# def is_par(nr):
#     if nr % 2 == 0:
#         return True
#     else:
#         return False
# print(is_par(56))

#
# def total_chars(
#         nume,
#         prenume,
#         nume_mijlociu
# ):
#     total = len(nume) + len(prenume) + len(nume_mijlociu)
#     return total
# print(total_chars(nume='vasile', prenume='ION', nume_mijlociu='Ghe'))

#
#
# def aria_dreptunghiului(lungimea, latimea):
#     aria = lungimea * latimea
#     return aria
# print(aria_dreptunghiului(34, 33))

# def aria_cercului(raza):
#     pi = 3.14159265359
#     aria = pi * raza * raza
#     return aria
# print(aria_cercului(10))
#
# def find(str1, str2):
#     if str1 in str2:
#         return True
#     else:
#         return False
#
# print(find('abc', 'abcuyt'))

# 7. Funcție fără return, primește un string și printează pe ecran:
# Numărul de caractere lower case este x
# Numărul de caractere upper case exte y

# def numar_mare_mic(x):
#     numar_mare = 0
#     numar_mic = 0
#     for char in x:
#         if str(char).islower():
#             numar_mic = numar_mic + 1
#         elif str(char).isupper():
#             numar_mare = numar_mare + 1
#         else:
#             continue
#     print(f'Am gasit atatea litere scrise cu majuscula:  {numar_mare}')
#     print(f'Am gasit atatea litere scrise cu minuscula:  {numar_mic}')
# numar_mare_mic('AteloIN')




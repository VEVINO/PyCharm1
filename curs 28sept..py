#  print(help("modules"))

# try: # in try punem codul'periculos'
#     lista = [1, 2, 3]
#     lista[6]
# except IndexError as e:  #  tratam Indexerror exceptie
#     print(e)
#     #formezi o exceptie
#  raise IndexError('Limita elevilor din clasa este de 30')

# def return_the_sixth(list):
#     try:
#         return list[6]                 ## exceptie este inten tionat bagata in cod
#     except IndexError as e:            ## si daca este suprascris mai tarziu  va functiona OK
#         # write error in logs here
#         print(e)
#         return list[-1]
# the_sixth = return_the_sixth([30, 20, 10, 435, 456, 5687, 678])
# print(the_sixth)
# def divide(x, y):         #test este numele, x si y sunt doua variabile pe care le dau functiei
#     try:
#         result = x // y
#     except ZeroDivisionError as e:
#         print("Impartirea la zero nu este permisa")
#         return -1
#     else:
#         print("divide done")
#         return result
#     finally:
#         print("acest cod se executa oricum.")
#
# nr1 = int(input("nr1: "))
# nr2 = int(input("nr2: "))
# print(divide(nr1, nr2))

# def return_the_sixth(list):               # varianta  cu if , else pentru exceptie
#     if len(list) < 6:
#         raise IndexError("Lista nu are 6 elemente cel putin.")
#     else:
#         return list[6]
#
# the_sixth = return_the_sixth([30, 20, 10, 435, 456, 5687, 678, 666])
# print(the_sixth)

# def divide(x, y):          # alta forma de exercitiu cu exception
#     try:
#         result = x // y
#     except (ZeroDivisionError, ConnectionError):
#         print("Impartirea la zero nu este permisa")
#         return -1
#     else:
#         print("divide done")
#         return result
#     finally:
#         print("acest cod se executa oricum.")
#
# nr1 = int(input("nr1: "))
# nr2 = int(input("nr2: "))
# print(divide(nr1, nr2))

# EXERCITII ECHIPA
# 8.
# Funcție care primește o LISTĂ de numere și returnează o LISTĂ doar cu numerele pozitive.
# def pozitiv_only(lista):
#     nr_pozitive = []
#     for nr in lista:
#         if nr > 0:
#             nr_pozitive.append(nr)
#     return nr_pozitive
# listapozitive = pozitiv_only([1, 3, 4, 6, 8])
# print(listapozitive)
# 9.
# Funcție care nu returneaza nimic. Primește două numere și PRINTEAZĂ
# def compare(x, y):               # afiseaza ce face
#     if x > y:
#         print(f"{x} e mai mare ca {y}")
#     elif y > x:
#         print(f"{y} e mai mare ca {x}")
#     else:
#         print("Numerele sunt egale")
# compare(5, 5)
# Primul număr x este mai mare decat al doilea număr y
# Al doilea număr y este mai mare decat primul număr x
# Numerele sunt egale.

# 10.
# Funcție care primește un număr și un set de numere.
# Printează ‘am adaugat numărul nou în set’ + returnează True
# Printează ‘nu am adaugat numărul în set. Acesta există deja’ + retu

# def add_number(number, set_numere):
#     if number not in set_numere:
#         set(set_numere).add(number)
#         print("am adaugat numarul in set")
#         return True
#     else:
#         print("Nu a adaugat. Exista deja")
#         return False
# set1 = {4, 5, 7}
# print(add_number(8, {3, 5, 8}))
# def add_number(number, set_numere):
#     try:
#         if number not in set_numere:
#             set_numere.add(number)    #  varianta cu exceptie
#             print("Am adaugat numarul in set")
#             return True
#         else:
#             print("Nu a adaugat. Exista deja")
#             return False
#     except Exception:
#         print(Exception('Error'))
# try:
#     print(add_number(8, 3, 5, 8))
# except TypeError:
#     print("Error")
# def add_number(number, set_numere):
#    try:
#         if number not in set_numere:
#             set_numere.add(number)
#             print("Am adaugat numarul in set")  #  exercitiu cu eroare
#             return True
#         else:
#             print("Nu am adaugat. Exista deja")
#             return False
#    except AttributeError as e:
#         print(e)
# set1 = {4, 5, 7}
# print(add_number(1, (3, 5, 8)))
# 11.
# Funcție care primește o lună din an și returnează câte zile are acea lună.

????


#12.
# Funcție calculator care să returneze 4 valori.Suma, diferența, înmulțirea, împărțirea a două numere.

# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
# # List
# list1 = ['abc', 34, True, 40, 'male', 'male']
# print(list1)
# print(list1[0])
# print(len(list1))


# # #    liste simplu inlantuite sau dublu inlantuite
# lista = [1, 2, 'asd', True, 5, 8]
# # print(lista)
# # print(lista[3])   # totul porneste de la 0 ca numaratoare normala
# # print(lista[-1])  # cu minus in lista se citeste de la celalalt capat
# print(lista[3:5])   # slicing
# print(lista[0:6:3])  # slicing
# print(lista[::5])   # slicing
# # lista.append(None)  # pentru o folosire pozitie goala si apare ca blank in cod
# # print(lista)

#  Dict
# mydict = { "brand": "Volvo", "model": "qwe", "2324": 34}
# # print(mydict)
# mydict["a"] = "wertyui"    # implementare element nou
# print(mydict)
# print(mydict.values())

# mydict = {                 # liste
#     "masini" : {
#         "brand": [1, 2, 3]
#     }
# }
# print(mydict['masini']["brand"][2])
# # matrice
# matrice = [
#     [1, 2, 3],
#     [4, 5, 6],
#     {"1": 2, "3": 4},
#     "234234"
#
# ]
# print(matrice[2]["3"])

# SET
# culori = {"alb", "rosu", "galben" }
# print(culori)
# print(len(culori))
#
# ss = {1, 2, 3, 3}    # seturile nu afiseaza duplicatele si se au doar ca original
# ff = {3, 4, 5}
# print(ss)
# print(ss,ff)
#
# print(ss.difference(ff))     # se citeste matematic
# print(ss.intersection(ff))    # doar ce este comun in cele 2 seturi

# ss = [1, 2, 3, 3, 3]
# ff = [3, 4, 5]
# print(set(ss).union(ff))    # uniunea(adunare) intre seturi

 # TUPLE   # un set in care valorile sant ordonate, imutabile si sant definite
 # accepta valorile duplicate  si este fixa > constant   (IMUTABIL)

# thistuple = ("apple", "banana", "cherry")
# print(thistuple)
# print(len(thistuple))

# ss = [1, 2, 3, 3, 3]   # Lista
# ff = {3, 4, 5, 5, 5}   # Set
#
# print(set(ss))
# #   Exercitiu
# count = 0
# for element in ss:
#     if element ==3:
#         print("l-am gasit pe 3")
#         count  = count + 1    # count ++
#
# print(f"L-am gasit pe 3 de {count} ori")


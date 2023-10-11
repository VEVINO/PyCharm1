# teste cu trainer

# note_muzicale = ['do', 're','mi','fa','so','la','si','do']
# print(note_muzicale)
#
# count = 0
# for nota in note_muzicale:
#     if nota == 'do':
#         count = count + 1
# print(f'"Am gasit nota de {count} ori')
# count = 0
#
# print(count)
# count = count + 1  # count = 0 + 1  -> count = 1
#
# print(count)
# count = count + 1  # count = 1 + 1 -> count = 2
#
# print(count)
# count = count + 1  # count = 2 + 1 -> count = 3
#
# print(f'L am gasit pe 3 de {count} ori')

# ss = {'oaiealba', 'oaieneagra', 'oaiealba',' vaca', 'taur', 'oaiealbastra', 'oi'}
# ff = {3, 4, 5, 6, 7, 7}
# print(ss)

# count_negre = 0
# count_albe = 0
# count_oi = 0                  # ciclurile repetitiv
# for element in ss:
#      if 'oi' in element:
#          count_oi += 1
#
#          print(f'oi : {count_oi}')

# count_negre = 0
# count_albastre = 0
# count_oi = 0
# for element in ss:
#     if element == 'oaiealba':
#         print('L am gasit pe 3 ')
#         count = count_oi + 1  # count ++
#
#     elif element == 'oaiealbastra':
#         count_negre = count_negre + 1
#
# print(f'oi albe: {count_negre} si oi albastre {count_albastre}')


# ss = {'oaiealba', 'oaieneagra', 'oaiealba',' vaca', 'taur', 'oaiealbastra', 'oi'}
# ff = {3, 4, 5, 6, 7, 7}
# count_negre = 0
# count_albastre = 0
# count_oi = 0
#
# lista = ['4', '5', '33', 4, 3, 3]
# string = '1234567'
# s = '3'
#
# if s in string:
#     # '3' in '1234567'
#     # se ia primul string si se cauta in interiorul celui de-al doilea string
#     print(f'l am gasit pe {s} in {string}')
#
# if s in lista:
#     # '3' in '3''4''5'
#     # se cauta primul element(oricare tip de variabila ar fi) si se cauta in lista
#     print('l am gasit in lista')

# l1 = [3,1,0,2]
# l2 = [6, 5, 4,]
#
# l3 = l1 + l2

# print(l1+l2)
# l3 = l1 + l2
# print(l3)
# l1.extend(l2)
# print(l1)

# l1.sort()
# print(l1)
# muta 0 la inceputul listei
# se face cu for

# if len(l3) > 0:
#     print('lista nu este goala')
# else:
#     print('lista este goala')

# l3.clear()
# print(l3)             # sterge din paranteze
# del l3                # sterge tot

# if len(l3) > 0:
#     print('lista nu este goala')
# else:
#     print('lista este goala')


# dict11 = {'Ana': 8, 'Gigel': 10, "dorel": 5}      # dict11['Gigel']
# print (dict11.keys())
# print(dict11.values())
#
# for key in dict11:
#      print(key, dict11[key])

# for key in dict11:
#     print(dict11[key])
# dict11['dorel'] = 6
# print(dict11)
#
# dict11.pop("Gigel")
# print(dict11)
#
# dict11['Ionica'] = 9
# print(dict11)

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'Sambata', 'Duminica'}
# weekend = {'Sambata', 'Duminica'}
#
# zile_sapt.add('Luni')
# print(zile_sapt)
#
# if weekend.issubset(zile_sapt):
#     print('este subset')
# else:
#     print('nu este subset')
#
# print(zile_sapt - weekend)
# print((zile_sapt.intersection(weekend)))


#   Import random
#
#
# da_team = ['Vasile', 'Valentin_Mihai', 'Corneliu', 'Raul', 'Anca', 'Bianca', 'Valentin_Sorin', 'Razvan', 'Ioana', 'Marius', 'Bogdan', 'Dorian', 'Madalina', 'Alexandru']
# sesiune = 4 #deja au trecut 4 sesiuni
# print(da_team)
# while len(da_team) >= 1:
#     prezinta_azi = random.choice(da_team)
#     sesiune = sesiune + 1
#     print(f'Sesiunea a {sesiune}-a, prezinta: {prezinta_azi}.')
#     da_team.remove(prezinta_azi)
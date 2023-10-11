# # dalmatienii
# for i in range(1,102):
#     print(f'Dalmatianul cu nr  {i}')
# dalmatienii
# for i in range(1,102,2):
#     print(f'Dalmatianul cu nr  {i}')
# for
# parcurgere lista cu for
# for i in range(0, len(numere)):
#     print(f'indexul curent este {i}')
#     print(f'numarul curent este {numere[i]}')


numere = [3, 4, 3, 3, 5, 3, 3, 3]
#  de cate ori apare 3 in [3, 2, 3, 5, 3, 3,]   tema de facut
count = 0
for Numar in numere:
    if Numar == '3':
        count = count + 1
print(f'"Am gasit pe 3 de {count} ori')

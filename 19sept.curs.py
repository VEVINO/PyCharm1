# Cicluri repetitive
# # for car in cars:
# #      if car == prefered_car:
# #       print(f'masina preferata este {car}')
# #       print(car)
# i = 0    # indexul fiecarui element din lista cars   i: 2
# while i < len(cars):
#     if  cars[i] == prefered_car:
#     # print(f'masina preferata este {cars[i]}')
#     # break
#     i += 1
#     continue
#     print(i, cars[i])
#     i += 1  # i=i + 1

# for i in range(len(cars)):
#     if 0 < i < len(cars) - 1:
#         cars[i] = cars[i].upper()   exercitiu facut de coleg..varianta
#
# else:
#     print(cars)

# for i, car in enumerate(cars):
#     if cars[i] == cars[0] or cars[i] == cars[-1]:   # exercitiu
#         continue
#     cars[i] = car.upper()
# print(cars)

# cars = ['Audi', 'Volvo', 'BMV', 'Mercedes',
#          'Aston-Martin', 'Lastun', 'Fiat', 'Trabant','Opel']
# prefered_car = 'Mercedes'
# # nu va modifica nimic in lista
# print(list(enumerate(cars)))
# for i, car in enumerate(cars):
#     # car = car.upper()
#     # if car == cars[0] or car == cars[-1]:
#     #     continue
#     if i == 0:
#         continue
#         cars[i] == car.upper()
#         print(i, car)
# else:
#     print(i)
#     print(cars)
# masini = ['Audi', 'Volvo', 'BMV', 'Mercedes',
#          'Aston-Martin', 'Lastun', 'Fiat', 'Trabant','Opel']
# masina_de_vanzare = 'Mercedes'
# for masina in masini:
#     if masina_de_vanzare == masina:
#         print(f'Am gasit masina Dv: {masina_de_vanzare}')
#         # break
#     else:
#         print(f'Am gasit masina X {masina}. Mai cautam ')

# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
#    Printează ‘Am găsit mașina X. Mai căutam‘

# masini = ['Audi', 'Volvo', 'BMV', 'Mercedes',
#          'Aston-Martin', 'Lastun', 'Fiat', 'Trabant','Opel']
# masina_de_vanzare = 'Mercedes'
# for masina in masini:
#     if masina in ('Lastun', 'Trabant'):
#         masini.remove(masina)
# print(masini)


    # if masina in ('Lastun', 'Trabant'):
    #     continue    # skipp
    # print(f'Sa-r putea sa va placa masina {masina}')


# Vine un cumpărător bogat dar indecis.
# Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
# Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.

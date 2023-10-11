# # 2. Verifică și afișează dacă x este număr natural sau nu.
# x = int(input("Enter a number: "))
#
# if x >= 0:
#     print(f" {x} is a natural number")
# else:
#     print(f" {x} is not a natural number")

# def input_validate(input_text: str):
#     string = input(input_text)
#     while string.__contains__('.') or string.__contains__(',') or string.isalpha():
#         print('Date incorecte! Incearca din nou!')
#         string = input(input_text)
#     return string

# x = input('enter number:')
# x = int(x)
# # % - modulo
# # este restul impartirii      # data science pentru matematica >broker>probabilitatea
#
# if x % 3 == 0:
#     print(f"rest: {x%2}")
#     print(f'numarul {x} este divizibil cu 3')
# else:
#     print(f'rest: {x % 2}')
#     print(f'numarul {x} este impar')

# 14.Exercițiu:
# citește un user de la tastatură;
# citește o parolă;
# afișează: 'Parola pt user x este ***** și are x caractere';
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.
#
# eg: parola abc => ***
#       parola abcd => ****

# user = input("user: ")
# parola = input('parola: ')
# lenght = len(parola)
#
# # l = [1, 2, 3, 4, 5, 6]
# # p = 'x' .join(l)
# print(f"userul {user} are parola  {lenght * '*'}")

# max_number = 0
# numbers = [21, 23, 121, 32, 43]
#
# for number in numbers:
#     if number > max_number:
#         max_number = number
#
# print(max_number)

# # 14.      x, y, z (int)
# # Afișează care este cel mai mare dintre ele?
#
# x = input('x= ')
# y = input('y= ')
# z = input('z= ')
#
# print(x, y, z)
# # 100 35  1 4 6 8 89 90 86 11
#
# if x >= y and x >= z:
#     print('x', x)
# elif y >= x and y > z:
#     print('y', y)
# elif z >= x and z > y:
#     print('z',z)

# 10.Transformă și printează notele din sistem românesc în  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
#
# nota = float(input('nota: '))
#
# if nota < 0:
#     nota = nota * -1
# print(nota)
#
# if nota >= 9:
#     print('A')
# elif nota >= 8:
#     print('B')
# elif nota >= 7:
#     print("c")
# elif nota >= 6:
#     print('D')
# elif nota > 4:
#     print("E")
# elif nota <= 4:
#     print("F")


# 8.
# X, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.


# # 9. Citește o literă de la tastatură.
# #     Verifică și afișează dacă este vocală sau nu.
#
# litera = input("introduceti o litera: ")
#
# vocale = 'aeiou'
# if litera in vocale:
#     print('este vocala')
# else:
#     print("este consoana")

# 1. introduceti un string de la tastatura. verificati daca acesta contine numere.


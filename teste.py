# 1. În cadrul unui comentariu, explică cu cuvintele tale ce este o variabilă.
# Raspuns : O magazie de scule si accesorii unde gasesti tot ce ai nevoie pentru a te folosi de ele mai tarziu sau pentru lucrarea curenta

# 2. Declară și initializează câte o variabilă din fiecare din următoarele tipuri de variabilă:
# string
var_str = 'VasileM'

# int
var_int = 45

# float
var_float = 12.55

# bool
bool = False
# Observație: Valorile vor fi alese de tine după preferințe.


# 3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(var_str))

# 4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
var_float = round(var_float)
print(var_float)

# Verifică tipul acesteia.
print(type(var_int))


# 5. Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
print(f'Numele meu este {var_str}')
print('Varsta mea este? ' + str(var_float))
print('E adevarat ca varsta mea este? ' + str(var_int))
print(f'Varsta mea este: {var_int}')
print(f'Am castigat la loto cu acest numar: {var_int}')
print('E adevarat ca voi castiga la loto cu acest numar? ' + str(bool))  #varianta 1
print(f'E adevarat ca voi castiga la loto cu acest numar? {bool}')   #varianta 2


# Rezolvă nepotrivirile de tip prin ce modalitate dorești.

# 6. Citește de la tastatură:
# numele;

# prenumele.

  #  Afișează: 'Numele complet are x caractere'

nume = input('nume: ')
prenume = input('prenume:  ')

print(' Numele complet are ' + str(len('nume + prenume')))

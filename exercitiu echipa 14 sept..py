# Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# Declară o Listă cu 5 jucători
# Schimbari_efectuate = te joci tu cu valori diferite
# Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# Efectuează schimbarea
# Șterge jucătorul scos din listă
# Adaugă jucătorul intrat
# Afișază a intrat x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
# Afișază ‘mai ai z schimbări’
# Testează codul cu diferite valori
# Google search hint
# “how to check if item is în list python”
#
# echipa = ['hagi', 'messi', 'ronaldo', 'mutu', 'banel']
#
#
# schimbari_efect = 2
# schimbari_max = 3
#
# jucator_schimbat = input('Scos din teren :')
# jucator_introdus = input('Introdus in teren :')
#
# if schimbari_efect < schimbari_max and jucator_schimbat in echipa:
#     if schimbari_efect < 3:
#         schimbari_efect = schimbari_efect +1
#         echipa.remove(jucator_schimbat)
#         echipa.append(jucator_introdus)
#     print(f'Afiseaza a intrat {jucator_introdus}, a iesit {jucator_schimbat}, mai ai {schimbari_max - schimbari_efect}')
#     print(echipa)
# elif schimbari_efect == schimbari_max:
#     print('Nu mai avem schimbari posibile')
# else:
#     print(f'Jucatorul {jucator_schimbat} nu se afla in echipa. Mai avem{schimbari_max - schimbari_efect} schimbari')





echipa = ['Ronaldo', 'Zidane', 'Messi', 'Maldini', 'Buffon']
schimbari_efectuate = 0
schimbari_max = 3

while schimbari_efectuate < schimbari_max:
    print(echipa)
    jucator_schimbat = input("Jucator schimbat: ")
    jucator_introdus = input("Jucator introdus: ")
    if jucator_schimbat in echipa:
        echipa.remove(jucator_schimbat)
        echipa.append(jucator_introdus)
        schimbari_efectuate = schimbari_efectuate + 1
        print(f'Jucatorul \"{jucator_schimbat}\" a fost scos. Jucatorul \"{jucator_introdus}\" a intrat pe teren. Schimbari ramase: {schimbari_max - schimbari_efectuate}.')
    else:
        print(f'Jucatorul \"{jucator_schimbat}\" nu face parte din echipa!')
        print(f'Schimbari ramase: {schimbari_max - schimbari_efectuate}')


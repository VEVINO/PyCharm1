# Clasa abstractă FormaGeometrica
class FormaGeometrica:
    PI = 3.14

    def descrie(self):
        print('Cel mai probabil am colturi')

    def aria(self):
        pass

# Clasa Pătrat
class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, val):
        self.__latura = val

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.latura**2

# Clasa Cerc
class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, val):
        self.__raza = val

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return self.PI * (self.raza**2)

# Polimorfism
class PiloniiOOP:
    def descrie(self):
        print('Eu nu am colturi')

# Exemplu de utilizare
if __name__ == '__main__':
    # Pătrat
    patrat = Patrat(5)
    print(f'Patrat: Latura = {patrat.latura}, Aria = {patrat.aria()}')
    patrat.descrie()

    # Modificăm latura
    patrat.latura = 7
    print(f'Patrat: Latura = {patrat.latura}, Aria = {patrat.aria()}')

    # Ștergem latura (opțional)
    del patrat.latura

    # Cerc
    cerc = Cerc(4)
    print(f'Cerc: Rază = {cerc.raza}, Aria = {cerc.aria()}')
    cerc.descrie()

    # Modificăm raza
    cerc.raza = 6
    print(f'Cerc: Rază = {cerc.raza}, Aria = {cerc.aria()}')
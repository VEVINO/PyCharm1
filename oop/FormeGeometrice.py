#
# DATABASE_URL = "https://mydb.com"
# USER = ""
# PAROLA = ""
#
#
# class Om:
#     nume = None
#     varsta = None
#     inaltime = None  # Corrected attribute name
#     greutate = None
#     data_nastere = None
#
#     def __init__(self, nume, varsta, inaltime, greutate, data_nastere):  # Added 'inaltime' parameter
#         self.nume = nume
#         self.varsta = varsta
#         self.inaltime = inaltime
#         self.greutate = greutate
#         self.data_nastere = data_nastere
#
#     def print_self(self):
#         print("sunt in functia print self \n")
#         print(self.nume, self.varsta, self.inaltime, self.greutate, self.data_nastere)
#
#     def __str__(self):
#         return f"{self.nume}, {self.data_nastere}"
#
#
# class Chef(Om):
#     def make_salad(self):
#         print("I made salad")
#
#     def make_fries(self):
#         print("I made fries")
#
#     def make_dishes(self):
#         print("I washed the dishes")
#
#
# class JapaneseChef(Chef):
#     sushi_level = None
#
#     def __init__(self, nume, varsta, inaltime, greutate, data_nastere, sushi_level):
#         super().__init__(nume, varsta, inaltime, greutate, data_nastere)
#         self.sushi_level = sushi_level
#
#     def make_sushi(self):
#         print("sushi")
#
#
# class ItalianChef(Chef):
#     def make_pizza(self):
#         print("pizza")
#
#
# bucatar = Chef(nume="Vasile", varsta="47", inaltime="185", greutate="110", data_nastere="10.4.77")
# bucatar.print_self()
#
# om = Om('', ',', ',', ',', '')  # You need to provide actual values
#
# japan_chef = JapaneseChef(nume="Jiro", varsta="60", inaltime="170", greutate="70", data_nastere="1.1.1960", sushi_level="Master")
# japan_chef.print_self()

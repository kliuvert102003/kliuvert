import random

nombre = input("introduce tu nombre: ")
print("tu nombre es",nombre)

edad = int(input("introduce tu edad: "))
print("tu edad es ", edad)

paises = ["Canada", "Bulgaria", "Polonia","Alemania"]
print("tu pais favorito es",random.choice(paises))

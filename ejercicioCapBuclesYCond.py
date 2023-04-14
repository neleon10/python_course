paises = {}

pais = input('Introduce pais: ')

while pais != 'quit':
    ciudad = input ('Introduce una ciudad: ')

    lista_ciudades = paises.setdefault(pais,[ciudad])

    if lista_ciudades != [ciudad]:
        paises[pais].append(ciudad)

    pais = input('Introduce país: ')

print(paises)


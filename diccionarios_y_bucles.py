capitales = {
    'España':'Madrid',
    'India':'Nueva Dehli',
    'Francia':'Paris',
    'Argentina':'Buenos Aires'
}

for key in capitales:
    valor=capitales[key]
    print(key,valor)

    """ items() es una forma de imprimir """

""" otra forma """
for key,value in capitales.items():
    print(key + ' => '+value)
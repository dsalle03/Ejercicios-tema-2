lista = [4,12,-9,8,4,9,6,7,-5,8,5,6,9,8,3,2]

def modificar(lista_1):
    lista_1 = list(set(lista_1))
    lista_1.sort(reverse=True)
    lista_2 = []
    for i in lista_1:
        if i % 2 == 0:
            lista_2.append(i)
    suma = sum(lista_2)
    lista_2.insert(0, suma)
    print(lista_2)
    return lista_2

nueva_lista = modificar(lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))






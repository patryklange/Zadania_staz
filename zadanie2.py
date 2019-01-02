def brakujace_elementy(lista,n):
    lista_wzorcowa = list(range(1,n+1))
    x= list(set(lista_wzorcowa) - set(lista))
    return x

print(brakujace_elementy([2,3,7,4,9], 10))
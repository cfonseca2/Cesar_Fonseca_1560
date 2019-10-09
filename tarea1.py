
def suma_lista(listaNumeros):
   if len(listaNumeros) == 1:
        return listaNumeros[0]
   else:
        return listaNumeros[0] + suma_lista(listaNumeros[1:])

def main():
    print(suma_lista([1,2,3,4,5]))

main()

        

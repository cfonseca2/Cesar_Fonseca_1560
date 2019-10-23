

from listas_enlazadas import Nodo , Linked_List

def main():
    lista=Linked_List()
    print(f"Está vacía?: {lista.is_empty()}")
    lista.append(10)
    lista.append(20)
    lista.append(30)
    lista.append(40)
    lista.append(50)
    lista.transversal()
    print(lista.get_tail().data)
    
    lista.append(60)

    lista.add_before( 30 , 25 )

    lista.transversal()

    lista.pop()

    lista.transversal()
    lista.add_after(10 , 15)
    lista.transversal()

    lista.remove(40)
    lista.transversal()
    


    

    
main()


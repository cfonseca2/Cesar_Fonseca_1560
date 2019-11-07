from arboles_binarios import NodoArbol

def main():
    root = NodoArbol('A', NodoArbol('B') , NodoArbol('C') )
    print("\t", root.data)
    print('' , root.left.data, end="")
    print('\t\t' , root.right.data)
    #root.left.left=NodoArbol('D',NodoArbol('I'),NodoArbol('J'))
    root.left.left=NodoArbol('D')
    root.left.left.left=NodoArbol('I')
    root.left.left.right=NodoArbol('J')
    root.right=NodoArbol('C', NodoArbol('G'), NodoArbol('H', NodoArbol('M',None, NodoArbol('N',NodoArbol('O')))))
    print(root.right.right.left.right.left.data)
    #Solo imprimir la hoja izquierda
    print(root.left.left.left.data)
    #Solo la hoja de la extrema izquierda, si no se conoce la profundida?
    curr_node = root
    while curr_node.left != None:
        curr_node=curr_node.left
    print(curr_node.data)

    #ambos nodos del nodo padre de la extrema derecha(No se conoce la prof)?
    curr_node = root
    while curr_node.right != None:
        curr_node=curr_node.right
    print(f" Izquierda: {curr_node.left.data} - Derecho:{curr_node.right}")
    
    
    
    
                             
                             

main()

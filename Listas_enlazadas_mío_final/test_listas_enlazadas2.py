from listas_enlazadas import Nodo

def main():
    head = Nodo (10)
    head.next = Nodo(20, Nodo(30, Nodo(40)))

    cur_node = head
    while cur_node.next != None:
        print(cur_node.data, "->" , end="")
        cur_node = cur_node.next
    print(cur_node.data)
    cur_node.next = Nodo(50)
    head=Nodo(5,head)

    cur_node = head
    while cur_node.next != None:
        print(cur_node.data, "->" , end="")
        cur_node = cur_node.next
    print(cur_node.data)
    

main()

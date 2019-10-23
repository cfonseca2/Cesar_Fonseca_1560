class Nodo:
    def __init__( self , value , siguiente = None ):
        self.data = value
        self.next = siguiente


# ADT Linked List

class Linked_List:
    def __init__( self ):
        self.head = None

    def is_empty( self ):
        return self.head == None

    def get_tail( self ):
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        return cur_node

    def append( self , value ):
        if self.is_empty():
            self.head = Nodo( value )
        else:
            self.get_tail().next = Nodo( value )

    def transversal( self ):
        cur_node = self.head
        while cur_node.next != None:
            print(cur_node.data, "->" , end= "")
            cur_node = cur_node.next
        print(cur_node.data)

    def prepend( self , value):
        self.head = Nodo(value, self.head)

    def remove( self, value ):
        cur_node = self.head
        try:
            previo = None
            while cur_node.data != value:
                previo = cur_node
                cur_node = cur_node.next
                pass
            previo.next = cur_node.next  
            
            self.size-=1
            pass
        except:
            print("Valor no valido")
            pass
        pass

     
    def pop( self ):
        cur_node = self.head
        prev = None
        while cur_node.next != None:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = None
        

    def add_before(self, ref_value, value):
        cur_node = self.head
        while cur_node.data != ref_value:
            prev = cur_node
            cur_node = cur_node.next
        prev.next = Nodo(value)
        prev.next.next = cur_node

    def add_after( self , ref_value , value):
        cur_node = self.head
        while cur_node.data == ref_value:
            desp = cur_node
            cur_node = cur_node.next
            desp.next = Nodo(value)
            desp.next.next = cur_node
        
        
        
   

    
        
     # def add_after( self , ref_value , value)
# head --> primer elemento de una lista ligada
# cur-Node --> variable para saltar de un nodo a otro  

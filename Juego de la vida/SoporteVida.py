from Array2d import Array2D

"""
0 --> Célula muerta
1 --> Célula viva

"""

class SoporteVida:
    def  __init__ ( self , rows , cols ):
        self.__rows = rows
        self.__cols = cols
        self.__gens = 0
        self.__grid = Array2D( rows , cols)
        self.__grid.clearing( 0 )

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def configure( self , inicial , generaciones):
        """ inicial es una lista de la forma:
                inicial = [[1,2],[2,2],[2,3],[3,1]]
        """
        
        self.__gens = generaciones
        for cell in inicial:
            self.__grid.set_item( cell[0] , cell[1] , 1 )

    def to_string(self):
        self.__grid.to_string()

    def clear_cell( self , row , col ):
        self.__grid.set_item(row,col,0)

    def set_cell(self,row,col):
        self.__grid.set_item(row,col,1)

    def is_alive_cell( self , row , col ):
        if self.__grid.get_item(row, col) == 1: # return self.__grid.get_item(row,col) == 1 --> lo mismo
            return True
        else:
            return False

    def get_alive_neighbors( self , row , col):
        vivos = 0
        limites = self.__calcula_vecinos(row,col)
        for r in range(limites[2],limites[3]+1,1):
            for c in range(limites[0],limites[1],1):
                if self.__grid.get_item(r,c) == 1:
                    vivos += 1
        return vivos
       
        """
        for r in range(self.__rows):
            for c in range(self.__cols):
                print(f"| {self.__grid.get_item(r,c) }|" , end="")
            print("")
            """

    def __calcula_vecinos(self,ren,col):

        x_ini = col-1
        x_fin = col+1
        y_ini = ren-1
        y_fin = ren+1
        if col == 0:
            x_ini = 0
        if col == self.__cols - 1:
            x_fin = self.__cols - 1
        if ren == 0:
            y_ini = 0
        if ren == self.__rows - 1:
            y_fin = self.__rows - 1

        return[x_ini, x_fin,y_ini,y_fin]
    
            
                             

def main():
  juego = SoporteVida(5 , 5)
  juego.to_string()
  juego.configure([[1,2],[2,1],[2,2],[2,3]], 5)
  print("Población inicial:")
  juego.to_string()
  juego.get_alive_neighbors(2,2)
  print(juego.get_alive_neighbors(0,0))
    
    
main()


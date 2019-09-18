from Array2d import Array2D
from SoporteVida import SoporteVida


class Juego:
    
    def __init__( self, rows, cols ):
        self.__tablero = SoporteVida( rows, cols )
        self.__contador = 1

    def configure( self, inicial, generaciones ):
        self.__tablero.configure( inicial, generaciones )

    def to_string( self ):
        self.__tablero.to_string()
    
    def get_gens( self ):
        return self.__tablero.get_gens()

#Aquí se definen las reglas, para matar o que nazcan células
    
    def reglas( self, row, col ):
        vecinos = self.__tablero.get_alive_neighbors( row, col )
        if( self.__tablero.is_alive_cell( row, col )):
            if( vecinos == 2 or vecinos == 3):
                return True
            else:
                return False
        else:
            if( vecinos == 3):
                return True
            else:
                return False

    def aplicarReglas( self ):
        nuevaConfig = []
        for i in range( self.__tablero.get_num_rows() ):
            for j in range( self.__tablero.get_num_cols() ):
                if(self.reglas( i, j )):
                    tupla = [i, j]
                    nuevaConfig.append(tupla)
        return nuevaConfig

    def iterarGeneracion( self ):
        if( self.__tablero.get_gens() > 1):
            self.__contador += 1
            arregloNuevaGen = self.aplicarReglas()
            self.__tablero.set_gens( self.__tablero.get_gens() -1 )
            self.__tablero.configure( arregloNuevaGen,  self.__tablero.get_gens())
            print(f"-------- {self.__contador}° Generación --------")
            self.to_string()
            self.iterarGeneracion()
    
def main():
    print("Juego de la vida \n")
    print("************************************************")
    rejillax=int(input("¿Cuantas filas deseas en tu comunidad? "))
    rejillay=int(input("¿Cuántas columnas deseas en tu comunidad? "))
    # vivas=int(input("¿Cuántas celulas vivas deseas al inicio? ")) # Quería ponerle el número de células vivas y su posición, pero nos dio menos tiempo :s
    
    generaciones=int(input("¿Cuántas generaciones deseas visualizar? "))
    part1 = Juego( rejillax, rejillay )
    part1.configure( [[1,2],[2,1],[2,2],[2,3]], generaciones )
    print("-------- 1° Generación --------")
    part1.to_string()
    part1.iterarGeneracion()

main()

import xlrd
def Ingresar_documento(archivo):
    for anio in range(1985,2019,1):
        archivo.append(xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+"Precip.xls"))
    return archivo

def obtener_rangos(hoja, archivo):
    for a in range(0,34,1):
        hoja.append(archivo[a].sheet_by_index(0))
    return hoja
def buscar_en_todos_los_excel(hoja,anio, entidad, mes):
    temp=anio-1985
    return hoja[temp].cell_value(entidad,mes)
def validar_entidades_y_nombrarlas():
    print("""
1 --> Aguascalientas                  2 --> Baja California
3 --> Baja California Sur          4 --> Campeche
5 --> Coahuila                            6 --> Colima
7 --> Chiapas                             8 --> Chihuahua
9 --> Distrito Federal                10 --> Durango
11--> Guanajuato                      12 --> Guerrero
13 --> Hidalgo                           14 --> Jalisco
15 --> Estado de México           16 --> Michoacán
17 --> Morelos                           18 --> Nayarit
19 --> Nuevo León                     20 ---> Oaxaca
21 --> Puebla                              22 --> Querétaro
23 --> Quintana Roo                  24 --> San Luis Potosí
25 --> Sinaloa                             26 --> Sonora
27 --> Tabasco                           28 --> Tamaulipas
29 --> Tlaxcala                           30 --> Veracruz
31 --> Yucatán                            32 --> Zacatecas
""")
    while(True):
        entidad= int(input("Ingresa el estado que deseas consultar: "))
        if entidad>=33 or entidad<=0:
            print("Número erróneo, favor de ingresar un número válido.")
            pass
        else:
            return entidad+1
            break
def promedio_de_entidad_por_anio(entidad,hoja):
    entidad_promedio=[]
    for x in range(0,34,1):
        entidad_promedio.append(hoja[x].cell_value(entidad,13))
        pass
    return entidad_promedio
def promedio_por_anio(hoja):
    temp = 0
    promedio_anios=[]
    for x in range(0,34,1):
        promedio_anios.append(hoja[x].cell_value(34,13))
        pass
    return promedio_anios


def menu():
    
    print("""
1. Consulta del promedio de precipaciones de cada entidad por año.
2. Consulta un valor específico por año y por mes.
3. Salir
""")
    


if __name__ == "__main__":
    menu()
    cont=1985
    archivo_local=[]
    ar_local=Ingresar_documento(archivo_local)
    hoja_local=[]
    hoja_local=obtener_rangos(hoja_local,ar_local)
    while True:
        op = int(input("Ingresa la opción que deseas consultar: "))
       
        if op == 1:
            cont=1985
            entidad=validar_entidades_y_nombrarlas()
            promediodeentidadporanio= promedio_de_entidad_por_anio(entidad, hoja_local)
            for x in promediodeentidadporanio:
                print(f"{cont}: |{x}|")
                cont+=1
                pass
            print("""
1. Consulta del promedio de precipaciones de cada entidad por año.
2. Consulta un valor específico por año y por mes.
3. Salir
""")            
            pass
           
        if op == 2:
            anio = int(input("Ingresa el año que deseas consultar: "))
            entidad = validar_entidades_y_nombrarlas()
            print("""
1-Enero            2-Febrero     3-Marzo            4-Abril
5-Mayo             6-Junio         7-Julio               8-Agosto
9-Septiembre   10-Octubre   11-Noviembre   12-Diciembre
""")
            mes = int(input("Ingresa el mes que deseas consultar: "))
            buscarenexcel= buscar_en_todos_los_excel(hoja_local,anio,entidad, mes)
            print(f"El promedio de lluvias fue de {buscarenexcel}")
            print("""
1. Consulta del promedio de precipaciones de cada entidad por año.
2. Consulta un valor específico por año y por mes.
3. Salir
""")
            
            pass
        
        if op == 3:
            print("Se va")
            exit()

    

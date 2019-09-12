ico={
    'Facultad':'FES_Aragon',
    'Area':"1_Fisico_Matematicas",
    'Plan':2011,
    'Dependencia':'Ingenieria',
    'Semestres':[]}

print(ico)

print('***************************************** \n')

primero={
    'Semestre':'Primero',
    "Introduccion_ingenieria_computación":1112,
    "Calculo_diferencia_e_integral":1113,
    'Algebra':1114,
    "Geometria_analitica":1115}

ico['Semestres'].append(primero)



segundo={
    'Semestre':'Segundo',
    "Calculo_Vectorial":'0065',
    "Algebra_lineal":'0062',
    "Comunicacion_oral_y_escrita":1202,
    "Programacion_orientada_a_objetos":1203,
    }

ico['Semestres'].append(segundo)

tercero={
    'Semestre':'Tercero',
    "Ecuaciones_diferenciales":'0066',
    "Metodos_numericos":'0067',
    "Estructura_de_datos":1302,
    "Introducción_a_la_economia":1303,
    "Electricidad_y_magnetismo":1304
    }
ico['Semestres'].append(tercero)

cuarto={
    'Semestre':'Cuarto',
    "Probabilidad_y_estadistica":'0069',
    "Investigacion_de_operaciones_y_sistemas":1402,
    "Estructuras_discretas":1403,
    "Ingenieria_economica":1404,
    "Analisis_de_circuitos":1405
    }
ico['Semestres'].append(cuarto)

quinto={
    'Semestre':'Quinto',
    "Diseño_y_analisis_de_algoritmos":1500,
    "Lenguajes_formales_y_automatas":'0442',
    "Dispositivos_electronicos":1501,
    "Programacion_de_sistemas":1502
    }
ico['Semestres'].append(quinto)

print(ico)
print('\n')
print("Fin del programa")
    

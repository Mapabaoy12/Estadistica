import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
matriculas = pd.read_excel('14_MATRICULAS_ED_SUPERIOR_LOS_LAGOS_2021.xlsx')
def tablin(variable):
    #Frecuencia Absoluta
    f = matriculas[variable].value_counts().sort_index()
    #Frecuencia Absoluta Acumulada
    F = f.cumsum()
    #Frecuencia Relativa
    h = (f/len(matriculas))*100
    #Frecuencia Relativa Acumulada
    H = (f.cumsum()/len(matriculas))*100
    #Tabla de frecuencias con la variable definida en los parametros
    tablaf = pd.DataFrame({
    'Frec. Absoluta': f,
    'Frec.relativa (%)': round(h),
    'Frec. Abs. Acumulada': F,
    'Frec. Rel. Acumulada':round(H)
    })
    return tablaf
print(matriculas.groupby('TIPO DE INSTITUCION'))
#Tabla de frecuencias segun tipo de institucion
print(f"Matriculas segun la variable tipo de institucion : \n{tablin('TIPO DE INSTITUCION')}")

#Promedio de la matricula segun institucion
promedios_tipo = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].mean()
print("---")
print(f"Promedio valor matricula segun tipo de institucion : \n{promedios_tipo}")
#moda
moda = matriculas['TIPO DE INSTITUCION'].mode()
print(f"La moda de la variable tipo de institucion es : \n{moda[0]}")
print("---")
#mediana
mediana = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].median()
print(f"La mediana de la variable tipo de institucion es : \n{mediana}")
print("---")
#Percentil 30 de los tipos de institucion
percentil_30 = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].quantile(0.3)
print(f"El percentil 30 de la variable valor matricula (pesos) es : \n{percentil_30}")
print("---")
#Cuartil 1 de los tipos de institucion
cuartil_1 = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].quantile(0.25)
print(f"El cuartil 1 de la variable valor matricula (pesos) es : \n{cuartil_1}")
print("---")
#Rango de la variable valor matricula (pesos) segun tipo de institucion
rango = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].agg(lambda x: x.max() - x.min())
print(f"El rango de la variable valor matricula (pesos) es : \n{rango}")
print("---")
#Varianza de la variable valor matricula (pesos) segun tipo de institucion      
varianza = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].var()
print(f"La varianza de la variable valor matricula (pesos) es : \n{varianza}")
print("---")
#Desviacion Estandar de la variable valor matricula (pesos) segun tipo de institucion
desviacion = matriculas.groupby('TIPO DE INSTITUCION')['VALOR MATRICULA (PESOS)'].std()
print(f"La desviacion estandar de la variable valor matricula (pesos) es : \n{desviacion}")
print("---")
#Coeficiente de variacion de la variable valor matricula (pesos) segun tipo de institucion
coeficiente = (desviacion/promedios_tipo)*100   
print(f"El coeficiente de variacion de la variable valor matricula (pesos) es : \n{coeficiente}")

#Histograma de la variable edad por si acas
matriculas['EDAD'].plot.hist(bins=10, color='#F2AB6D', rwidth=0.85)#Esto lo copie de googley le cambio los datos, por si las dudas, asi que no cacho que tambien estara, hell yea gell trea traba hell
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.title('Histograma de edades de matrícula')
plt.show()



#preguntas items 2
#1.¿Hay áreas del conocimiento donde las carreras sean más caras?
promedios_area = matriculas.groupby('AREA CONOCIMIENTO')['VALOR MATRICULA (PESOS)'].mean()
print(f"Promedio valor matricula segun tipo de institucion : \n{promedios_area}")
print("---")
#2.¿Qué influencia tiene la edad en el tipo de institución a la que ingresan los estudiantes?
promedio_edad = matriculas.groupby('TIPO DE INSTITUCION')['EDAD'].mean()
mediana_edad = matriculas.groupby('TIPO DE INSTITUCION')['EDAD'].median()
print("Promedio de edad por tipo de institución:\n", promedio_edad)
print("Mediana de edad por tipo de institución:\n", mediana_edad)
print("---")
#No se si sirvan esos datos para sacar la influencia pero demas que si, ahi lo dejo
#3.¿Hay carreras cuyo arancel sea sustantivamente más caro que la mayoría de los aranceles? ¿Qué explicación pueden encontrar? Consideren qué variables de la base de datos los puede ayudar y el contexto de la región que les tocó trabajar.
tablota = pd.pivot_table(
    matriculas,
    values='VALOR ARANCEL (PESOS)',
    index='NOMBRE CARRERA',
    columns='REGION SEDE',
    aggfunc='mean'
)
print(round(tablota))#pivot table es una funcion de panda bien cool, index es para las filas de las tablas, value para los datos a resumir, colum define las columnas, y aggfuncion, como lo quieres resumir


#Les pongo las demas variables por si quieren verlas y si les tinca mas otra, no mas borren los corchetes
"""
#Genero
print(f"Matriculas segun la variable genero : \n{tablin('GENERO')}")
print(f"Matriculas segun la variable edad : \n{tablin('EDAD')}")
print(f"Matriculas segun la variable rango edad : \n{tablin('RANGO EDAD')}")
print(f"Matriculas segun la variable anio ingreso : \n{tablin('AÑO INGRESO')}")
print(f"Matriculas segun la variable semestre ingreso : \n{tablin('SEMESTRE INGRESO')}")
print(f"Matriculas segun la variable tipo de institucion : \n{tablin('TIPO DE INSTITUCION')}")
print(f"Matriculas segun la variable nombre de institucion : \n{tablin('NOMBRE DE INSTITUCION')}")
print(f"Matriculas segun la variable acreditacion institucional : \n{tablin('ACREDITACION INSTITUCIONAL')}")
print(f"Matriculas segun la variable periodo de acreditacion : \n{tablin('PERIODO DE ACREDITACION')}")
print(f"Matriculas segun la variable anios de acreditacion : \n{tablin('AÑOS DE ACREDITACION')}")
print(f"Matriculas segun la variable nombre carrera : \n{tablin('NOMBRE CARRERA')}")
print(f"Matriculas segun la variable requisito carrera : \n{tablin('REQUISITO INGRESO')}")
print(f"Matriculas segun la variable via de ingreso : \n{tablin('VIA DE INGRESO')}")
print(f"Matriculas segun la variable modalidad : \n{tablin('MODALIDAD')}")
print(f"Matriculas segun la variable jornada : \n{tablin('JORNADA')}")
print(f"Matriculas segun la variable tipo plan carrera : \n{tablin('TIPO PLAN CARRERA')}")
print(f"Matriculas segun la variable nivel de estudio de carrera : \n{tablin('NIVEL DE ESTUDIO CARRERA')}")
print(f"Matriculas segun la variable nivel carrera : \n{tablin('NIVEL CARRERA')}")
print(f"Matriculas segun la variable area conocimiento : \n{tablin('AREA CONOCIMIENTO')}")
print(f"Matriculas segun la variable duracion plan de estudio(semestres) : \n{tablin('DURACION PLAN DE ESTUDIO (SEMESTRES)')}")
print(f"Matriculas segun la variable duracion proceso titulacion(semestres) : \n{tablin('DURACION PROCESO TITULACION (SEMESTRES)')}")
print(f"Matriculas segun la variable duracion total carrera(semestres) : \n{tablin('DURACION TOTAL CARRERA (SEMESTRES)')}")
print(f"Matriculas segun la variable valor matricula(pesos) : \n{tablin('VALOR MATRICULA (PESOS)')}")
print(f"Matriculas segun la variable valor arancel(pesos) : \n{tablin('VALOR ARANCEL (PESOS)')}")
print(f"Matriculas segun la variable region sede : \n{tablin('REGION SEDE')}")
print(f"Matriculas segun la variable provincia sede : \n{tablin('PROVINCIA SEDE')}")
print(f"Matriculas segun la variable comuna sede : \n{tablin('COMUNA SEDE')}")
"""

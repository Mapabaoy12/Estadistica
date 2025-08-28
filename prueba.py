import matplotlib.pyplot as plot
import pandas as pd
"""
edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

datos = pd.Series(edades) # cargamos los datos en un objeto Series
intervalos = range(min(datos), max(datos) + 2)  # calculamos los extremos de los intervalos

datos.plot.hist(bins=8, color='#F2AB6D', rwidth=0.85) # generamos el histograma a partir de los datos
plot.xticks(intervalos)
plot.ylabel('Frecuencia')
plot.xlabel('Edades')
plot.title('Histograma de edades - pandas - codigopiton.com')

plot.show()
"""
print((2.1+3.2+2.8+4.2+3.2+3.5+2.9)/7)
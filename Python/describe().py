import pandas as pd 

csv = 'Python/introduccion a machine learning/melb_data.csv'
#Guardar los datos y almacenarlos en el dataframe llamado melbourne_data
melbourne_data = pd.read_csv(csv)
#Resumen de los datos de Melboure
print('=====================================================')
print('================== FUNSION DESCRIBE =================')
print(f'=====================================================\n{melbourne_data.describe()}')
#El resultado muestra 8 filas,
#la primera COUNT muestra cuantas filas tienen datos no nulos o vacios
#MEAN es el promedio,
#STD es la derivacion estandar, que mide cuán dispersos numpericamente están los valores.
# para interpretar min, 25%, 50%, 75% y max, imagina la lista organizada de el mas pequeño al mas grande,
# el primer valor es el minimo, si var a un cuarto de la lista encontraras un numero que es mas grande que el 25% de los valores y mas pequeños que el 75%.
# los 50% y 75% se definen de forma analoga y el max es el numero mas grande.

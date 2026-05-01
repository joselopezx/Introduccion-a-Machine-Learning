from sklearn.tree import DecisionTreeRegressor
import pandas as pd 

csv = 'Python/introduccion a machine learning/melb_data.csv'
#Guardar los datos y almacenarlos en el dataframe llamado melbourne_data
melbourne_data = pd.read_csv(csv)
#Resumen de los datos de Melboure

print(melbourne_data.head())
print('=====================================================')
print('================== FUNSION DESCRIBE =================')
print(f'======================================================\n{melbourne_data.describe()}')

print('=====================================================')
print('===================== COLUMNAS ======================')
print(f'======================================================\n{melbourne_data.columns}')
#Los datos de Melburne tienen algunos valores faltantes (algunas casas de algunas variables no fueron recolectadas.)
#dropna elimina valores faltantes (piensa en na comoo 'not available')

melbourne_data = melbourne_data.dropna(axis=0)

#Seleccionando el target de prediccion
#El target de prediccion es llamada y.
y = melbourne_data.Price

#Escogiendo 'FEATURES'
#Las columnas que estan en nuestro modelo (y despues usadas para hacer predicciones)
#son llamadas 'features'
#Seleccionamos multiples 'features', dando una lista de nombres de columnas dentro de brackets [ ].
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
#por convencion estos datos son llamados X
X = melbourne_data[melbourne_features]

#Usando los metodos describe y head, se hace una vista rapida a los datos que se usaran para predecir los precios de las casas.
print('======================================================')
print('===================== DESCRIBE X =====================')
print(f'======================================================\n{X.describe()}')

print('======================================================')
print('======================== HEAD X ======================')
print(f'======================================================\n{X.head()}')

print('======================================================')
print('=============== CREACION DEL MODELO ==================')
print('======================================================')

#Defininedo el modelo, especificando un numero de random_state para asegurar el mismo resultado en cada ejecución.
melbourne_model = DecisionTreeRegressor(random_state=1)

#Fit model
melbourne_model.fit(X, y)

print('======================================================')
print('== HACIENDO PREDICCIONES DE LAS SIGUEINTES 5 CASAS ===')
print('======================================================')

print('===================== HEAD DE X ======================')
print(X.head())

print('================ Las predicciones son ================')
print(melbourne_model.predict(X.head()))

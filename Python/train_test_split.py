from sklearn.tree import DecisionTreeRegressor
import pandas as pd 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

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

#========================================================
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

melbourne_model = DecisionTreeRegressor(random_state=1)

#Fit model
melbourne_model.fit(train_X, train_y)

print('======================================================')
print('== HACIENDO PREDICCIONES DE LAS SIGUEINTES 5 CASAS ===')
print('======================================================')

val_predictions = melbourne_model.predict(val_X)
#MAE
print('======================================================')
print('=============== HACIENDO USO DE "MAE" ================')
print('======================================================')
print(f'================ Las predicciones son ================\n{mean_absolute_error(val_y, val_predictions)}')


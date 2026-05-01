#install.packages('psych')
#install.packages('rpart')
library('rpart')
library('tidyverse')
library('psych')

csv<-'C:/Users/USER/Desktop/Codigos/R/introduccion a machine learning/melb_data.csv'
#Guardar los datos y almacenarlos en el dataframe llamado melbourne_data
melbourne_data <- read_csv(csv)

head(melbourne_data)

print('=====================================================')
print('================== FUNSION DESCRIBE =================')
print('=====================================================')
describe(melbourne_data)

print('=====================================================')
print('================== FUNSION SUMMARY  =================')
print('=====================================================')
summary(melbourne_data)

print('=====================================================')
print('======================= COLUMNAS ====================')
print('=====================================================')
colnames(melbourne_data)

#Los datos de Melburne tienen algunos valores faltantes (algunas casas de algunas variables no fueron recolectadas.)
#na.omit es el equivalente a dropna de python, para eliminar cualquier fila con na
melbourne_data <- na.omit(melbourne_data)

#Seleccionando el target de prediccion
#El target de prediccion es llamada y.
y <- melbourne_data$Price

#Escogiendo 'FEATURES'
#Las columnas que estan en nuestro modelo (y despues usadas para hacer predicciones)
#son llamadas 'features'
#Seleccionamos multiples 'features', dando una lista de nombres de columnas dentro de c ( ).
melbourne_features <- c('Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude')
#por convencion estos datos son llamados X
X <- melbourne_data[, melbourne_features]

#Usando los metodos describe y head, se hace una vista rapida a los datos que se usaran para predecir los precios de las casas.
print('=====================================================')
print('====================== X SUMMARY  ===================')
print('=====================================================')
summary(X)

print('=====================================================')
print('======================== HEAD X  ====================')
print('=====================================================')
head(X)

print('=====================================================')
print('================= CREACION DEL MODELO ===============')
print('=====================================================')

#Defininedo el modelo, especificando un numero de set.seed para asegurar el mismo resultado en cada ejecución.
set.seed(1) #Equivalente a random_state = 1
melbourne_model <- rpart(Price ~ Rooms + Bathroom + Landsize + Lattitude + Longtitude, 
                         data = melbourne_data, 
                         control = rpart.control(minsplit = 2, cp = 0))
#En R, el "fit" ocurre automáticamente en el momento en que ejecutas la función del modelo (en este caso rpart).
#No hay una función .fit() separada.

cat("======================================================\n")
cat("== HACIENDO PREDICCIONES DE LAS SIGUIENTES 5 CASAS ===\n")
cat("======================================================\n")

print('======================== HEAD X  ====================')
head(X, 5)

print("================ Las predicciones son ================")
print(predict(melbourne_model, head(X,5)))

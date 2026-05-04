>[!NOTE]
>Kagle curso -> https://www.kaggle.com/learn/intro-to-machine-learning.  
>Para intalar la libreria Pandas en Windows use el CMD y escriba `pip install pandas`.  
>`pip install scikit-learn` para instalar los modelos de sklearn.

Pandas ua herramienta muy usada para la exploracion de los datos y su manipulación, una forma de exportarla y hacer uso de esta libreria es abreviarla como `pd`  
`import pandas as pd`  
La parte mas importante de la libreria es el **DataFrame** similar a las tablas en excel, o una base de datos SQL.  
La forma de leer un CSV es `pd.read_csv(ruta del csv)` desearas almacenar esta lectura en una variable para poder trabajar con ella.  

## Mean Absolute Error MAE
Empezando por la utima palabra, error.  
El error predicho es `error = actual - predicted`  
Con **MAE**, tomamos el valor absoluto '| |' de cada error. Esto conviete cada error en un valor positivo. Despues tomamos el promedio de esos errores absolutos. esto es nuestro *measure of model quality* 

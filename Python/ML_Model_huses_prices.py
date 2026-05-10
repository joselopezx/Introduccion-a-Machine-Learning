from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import random as rd

csv = 'Python/introduccion a machine learning/train.csv'

df = pd.read_csv(csv)

#print(df.info())

#correlacion = df.corr(numeric_only=True)

#print(correlacion)

#correlacion.to_csv('Python/introduccion a machine learning/correlacion.csv')

features = ['OverallQual', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea', 'FullBath', 'TotRmsAbvGrd', 
            'GarageCars', 'HalfBath', 'GarageArea', 'LotArea', 'LotFrontage', 'Fireplaces']

X = df[features]
y = df.SalePrice

def model (test_siz, n_estim, max_dep):
    train_x, test_x, train_y, test_y = train_test_split(X, y, random_state=1, test_size=test_siz)

    df_model = RandomForestRegressor(random_state=1, n_estimators=n_estim, max_depth=max_dep)

    df_model.fit(train_x, train_y)

    y_predc = df_model.predict(test_x)

    print(f'size :{test_siz}, n_est :{n_estim}, max : {max_dep}')
    print(mean_absolute_error(test_y, y_predc))


model(0.7, 170, 10)
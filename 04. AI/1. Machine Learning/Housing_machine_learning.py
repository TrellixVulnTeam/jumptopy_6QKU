import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

housing_file_path = 'housing.csv'
housing = pd.read_csv(housing_file_path)

housing = housing.replace('yes', 1)
housing = housing.replace('no', 0)


housing_price_data = housing.price

housing_price_datalist = []
housing_price_predict_list = []
i = 0
while True:
    if i != 5:
        housing_price_datalist.append(housing_price_data[i])
        i = i + 1
    else:
        break

housing_predictors = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway',
       'recroom', 'fullbase', 'gashw', 'airco', 'garagepl', 'prefarea']

y = housing_price_data
X = housing[housing_predictors]

housing_model = DecisionTreeRegressor()
housing_model.fit(X,y)

t = 0
while True:
    if t != 5:
        housing_price_predict_list.append(housing_model.predict(X.head())[t])
        t = t + 1
    else:
        break

print(housing_price_predict_list)

A = housing_price_datalist
B = housing_price_predict_list
result_value = 0
for value in [x - y for x, y in zip(A, B)]:
    result_value += value **2
count_value = result_value / len(A)

print("Cost Function : %s" % count_value)
"""                 m
Cost function = 1/m ∑ ( 선값(x) - 실제값(x) ) ^2
                   i=1
"""


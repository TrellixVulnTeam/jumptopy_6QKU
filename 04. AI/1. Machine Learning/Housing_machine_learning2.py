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

for price_data in housing_price_data:
    housing_price_datalist.append(price_data)

housing_predictors = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway',
       'recroom', 'fullbase', 'gashw', 'airco', 'garagepl', 'prefarea']

y = housing_price_data
X = housing[housing_predictors]

housing_model = DecisionTreeRegressor()
housing_model.fit(X,y)
t = 0
while True:
    if t != 546:
        housing_price_predict_list.append(housing_model.predict(X.head(546))[t])
        t = t + 1
    else:
        break
# for predict_price in

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


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

housing = pd.read_csv('Housing.csv', sep=',', header=0)

housing = housing.replace('yes', 1)
housing = housing.replace('no', 0)

print(housing.head())
my_formula = 'price ~ lotsize + bedrooms + bathrms + stories + driveway + recroom \
+ fullbase + gashw + airco + garagepl + prefarea'
lm = ols(my_formula, data=housing).fit_regularized()


dependant_variable = housing['price']
independent_variables = housing[housing.columns.difference(['price'])]
independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
housing_standardized = pd.concat([dependant_variable, independent_variables_standardized], axis=1)

lm_standardized = ols(my_formula, data=housing_standardized ).fit_regularized()
print("\nCoefficients:\n%s" % lm_standardized.params)
new_observations = housing.ix[housing.index.isin(range(10)),independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

def inverse_logit(model_formula):
	from math import exp
	return (1.0 / (1.0 + exp(-model_formula)))*100.0

iris = pd.read_csv('iris.csv', sep=',', header=0)
iris.columns = [heading.lower() for heading in \
iris.columns.str.replace('.', '_').str.replace("\'", "").str.strip('?')]
print(iris.head())
print(iris.describe())
# dependent_variable = iris['variety']
dependent_variable = iris['is_setosa']
independent_variables = iris[['sepal_length','sepal_width','petal_length','petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
# logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit()

# print("\nQuantities you can extract from the result:\n%s" % dir(logit_model))
# print("\nCoefficients:\n%s" % logit_model.params)
# print("\nCoefficient Std Errors:\n%s" % logit_model.bse)
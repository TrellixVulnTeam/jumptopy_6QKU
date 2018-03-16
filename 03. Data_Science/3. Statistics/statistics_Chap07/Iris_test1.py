import numpy as np
import pandas as pd
import statsmodels.api as sm
import random

# 데이터셋을 데이터 프레임으로 읽음
iris = pd.read_csv('iris.csv',sep=',', header=0)
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace(".","_")]

iris['iris01'] = np.where(iris['variety'] == 'Setosa',1.,0.)
# print(iris.head())
# 그룹별 기술 통계 구하기
# print(iris.groupby(['variety'])[['sepal_length','sepal_width','petal_length','petal_width']].agg(['count','mean','std']))

dependent_variable = iris['iris01']
independent_variables = iris[['sepal_length','sepal_width','petal_length','petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
#
# print(dependent_variable)
# print(independent_variables_with_constant)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()
# print(logit_model.summary())
#
new_observations = iris.ix[iris.index.isin(random.sample(range(150),10)), independent_variables.columns]
new_observations_with_constant = sm.add_constant(new_observations, prepend=True)
y_predicted = logit_model.predict(new_observations_with_constant)
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
result = []
for i in y_predicted_rounded:
    if i == 1.0:
        result.append('Setosa')
    else:
        result.append('Versicolor')
print(result)


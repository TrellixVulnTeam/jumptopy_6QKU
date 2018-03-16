import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv',sep=',', header=0)

dependent_variable = iris['name']
# print(dependent_variable)
independent_variables = iris[['sepallength','sepalwidth','petallength','petalwidth']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)
# print(independent_variables_with_constant)

logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()
print(logit_model)
# new_observations = iris.ix[iris.index.isin(range(100)), independent_variables.columns]
# new_observations_with_constant = sm.add_constant(new_observations, prepend=True)

train_data, test_data, train_label, test_label = \
train_test_split(independent_variables, dependent_variable)
# train_test_split(independent_variables_with_constant, dependent_variable)

# 데이터 학습시키고 예측하기 --- (※4)
logit_model = sm.Logit(dependent_variable, independent_variables_with_constant).fit_regularized()
y_predicted = logit_model.predict(test_data)
# y_predicted_rounded = [round(score, 2) for score in y_predicted]

# 정답률 구하기 --- (※5)
ac_score = metrics.accuracy_score(test_label, y_predicted)
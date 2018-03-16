import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
# 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
iris = pd.read_csv('iris2.csv',sep=',', header=0)
iris.columns = [heading.lower() for heading in \
                iris.columns.str.replace(".","_")]

iris['iris01'] = np.where(iris['variety'] == 'Versicolor',1,0)

dependent_variable = iris['iris01']
independent_variables = iris[['sepal_length','sepal_width','petal_length','petal_width']]
independent_variables_with_constant = sm.add_constant(independent_variables, prepend=True)

# 학습 전용 데이터와 테스트 전용 데이터로 나누기 --- (※3)
train_data, test_data, train_label, test_label = \
train_test_split(independent_variables_with_constant, dependent_variable )
# 데이터 학습시키고 예측하기 --- (※4)
logit_model = sm.Logit(train_label, train_data).fit_regularized()
# logit_model = sm.Logit(train_label, train_data).fit_regularized()
pre = logit_model.predict(test_data)
# 정답률 구하기 --- (※5)
print("예측값 출력")

y_predicted_rounded = [round(score) for score in pre]

index = 0
correct_score=0
for pridicted_value in y_predicted_rounded:
    if pridicted_value:
        print("%d번째 샘플링 데이터 예측 결과 %f : Versicolor 확실 "%(index+1,pridicted_value),end='')
        if y_predicted_rounded[index]:
            correct_score +=1
            print("\t"*3+" => 예측 결과 정답")
        else:
            print("\t"*3+" => 예측 결과 오답")
    else:
        print("%d번째 샘플링 데이터 예측 결과 %f : Versicolor 아닌 다른 품종"%(index,pridicted_value), end='')
        if not y_predicted_rounded[index]:
            correct_score += 1
            print("\t => 예측 결과 정답")
        else:
            print(" => 예측 결과 오답")
    index+=1


# ac_score = metrics.accuracy_score(test_label, pre)
print("전체 데이터 수: %d"%(len(iris)))
print("학습 전용 데이터 수: %d"%(len(train_data)))
print("테스트 데이터 수: %d"%(len(test_data)))
print("정답률 =", correct_score/len(test_data))



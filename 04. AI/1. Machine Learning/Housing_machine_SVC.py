### Housing - 예측값 구하기

import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

housing_file_path = 'housing.csv'
housing = pd.read_csv(housing_file_path)        ## pandas의 read_csv() 함수를 사용하여 CSV 파일을 읽어 데이터프레임에 넣는다.
# print(housing.columns)
housing = housing.replace('yes', 1)
housing = housing.replace('no', 0)

## 필요한 열 추출하기 --- (※2)
housing_data = housing[['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway', 'recroom',
                      'fullbase', 'gashw','airco', 'garagepl', 'prefarea']]
housing_label = housing["price"]

## 학습 전용 데이터와 테스트 전용 데이터로 나누기 --- (※3)
train_data, test_data, train_label, test_label = train_test_split(housing_data, housing_label)

## 데이터 학습시키고 예측하기 --- (※4)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

## 정답률 구하기 --- (※5)
ac_score = metrics.accuracy_score(test_label, pre)

print("전체 데이터 수 : %d" % (len(housing_data)))
print("학습 전용 데이터 수 : %d" % (len(train_data)))
print("테스트 데이터 수 : %d" % (len(test_data)))
print("정답률 = ", ac_score)
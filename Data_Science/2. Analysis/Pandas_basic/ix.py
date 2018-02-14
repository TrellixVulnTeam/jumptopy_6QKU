from pandas import Series, DataFrame
import pandas as pd

print("Step1] 기본 data frame 만들기")
data = {
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}

frame = DataFrame(data)
print(frame)

print("\nStep2] column 순서 정하기")
frame = DataFrame(data, columns = ['year','state','pop'])
print(frame)

print("\nStep3] row index 설정하기")
frame = DataFrame(data, columns = ['year','state','pop'],
                  index=['one','two','three','four','five'])
print(frame)

print("\nStep4] 특정 행(Row) 찾기 (ex: three) ")
print("특정 행(Row) 접근: frame.ix['three']")
three_row_data = frame.ix['three']
print(three_row_data)

print("특정 행(Row) 값 접근: frame.ix['three'].values")
three_row_data_value_list = frame.ix['three'].values
print(three_row_data_value_list)

print("특정 행(Row) 접근: frame.ix[2](frame.ix['three']와 같은 결과)")
year_column_values = frame.ix[2]
print(year_column_values)

print("\n프로그램 종료")

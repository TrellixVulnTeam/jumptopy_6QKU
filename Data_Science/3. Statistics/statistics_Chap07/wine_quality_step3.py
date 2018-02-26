#!/usr/bin/env python3
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm


# Read the data set into a pandas DataFrame
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())

# Display descriptive statistics for all variables
print(wine.describe())

# Identify unique values
print(sorted(wine.quality.unique()))

# Calculate value frequencies
print(wine.quality.value_counts())

# Display descriptive statistics for quality by wine type
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

# Look at the distribution of quality by wine type
red_wine = wine.ix[wine['type']=='red', 'quality']
white_wine = wine.ix[wine['type']=='white', 'quality']

sns.set_style("dark")
print(sns.distplot(red_wine, \
		norm_hist=True, kde=False, color="red", label="Red wine"))
print(sns.distplot(white_wine, \
		norm_hist=True, kde=False, color="white", label="White wine"))
# sns.axlabel("Quality Score", "Density")
plt.xlabel("Quality Score")
plt.ylabel("Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
# plt.show()

print("\n와인의 종류에 따라 품질의 차이 검정")
print(wine.groupby(['type'])[['quality']].agg(['std', 'mean']))
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f  pvalue: %.4f' % (tstat, pvalue))

print("\n"+'='*80)
print("7.2.3 상관관계 분석")
print("모든 변수 쌍 사이의 상관계수 구하기")
print(wine.corr())

def take_sample(data_frame, replace=False, n=200):
	return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]
reds = wine.loc[wine['type']=='red', :]
whites = wine.loc[wine['type']=='white', :]
reds_sample = take_sample(wine.loc[wine['type']=='red', :])
whites_sample = take_sample(wine.loc[wine['type']=='white', :])
wine_sample = pd.concat([reds_sample, whites_sample])
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1.,0.)

reds_sample = reds.ix[np.random.choice(reds.index, 100)]
whites_sample = whites.ix[np.random.choice(whites.index, 100)]
wine_sample = pd.concat([reds_sample, whites_sample], ignore_index=True)

print("\nprint: wine['in_sample']")
print(wine['in_sample'])
print("\nprint: pd.crosstab(wine.in_sample, wine.type, margins=True)")
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

sns.set_style("dark")
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False, "x_jitter": 0.25, "y_jitter": 0.25}, \
hue='type', diag_kind='hist', diag_kws={"bins": 10, "alpha": 1.0}, palette=dict(red="red", white="white"), \
markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
print("print: g")
print(g)
plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar', fontsize=14, \
		horizontalalignment='center', verticalalignment='top',
		x=0.5, y=0.999)
plt.show()
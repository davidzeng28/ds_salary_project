# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:30:28 2023

@author: David
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
df = pd.read_csv('eda_data.csv')


## choose relevant columns
df.columns

df_model = df[['avg_salary','Rating','Size', 'Type of ownership','Industry','Sector','Revenue','num_comp','employer_provided',
             'job_state','same_state','python_yn','spark','aws','excel','job_simp','seniority','desc_len']]
## get dummy data
df_dum = pd.get_dummies(df_model)
## train_test_split: train  and test set
X = df_dum.drop('avg_salary' , axis =1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state =42)
## multiple linear regression
X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score
lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train,y_train, scoring = 'neg_mean_absolute_error', cv =5))
## lasso regression
lm_l = Lasso(alpha = .13)
lm_l.fit(X_train, y_train)
np.mean(cross_val_score(lm_l, X_train,y_train, scoring = 'neg_mean_absolute_error', cv =5))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)
plt.show()

err= tuple(zip(alpha, error))
df_err = pd.DataFrame(err, columns =['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]
## XGBoost
import xgboost as xgb
xb = xgb.XGBRegressor()
np.mean(cross_val_score(xb, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 3))
## random forrest model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
#using randomize search for randomforest 
parameter_rf = {'n_estimators':range(10,400,10)}
gs_rf = RandomizedSearchCV(rf, parameter_rf, scoring='neg_mean_absolute_error', cv=5)
gs_rf.fit(X_train, y_train)
gs_rf.best_estimator_
gs_rf.best_score_

np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 3))
### tune model using gridsearchcv for XGBoost because it gave the best overall performance
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
params = {
        'min_child_weight': [1, 5, 10],
        'n_estimators': range(10, 300, 10),
        'max_depth': [3, 4, 5],
        'learning_rate': [0.1, 0.01, 0.05]
        }
gs = GridSearchCV(xb, params, scoring = 'neg_mean_absolute_error', cv =5)
gs.fit(X_train, y_train)
gs.best_score_
gs.best_estimator_
## test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf1 = gs_rf.best_estimator_.predict(X_test)
tpred_xb = gs.best_estimator_.predict(X_test)

### evaluate the model
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpred_lm)
mean_absolute_error(y_test, tpred_lml)
mean_absolute_error(y_test, tpred_rf1)
mean_absolute_error(y_test, tpred_xb)

import pickle 
pickl = {'model': gs.best_estimator_}
pickle.dump(pickl, open('model_file'+".p","wb"))

file_name ="model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
    
list(X_test.iloc[1,:])



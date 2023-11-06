import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import auc, roc_auc_score

from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier


import pickle



#PARAMETERS FOR TRAINING
max_depth = 10
min_L = 500




#DATA PREPARATION

dataset = pd.read_csv('smoking_driking_dataset_Ver01.csv')

drinker_smoker_values = {
    "Y": 0.0,
    "N": 1.0
}
dataset.DRK_YN = dataset.DRK_YN.map(drinker_smoker_values)


Full_train, df_test = train_test_split(dataset, test_size=0.20, random_state=1)
Full_train = Full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

df_train, df_val = train_test_split(Full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)

y_train = df_train.DRK_YN.values
y_test = df_test.DRK_YN.values
y_val = df_val.DRK_YN.values

del df_train['DRK_YN']
del df_test['DRK_YN']
del df_val['DRK_YN']


numerical = (list(df_train.dtypes[dataset.dtypes == 'float64'].index)) + (list(df_train.dtypes[df_train.dtypes == 'int64'].index))
categorical = list(df_train.dtypes[dataset.dtypes == 'object'].index)

#Train function

def train(full_train, y_train):
    train_dicts = full_train[numerical + categorical].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(train_dicts)

    model = DecisionTreeClassifier(criterion='gini',
                                   splitter='best',
                                   max_depth=max_depth,
                                    min_samples_leaf=min_L)
    model.fit(X_train, y_train)

    return dv, model


#Final training of the model

dv, model = train(df_train, y_train)

#saving the model

with open('drunk_or_not.bin', 'wb') as file_out:
    pickle.dump((dv, model), file_out)

import pandas as pd
import numpy as np
import os, sys

path_data1, file_train_data1 = 'data1', 'train_df_final.hdf5'
path_data2, file_train_data2 = 'data2', 'train_test.hdf'

file_train_data1 = os.path.join(path_data1, file_train_data1)
file_train_data2 = os.path.join(path_data2, file_train_data2)

# dfData1 = pd.read_hdf(file_train_data1)
# dfData2 = pd.read_hdf(file_train_data2)

dfData1 = pd.read_csv(file_train_data1.replace('.hdf5', '.csv'))
# dfData1.to_hdf(file_train_data1.replace('.hdf5', '.hd5'), 0)

dfData2 = pd.read_csv(os.path.join(path_data2, 'train.csv'))
# dfData2.to_hdf(os.path.join(path_data2, 'train.hd5'), 0)

print ('task1', dfData1.columns)
print ('task2', dfData2.columns)

print (dfData1.head(4))
print (dfData2.head(4))




fff = 11

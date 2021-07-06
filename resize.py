import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

#######################################################
# Importing time in seconds and the behavior at
# those corresponding times and sorting according to time

data = pd.read_excel(r'INPUT.xlsx')
data = data.replace(float('NaN'), -1)
#print(data)
time_arr = []
time_hrmin_arr = []
behaviour_arr = []

data_col_length = data.shape[0]
data_row_length = data.shape[1]

print(data_col_length)
print(data_row_length)

#datanumpy = data.values
#datanumpy = data.to_numpy()

#time_imported_arr = data.iloc[:, 1]
nantype = data.iloc[2,5]
print(data.iloc[2,5] == nantype)
#print(type(float('nan')))
col_index = 0
while col_index < data_col_length:
    row_index = 5
    while row_index < data_row_length:
        if data.iloc[col_index, row_index]!=-1:
            time_hrmin_arr.append(data['time'].iloc[col_index])
            time_arr.append(data['TIME (SEC)'].iloc[col_index])
            behaviour_arr.append(data.iloc[col_index, row_index])
        #print(row_index)
        row_index = row_index + 1
    #print(col_index)
    col_index = col_index + 1

Index = np.arange(0, len(time_arr), 1)

Columns =  ["time in s", "time", "behaviour"]

final_arr = np.array([time_arr, time_hrmin_arr, behaviour_arr])
final_arr = np.transpose(final_arr)

df = pd.DataFrame(final_arr, index = Index, columns = Columns)

print(df)

df.to_excel('new_data_OUTPUT.xlsx')


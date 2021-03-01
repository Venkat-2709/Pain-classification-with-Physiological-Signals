import pandas as pd
import pickle
import os
import sys

from dataCollection import collection
from classifier import preprocess
from plot import box_plot, line_plot


# Checking the command line parameter.
try:
    parameter = str(sys.argv[1])
    if parameter not in ['dia', 'sys', 'eda', 'res', 'all']:
        raise Exception

except Exception as e:
    print('Wrong Parameter.')
    raise
except BaseException:
    print('Parameter cannot be Empty.')
    raise

# Loading the dataset.
if os.path.isfile('DataSet'):
    data = open('DataSet', 'rb')
    dataset = pickle.load(data)
    data.close()
    print('Data File is Loaded.')
    # line_plot(dataset)            # For plotting the line graph.
else:
    dataset = pd.read_csv('Project1Data.csv', header=None, names=range(63443))
    data = open('DataSet', 'ab')
    pickle.dump(dataset, data)
    data.close()
    print('Data File is Loaded.')

# Preparing dataset for dia parameter.
if parameter == 'dia' or parameter == 'all':
    if os.path.isfile('DiaData'):
        data = open('DiaData', 'rb')
        diaDataset = pickle.load(data)
        data.close()
        X_dia = diaDataset.iloc[:, diaDataset.columns != 'Class']
        X = X_dia
        Y = diaDataset.iloc[:, 5]
    else:
        diaDataset = collection(dataset, parameter='dia')
        data = open('DiaData', 'ab')
        pickle.dump(diaDataset, data)
        data.close()
        X_dia = diaDataset.iloc[:, diaDataset.columns != 'Class']
        X = X_dia
        Y = diaDataset.iloc[:, 5]

# Preparing dataset for sys parameter.
if parameter == 'sys' or parameter == 'all':
    if os.path.isfile('SysData'):
        data = open('SysData', 'rb')
        sysDataset = pickle.load(data)
        data.close()
        X_sys = sysDataset.iloc[:, sysDataset.columns != 'Class']
        X = X_sys
        Y = sysDataset.iloc[:, 5]
    else:
        sysDataset = collection(dataset, parameter='sys')
        data = open('SysData', 'ab')
        pickle.dump(sysDataset, data)
        data.close()
        X_sys = sysDataset.iloc[:, sysDataset.columns != 'Class']
        X = X_sys
        Y = sysDataset.iloc[:, 5]

# Preparing dataset for eda parameter.
if parameter == 'eda' or parameter == 'all':
    if os.path.isfile('EdaData'):
        data = open('EdaData', 'rb')
        edaDataset = pickle.load(data)
        data.close()
        X_eda = edaDataset.iloc[:, edaDataset.columns != 'Class']
        X = X_eda
        Y = edaDataset.iloc[:, 5]
    else:
        edaDataset = collection(dataset, parameter='eda')
        data = open('EdaData', 'ab')
        pickle.dump(edaDataset, data)
        data.close()
        X_eda = edaDataset.iloc[:, edaDataset.columns != 'Class']
        X = X_eda
        Y = edaDataset.iloc[:, 5]

# Preparing dataset for res parameter.
if parameter == 'res' or parameter == 'all':
    if os.path.isfile('ResData'):
        data = open('ResData', 'rb')
        resDataset = pickle.load(data)
        data.close()
        X_res = resDataset.iloc[:, resDataset.columns != 'Class']
        X = X_res
        Y = resDataset.iloc[:, 5]
    else:
        resDataset = collection(dataset, parameter='res')
        data = open('ResData', 'ab')
        pickle.dump(resDataset, data)
        data.close()
        X_res = resDataset.iloc[:, resDataset.columns != 'Class']
        X = X_res
        Y = resDataset.iloc[:, 5]

# Preparing dataset for all parameter.
if parameter == 'all':
    allDataset = [X_dia, X_sys, X_eda, X_res]
    X = pd.concat(allDataset, axis=1)

# box_plot(X)           # For plotting the box plot.

print('Dataset for ' + str(parameter) + ' is processed.')
accuracy, precision, recall, matrix = preprocess(X, Y)          # Classifying the processed data.

# Printing the results.
print('Results')

print('The Average accuracy of the Classifier for ' + str(parameter) + ' is: ' + str(accuracy))
print('The Average precision is: ' + str(precision))
print('The Average recall is: ' + str(recall))
print('The Average confusion matrix is: ' + str(matrix))

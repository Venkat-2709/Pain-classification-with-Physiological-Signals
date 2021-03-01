import pandas as pd

from scipy.stats import entropy
from statistics import variance, mean


def collection(x, parameter):
    dataset = pd.DataFrame(columns=['Mean', 'Variance', 'Entropy', 'Max', 'Min', 'Class'])
    # Preparing the data for dia parameter.
    if parameter == 'dia':
        for index, row in x.iterrows():
            row = list(row)
            if row[1] == 'BP Dia_mmHg':
                calculation(row, dataset)

        return dataset

    # Preparing the data for sys parameter.
    elif parameter == 'sys':
        for index, row in x.iterrows():
            row = list(row)
            if row[1] == 'LA Systolic BP_mmHg':
                calculation(row, dataset)

        return dataset

    # Preparing the data for eda parameter.
    elif parameter == 'eda':
        for index, row in x.iterrows():
            row = list(row)
            if row[1] == 'EDA_microsiemens':
                calculation(row, dataset)

        return dataset

    # Preparing the data for res parameter.
    elif parameter == 'res':
        for index, row in x.iterrows():
            row = list(row)
            if row[1] == 'Respiration Rate_BPM':
                calculation(row, dataset)

        return dataset

    # Preparing the data for all parameter.
    else:
        for index, row in x.iterrows():
            row = list(row)
            calculation(row, dataset)

        return dataset


# Finding the features for each row in dataset.
def calculation(row, dataset):
    row_result = []
    data_row = row[3:]
    data_row = [x for x in data_row if str(x) != 'nan']
    data_row = [0 if x < 0 else x for x in data_row]
    row_result.append(mean(data_row))
    row_result.append(variance(data_row))
    row_result.append(entropy(data_row, base=2))
    row_result.append(max(data_row))
    row_result.append(min(data_row))
    row_result.append(row[2])
    row_result = [0 if str(x) == 'nan' else x for x in row_result]
    dataset.loc[len(dataset)] = row_result

    return dataset

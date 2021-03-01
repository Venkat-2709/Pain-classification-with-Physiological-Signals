# Pain-classification-with-Physiological-Signals

## Classifying pain from physiological data where data include Diastolic BP, Systolic BP, EDA, and Respiration.

### Step 1: Importing the Libraries
```
Numpy 
Pandas
Pickle
Sklearn
Scipy
```
### Step 2: Execute
To execute type the command in terminal followed by parameter - dia, sys, eda, res, all. Any one of the following.
```
python main.py <parameter>
```
If the parameter is dia then only the Diastolic BP from the data is used for classification.                                                                         
If the parameter is sys then only the Systolic BP from the data is used for classification.                                                                         
If the parameter is eda then only the EDA from the data is used for classification.                                                                                 
If the parameter is res then only the Respiration Rate from the data is used for classification.                                                                     
If the parameter is all then all the data is fused together and used for classification.

### Output
```
Results for LA Systolic BP_mmHg data
The Average accuracy of the Classifier for sys is: ​ 0.8916666666666666
The Average precision is: ​ 0.9212698412698412
The Average recall is: ​ 0.8804761904761905
The Average confusion matrix is: ​ [[5.4, 0.6], [0.7, 5.3]]
```

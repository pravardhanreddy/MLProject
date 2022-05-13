import pandas as pd
from pandas import DataFrame
import openpyxl

writer = pd.ExcelWriter('/Users/aparnak/Dropbox/Personal/Machine_Learning/test.xlsx', engine='openpyxl')
file = open('/Users/aparnak/Downloads/gaussian')
samples=[]
Gamma=[]
cost=[]
val_accuracy=[]
test_accuracy=[]
validation = 0.0
test = 0.0
for line in file:
    line = line.split()
    if "F" in line[0]:
        sample = line[2]
        gamma= line[5]
        c = line[8]
        samples.append(sample)
        Gamma.append(gamma)
        cost.append(c)
    if "***Validation" in line[0]:
        validation = next(file)
        val_accuracy.append(float(validation))
    if "***Test" in line[0]:
        test = next(file)     
        test_accuracy.append(float(test))
df = DataFrame({'Sample' : samples,'gamma': Gamma, 'cost': cost,'validation_accuracy': val_accuracy, 'test_accuracy': test_accuracy})
print (df)

df.to_excel(writer, sheet_name='gaussian', index=False)
writer.save() 

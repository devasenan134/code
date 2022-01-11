import sklearn
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.utils import shuffle


data = pd.read_csv("student-mat.csv", sep=";")

data = data[["Fjob", "age", "absences", "failures", "studytime", "G1", "G2", "G3"]]
print(data.head())


predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

print(x)

import numpy as np
import pandas as pd
from matplotlib.pyplot import plt
import seaborn as sb


file_path = "melb_data.csv"
melb_data = pd.read_csv(file_path)

print(melb_data.shape)
print(melb_data.info())
print(melb_data.describe())

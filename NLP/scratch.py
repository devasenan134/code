import pandas as pd

path = "C:/Users/devas/Desktop/CS/ML/NLP/bad-words.csv"
file = pd.read_csv(path)
file = file[:30]

print(file.iloc[5:10, 0])

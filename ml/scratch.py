import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melb_data = pd.read_csv("melb_data.csv")
# print(melb_data.iloc[:30, :5])

y = melb_data.Price

melb_features = ["Rooms", "Bathroom", "Landsize", "Lattitude", "Longtitude"]
x = melb_data[melb_features]


melb_model = DecisionTreeRegressor(random_state=1)

melb_model.fit(x, y)
print(melb_data.loc[:4, "Price"])
print("Making predictions for the following 5 houses:")
print(x.head())
print("The predictions are")
print(melb_model.predict(x.head()))

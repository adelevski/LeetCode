import csv
import pandas as pd

data = pd.read_csv('data science\electionpoll.csv')
mean = data["Workers' Party"].mean()
median = data["Workers' Party"].median()
std_dev = data.std(axis=0)
diff = data["Workers' Party"].max() - data["Workers' Party"].min()
allMax = data.max()
allMin = data.min()



print(mean)
print(median)
print(std_dev)
print(diff)
print(data["Workers' Party"].max())
print(data["Workers' Party"].min())
print(allMax)
print(allMin)


import pandas as pd
import matplotlib.pyplot as plt

#Load the csv file
df = pd.read_csv('hemisphereClean.csv')

counter = 0

for rows in len(df):
    counter +=1

print(counter)
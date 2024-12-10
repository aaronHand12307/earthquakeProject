import pandas as pd

df = pd.read_csv('Earthquake.csv')
print(df.info())
print(df.dtypes)

#removing empty columns
df = df.dropna(subset=["Latitude","Longitude"])

#Date Time fixing
df["Datetime"] = pd.to_datetime(df["Date"],utc=True,format='mixed')

#convert data types
df = df.convert_dtypes()
print(df.dtypes)
print(df.info())

df.to_csv("hemisphereClean.csv")




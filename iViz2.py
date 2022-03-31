import pandas as pd
import matplotlib as plt


dataframe = pd.read_csv('drinks.csv') # add csv file here
#will go ahead and create the code for the graphs that I choose to visualize
print(dataframe)

maxValue = dataframe.max()

print(maxValue)


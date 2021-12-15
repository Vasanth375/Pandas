'''
one of the most used method to see overview of dataframe
The head() method returns the headers and a specified number of rows, starting from the top.
'''
import pandas as pd
df=pd.read_csv("pandas/AnalyzingData/data.csv")

#if the number of rows is not specified, the head() method will return the top 5 rows.
print(df.head(10))

#tail(n) method is used to return n number rows from bottom
#tail() default will return last 5 rows
print(df.tail(10))

#info() provides information about data frame
print(df.info())

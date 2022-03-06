import pandas as pd
import os

# Pandas is used to analyze data
df=pd.read_csv("testing.csv")

#Printing CSV File Name with the help of OS Library
file_path=r"C:\Users\Dhiraj\Desktop\Collage\DSBDA\Pr1\testing.csv"
file_name=os.path.basename(file_path)
print("Performing operation on (",file_name,")- Stocks Dataset")

#describe() is used to view some basic statistical details 
# like percentile, mean, std etc. 
print("\n----Dataset Description-----")
print(df.describe())

#type() method returns class type of the argument(object) passed as parameter. type() 
print("\n----Dataset type-----")
print(type(df))

#The head() function is used to get the first n rows
print("\n----Head Data-----")
print(df.head(3))

#The tail() function is used to get the last n rows. 
print("\n----Tail Data-----")
print(df.tail(3))

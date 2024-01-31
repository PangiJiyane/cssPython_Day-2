# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:44:17 2024

@author: ccm
"""
#importing:pd can be named anything
import pandas as pd
file=pd.read_csv("iris.csv")
print(file)

#Absolute path:C:\Users\ccm\Day 2 Python Training
#Relative path:iris.csv
pf=pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#To give the data from the website headers
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
#Different file types 


#Text
file=pd.read_csv("Geospatial Data.txt", sep=";")

#Excel 
#file=pd.read_excel("residentdoctors.xlsx")

#Json
#file=pd.read_json("student_data.json")

#df= Dataframe;saves data in a table form
# url ="https://github.com/Asabele240701/css4_day02/blob/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
#ETL Stands form extraction, transfromation and loading 

#TRANSFROMATION 
df =pd.read_csv("country_data_index.csv",index_col=0)

#Inconsistent Data Types & Names
df=pd.read_excel("residentdoctors.xlsx")
#print(df)
print(df.info())
#adding a column
#\d digits from 0 to 9, the sign mean
#astype :to convert to object into an interger 
df["LOWER_AGE"]= df["AGEDIST"].str.extract('(\d+)-')
print (df.info())

df["LOWER_AGE"]=df["LOWER_AGE"].astype(int)
print(df.info())

#Working with dates 
#Read dates from Excel as string
df= pd.read_csv("time_series_data.csv",index_col=0)
print(df.info())

df['Date']=pd.to_datetime(df['Date'])
print (df.info())
df['Date']=pd.to_datetime(df['Date'],format="%d-%m%y")
print(df.info())

#Extracting dates 
df['Year']=df['Date'].dt.year 

"""
.str
.extract
.astype
.dt                      
Ways to manipulate your data from your column
"""
#Remove an error column from Excel
#df.drop(index=26, inplace=true 26 is the error position/column)

df=pd.read_csv('patient_data_dates.csv')
# Allows you to see all rows
pd.set_option('display.max_rows',None)

print(df)
df.drop(['Index'],inplace=True,axis=1)

#Applying Data Transformations
#Aggregation
df=pd.read_csv("iris.csv")
print(df.columns)
#print(df_names)
df["sepal_length_sq"]=df["sepal_length"]**2
#df["sepal_length_sq_2"]=df["sepal_length"].apply(lambada x:x**2)

#Append and Merge
df1=pd.read_csv("person_split1.csv")
df2=pd.read_csv("person_split2.csv")
 
# Concatenate the dataframes
df = pd.concat([df1, df2], ignore_index=True)

df1 = pd.read_csv('person_education.csv')
df2 = pd.read_csv('person_work.csv')

##Inner Join 
df_merge = pd.merge(df1,df2,on='id')
df_merge = pd.merge(df1, df2, on='id', how='outer')

#Filtering
# Filtering data
print(df[df['age'] > 30])
#CSV
df.to_csv("output/pulsar.csv") 





      
       


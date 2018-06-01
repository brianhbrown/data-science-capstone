import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("911.csv") #Read in the database of 911 calls
print(df.info()) #Check the info of the database
print()

print(df.head()) #Check the first 5 lines of the database
print()

print(df["zip"].value_counts().head(5)) #What are the top 5 zip codes?
print()

print(df["twp"].value_counts().head(5)) #What are the top 5 townships?
print()

print(df["title"].nunique()) #How many unique values in title column?
print()

df["Reason"] = df["title"].apply(lambda title: title.split(":")[0]) #Create a new column with the reason title
print(df["Reason"].value_counts()) #What is the breakdown of reasons?
print()

#sns.countplot(x="Reason", data=df, palette="viridis") #Create a category plot for reason
#plt.show()

print(type(df["timeStamp"].iloc[0])) #What is the datatype of the time column?  str
print()

df["timeStamp"] = pd.to_datetime(df["timeStamp"]) #convert time to datetime format
df["Hour"] = df["timeStamp"].apply(lambda time: time.hour) #create a new column for hours
df["Month"] = df["timeStamp"].apply(lambda time: time.month) #create a new column for months
df["Day of Week"] = df["timeStamp"].apply(lambda time: time.dayofweek) #create a new column for day of week
dmap = {0:"Mon", 1: "Tues", 2:"Wed", 3:"Thurs", 4:"Fri", 5:"Sat", 6:"Sun"} #create a mapping of day from numeric to str
df["Day of Week"] = df["Day of Week"].map(dmap) #remap day of week column

#sns.countplot(x="Day of Week", data=df, hue="Reason", palette="viridis") #plot day of week with reason as hue
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) #move legend off plot
#plt.show()

#sns.countplot(x="Month", data=df, hue="Reason", palette="viridis") #plot month with reason as hue
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.) #move legend off plot
#plt.show()

byMonth = df.groupby("Month").count() #groupy on the months
print(byMonth.head())
print()

#byMonth["twp"].plot() #plot months vs twp a lineplot
#plt.show()

#sns.lmplot(x="Month", y="twp", data=byMonth.reset_index()) #create a linear fit on the calls per month, rest on column index
#plt.show()

df["Date"] = df["timeStamp"].apply(lambda t: t.date()) #create a new column applying the date function to timeStamp
#byDate = df.groupby("Date").count()["twp"].plot() #groupby data vs 911 calls
#plt.tight_layout() #plot a tight layout to make it more readable
#plt.show()

#df[df["Reason"]=="Traffic"].groupby("Date").count()["twp"].plot() #create three separate plots for each reason
#plt.title("Traffic")
#plt.tight_layout()
#plt.show()

#df[df["Reason"]=="Fire"].groupby("Date").count()["twp"].plot()
#plt.title("Fire")
#plt.tight_layout()
#plt.show()

#df[df["Reason"]=="EMS"].groupby("Date").count()["twp"].plot()
#plt.title("EMS")
#plt.tight_layout()
#plt.show()

dayHour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack() #restructure the df so that the columns become the hours and the index becomes the days
print(dayHour.head()) #show the first 5 entries
print()

#plt.figure(figsize=(12,6))
#sns.heatmap(dayHour,cmap='viridis') #create a heatmap for the new dayHour frame
#plt.show()

#sns.clustermap(dayHour,cmap='viridis') #create a cluster map
#plt.show()

dayMonth = df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack() #restructure the df so that the columns become the months and the index becomes the days
print(dayMonth.head()) #show the first 5 entries
print()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis') #create a heatmap for the new dayMonth frame
plt.show()

sns.clustermap(dayMonth,cmap='viridis') #create a cluster map
plt.show()



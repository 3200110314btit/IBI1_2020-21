import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/users/13035/IBI1_2020-21/Practical7")
covid_data = pd.read_csv("full_data.csv")
#The code for importing the .csv file works
covid_data.iloc[0:12:2,]
print(covid_data.iloc[0:12:2,])
#There is correct code for showing all columns, and every second row between (and including) 0 and 10
ls_Afghanistan = covid_data['location'] == 'Afghanistan'
covid_data[covid_data['location']=='Afghanistan']
print(covid_data[covid_data['location']=='Afghanistan'].iloc[:,[0,1,4]])
#a Boolean to show “total cases” for all rows corresponding to Afghanistan
World_new_cases = covid_data[covid_data['location']=='World'].iloc[:,[2]]
print(World_new_cases.describe())
#mean and median of new cases is 8454.326087 and 2023.500000
plt.boxplot(World_new_cases,vert=False,whis=2,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False,boxprops={'color':'blue','facecolor':'purple'})
plt.title('new cases worldwide')
plt.show()
#a boxplot of new cases worldwide.
World_new_deaths= covid_data[covid_data['location']=='World'].iloc[:,[3]]
World_dates=covid_data.loc[(covid_data["location"]=="World"),"date"]
plt.plot(World_dates, World_new_cases,'ro',label="new cases")
plt.plot(World_dates, World_new_deaths,'yo',label="new deaths")
plt.xticks(World_dates.iloc[0:len(World_dates):5],rotation=90)
plt.legend()
plt.show()
#make a figure anout world new cases and world new deaths
plt.figure()
Total_cases=covid_data[covid_data["date"]=="2020-03-14"].iloc[:,[5]]
plt.boxplot(Total_cases,vert=True, whis=2,patch_artist=True,meanline=False,showbox=True,showcaps=True,showfliers=True,notch=False, boxprops={'color':'blue','facecolor':'purple'})
plt.title("Total cases boxplot")
plt.show()
#Plot a boxplot of total case numbers in different countries on 14 March 2020.
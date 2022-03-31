#import the libs
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


covid_data = pd.read_csv("full_data.csv")

# print(covid_data.head(5))
# # read the first 5 lines with statistic in the csv
#
# covid_data.info()
# #show the type, dtype, name of columns and rows,  memory usage and non-null count of the whole data
#
# print(covid_data.describe())
# #show the statistic charcteristics of the data
#
# print(covid_data.iloc[0,1])
# print(covid_data.loc[0,'location'])
# #take the string in the row 0 and column 1

# print(covid_data.iloc[2,0:5])#the second row and its dtype and type, column 0 to row 5
# print('-----------')
# print(covid_data.iloc[0:2,:])#row 0 to 2, all the columns
# print('-----------')
# print(covid_data.iloc[0:10:2,0:5])#row 0 to 10, print every one in two, column 0 to 5
# print('-----------')
# print(covid_data.iloc[0:3,[0,1,3]])#row 0 to 3, colume 0, 1 and 3
# print('-----------')
# my_columns = [True, True, False, True, False, False]
# print(covid_data.iloc[0:3,my_columns])#row 0 to 3, true means print, false means not print
# print('-----------')

# print(covid_data.loc[2:4,'date'])#print the date of row 2 to 4
# print('-----------')
#print(covid_data.loc[covid_data["location"]=="Afghanistan",:])#print the rows that their location called Afghanistan

china_new_data=covid_data.loc[covid_data["location"]=="China",["date","new_cases","new_deaths"]]
# print(china_new_data)
#choose the datas we want by defining the name
cases = np.average(china_new_data.loc[:,'new_cases'])
deaths = np.average(china_new_data.loc[:,'new_deaths'])
print(cases)#the average number of cases
print(deaths)#the average number of deaths
print(deaths/cases)#the ratio of death

# #make the boxplot that contains both cases and deaths
# plt.boxplot([china_new_data.loc[:,'new_cases'],china_new_data.loc[:,'new_deaths']], labels=['new_cases','new_deaths'], vert=True, whis = 1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True, showfliers=True)
# plt.show()

# china_dates=covid_data.loc[covid_data["location"]=="China","date"]
# china_new_cases = covid_data.loc[covid_data["location"]=="China","new_cases"]
# china_new_deaths = covid_data.loc[covid_data["location"]=="China","new_deaths"]
## the 3 steps above help choose the certain data in the whole file by using '==', True
# plt.plot(china_new_deaths, 'ro', china_new_cases,'b+')#+ and o define the shape of the dots, b or r define the color and they are in different color
# plt.show()
# x = china_dates
# y1 = china_new_cases
# y2 = china_new_deaths
# plt.plot(x,y1,'bo')
# plt.plot(x,y2,'ro')
# plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-90)
# #xticks is used to modify the value of the x axis, iloc[0:len(china_dates):4]means take the data from china_dates and take one every 4 number, rotation means rotate the date to vertical(90 angles)
# plt.show()

y1 = covid_data.loc[covid_data["location"]=="Korea","total_cases"]
y2 = covid_data.loc[covid_data["location"]=="Kenya","total_cases"]
y3 = covid_data.loc[covid_data["location"]=="Colombia","total_cases"]
x1 = covid_data.loc[covid_data["location"]=="Korea","date"]
x2 = covid_data.loc[covid_data["location"]=="Kenya","date"]
x3 = covid_data.loc[covid_data["location"]=="Colombia","date"]
#give value to the axises, to show the 3 sets of data in one plot
plt.plot(x1,y1,'bo')
plt.plot(x2,y2,'b+')
plt.plot(x3,y3,'ro')
#use bo, b+ and ro to differ the 3 countries
plt.xticks(x1,rotation=-90)
plt.xticks(x2,rotation=-90)
plt.xticks(x3,rotation=-90)
#to see the x axis more clearly.
plt.show()

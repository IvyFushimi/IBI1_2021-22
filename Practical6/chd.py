#Firstly we need to create a dictionary that contains all the datas. Because we need a whole output of the dictionary, so a subdictionary is needed under the main key. Then we create a scatter plot based on the dictionary. I was not quite sure that whether I make the code more complex, but it could run well at least.
#create a dict based on the data
dict = {'paternal_age:chd':{
    '30':'1.03',
    '35':'1.07',
    '40':'1.11',
    '45':'1.17',
    '50':'1.23',
    '55':'1.32',
    '60':'1.42',
    '65':'1.55',
    '70':'1.72',
    '75':'1.94'
}}
dict2 = dict['paternal_age:chd']
#print the dict
print('paternal_age:chd=',dict['paternal_age:chd'])
#print the age and get the return of the value of the risk
age = input('please input the age (choose one from 30,35,40,45,50,55,60,65,70,75)')
print('the risk is',dict2[age])

#get the graph of the scatter
import matplotlib.pyplot as plt#import the library of graphing
x = 30,35,40,45,50,55,60,65,70,75
y = dict2.values()
plt.scatter(x,y,marker='o')
plt.ylabel('the risk')
plt.xlabel('the ages')
plt.title('the relationship between the age and the correct risk of cardiovascular health in the offsprint')
plt.show()

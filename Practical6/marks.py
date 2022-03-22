#In this programme, both numpy and matplot are needed since we need a boxplot and the average value.The list was given so we could use it directly.
#import numpy
import  numpy as np
#create a list called 'marks'
marks=[45,36,86,57,53,92,65,45]
print('the marks are: ', sorted(marks))#print the sorted list
plt.boxplot(marks, vert=True, whis = 1.5, patch_artist=True, meanline=False, showbox=True, showcaps=True, showfliers=True, notch=False )
plt.show()#create and display the boxplot
ave = np.average(marks)#use numpy to calculate the average value
print(ave)#print the average value of marks
if ave > 60:
    print('passed')
else:
    print('failed')#compare the average mark with 60

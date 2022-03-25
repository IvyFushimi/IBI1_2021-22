a = 19245301#the number of 2022
b = 4218520#the number of 2021
c = 271#the number of 2020
d = b - c#the new cases in 2021
e = a - b#the new cases in 2022
if d > e:
	print("the rate of new cases of 2021 is greater")
elif d < e:
	print("the rate of new cases of 2022 is greater")#compare them and print the right answer

X = input('Boolean X = :')
Y = input('Boolean Y = :')#input 2 boolean value X and Y.
W = X and Y
print(W)

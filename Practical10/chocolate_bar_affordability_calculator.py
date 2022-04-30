#Chocolate bar affordability calculator
def result(total_money,price):
    bar = int(float(total_money) / float(price))
    change = float(total_money) - ((float(bar)) * (float(price)))
    print('bar = '+str(bar)+', change = '+str(change))
    return total_money,price
total_money = input('total_money = ')
price = input('price = ')
result(total_money,price)

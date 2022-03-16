# compute each value
#dots = 0
#n = int(input())
#while n > 0:#use loop to compute it
#	dots = dots + n
#	n = n-1
#print(dots)

N = int(input())#N is the sum of all triangles
dots = 0
DOTS = 0
n = N
while n > 0:
    dots = dots + n
    n = n-1
    N = N-1
    DOTS = DOTS + dots
print(DOTS)

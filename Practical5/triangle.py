
#the basic way to culculate the dots of each triangle
#dots = 0
#n = int(input())
#while n > 0:#use loop to compute it
#	dots = dots + n
#	n = n-1
#print(dots)

N = int(input('the number of triangles:'))#N is the number of triangles
dots = 0#the initial value
DOTS = 0#DOTS is the sum of the dots
while N > 0:
    dots = N*(N+1)/2#the dots each triangle have
    DOTS = DOTS + dots#the sum of dots
    N = N-1
print(DOTS)

# import math

# 1-masala

# def powerA3 (a):
#     k = 1
#     for i in range(3):
#         k *= a
#     return k
# print(powerA3(3))

# 2-masala

# def power234 (a):
#     x2 = a*a
#     x3 = 1
#     x4 = 1
#     for i in range(4):
#         if i < 3:
#             x3 *= a
#         x4 *= a
#     print(f"2 daraja : {x2} \n3 daraja: {x3} \n4 daraja: {x4}")
        
# power234(2)

# 3-masala

# def mean(a,b):
#     aorta = (a + b) / 2
#     geo = (a * b) / (a * b)
#     print( aorta,"\n", geo)
# mean(2,3)

# 4-masala

# def triangle(a):
#     p = 3 * a
#     s = (math.sqrt(3) / 4) * (a ** 2)
#     print(p,s)

# 5-masala

# def rectps(x1,y1,x2,y2):
#     a = x2 - x1 
#     b = y2 - y1 
#     p = 2 * (a + b)
#     s = a * b
#     print(f"P: {p} \nS: {s}")
# rectps(2,3,2,4)

# 6-masala

# def digitCS(a):
#     count = 0
#     summ = 0
#     while a > 0:
        
#         summ += a % 10
#         count += 1
#         a //= 10
#     print(f"count: {count} \nSumm: {summ}")
# digitCS(56)

# 7-masala

# def invertD(a):
#     s = ''
#     while a > 0:
#         k = str(a % 10)
#         s += k
#         a //= 10
#     return s
# print(invertD(123))

# 8-masala

# def addR(a,r):
#     a = str(abs(a))
#     r = str(abs(r))
#     l = a + r
#     l = int(l)
#     return l
# print(addR(235,2))

# 9-masala

# def addR(a,r):
#     a = str(abs(a))
#     r = str(abs(r))
#     l = r + a
#     l = int(l)
#     return l
# print(addR(235,2))

# 10-masala

# def swap2(a,b):
#     k = a
#     a = b
#     b = k
#     print(a,b)
# swap2(3,5)

# 11-masala

# def minmax(x,y):
#     big = x
#     small = y
#     if y > x:
#         big = y
#         small = x
#     x = small
#     y = big
#     print(x,y)
# minmax(6,2)

# 12-masala

# def sortInc(a,b,c):
#     big = max(a,(max(b,c)))
#     mid = 0
#     small = min(a,(min(b,c)))
#     if (a == big and small == b) or (a == small and b == big):
#         mid = c
#     print(small,mid,big)
# sortInc(2,6,4)    

# 13-masala

 # def sortInc(a,b,c):
#     big = max(a,(max(b,c)))
#     mid = 0
#     small = min(a,(min(b,c)))
#     if (a == big and small == b) or (a == small and b == big):
#         mid = c
#     print(big,mid,small)
# sortInc(2,6,4)  

# 14-masala

# def shiftR(a,b,c):
#     kC = c
#     kB = b
#     b = a
#     c = kB
#     a = kC
#     print(a,b,c)
# shiftR(1,2,3)

# 15-masala

# def shiftL(a,b,c):
#     kA = a
#     kC = c
#     c = b
#     b = kA
#     a = kC
#     print(a,b,c)
# shiftL(1,2,3)

# 16-masala

# def ishora(a):
#     if a > 0:
#         return -1
#     elif a == 0:
#         return 0
#     else:
#         return 1
    
# 17-masala

# def ildiz(a,b,c):
#     k = 0
#     d = b ** 2 - (4 * a * c)
#     if d > 0:
#         k = 2
#     elif d == 0:
#         k = 1
#     else:
#         k = 0
#     return k
# print(f"tenglamanining {ildiz(5,2,6) } ildizi bor")

# 18-masala

# def roundS(r):
#     s = 3.14 * (r ** 2)
#     return s
# print(roundS(5))

# 19-masala

# def ringS(r1,r2):
#     sHalqa = 3.14 * ((r2 ** 2) - (r1 ** 2))
#     return sHalqa
# print(ringS(5,6))

# 20-masala

# def triangleP(a,b):
#     c = math.sqrt((a ** 2) + (b **2))
#     p = a + b + c
#     return p
# print(triangleP(2,4))

# 21-masala

# def sumR(a,b):
#     k = 0
#     for i in range(a,b):
#         k += i
#     return k
# print(sumR(2,5))

# 22-masala

# def calc(a,b,op):
#     k = 0
#     if op == 1:
#         k = a - b
#     elif op == 2:
#         k = a * b
#     elif op == 3:
#         k = a / b
#     else:
#         k = a + b
#     return k
# print(calc(4,2,2))
    
# 23-masala

# def quorter(x,y):
#     k = 0
#     if x > 0 and y > 0:
#         k = 1
#     elif x < 0 and y > 0:
#         k = 2
#     elif x < 0 and y < 0:  
#         k = 3
#     else:
#         k = 4
#     return k 
# print(quorter(2,-4))

# 24-masala

# def even(a):
#     return (a % 2 == 0)
# print(even(5))

# 25-masala

# def issquare(a):
#     k = math.sqrt(a)

#     return k * k == a
# print(issquare(20))

# 26-masala

# def issquare5(a):
#     k = math.sqrt(a)

#     return k * k == a and k == 5
# print(issquare5(25))


# 27-masala

# def issquare5(a,n):
#     k = math.sqrt(a)

#     return k * k == a and k == n
# print(issquare5(25,5))

# 28-masala

# def isPrime(a):
#     count = 0
#     for i in range(1,a):
#         if a % i == 0:
#             count += 1
#         if count == 2:
#             break
#     return count == 2
# print(isPrime(9))
    
# 29-masala

# def digit(a):
#     count = 0

#     while a > 0:

#         count += 1
#         a //= 10
#     return count
# print(digit(565))

# 30-masala

# def digit(a,n):
#     arr = []
#     while a > 0:
#         k = a % 10
#         arr.append(k)
#         a //= 10
#     if n > len(arr):
#         return -1
#     else:
#         return arr[n]
# print(digit(4568,2))

# 31-masala

# def isPal(a):
#     arr = []
#     while a > 0:
#         k = a % 10
#         arr.append(k)
#         a //= 10
#     reverse = list(reversed(arr))
#     return arr == reverse
# print(isPal(121))

# 32-masala

# def deg(r):
#     rad = r * 3.14 / 180
#     return rad
# print(deg(30))

# 33-masala

# def deg(rad):
#     deg = int(rad * 180 / 3.14)
#     return deg
# print(deg(0.52))

# 34-masala

# def fact(a):
#     f = 1
#     for i in range(1,a + 1):
#         f *= i
#     return f
# print(fact(5))

# 35-masala

# def fact(a):
#     f = 1
#     for i in range(1,a + 1):
#         f *= i
#     return 2 * f
# print(fact(5))

# 36-masala
# def goldenR(k):
#     r = (1 + math.sqrt(5)) / 2
#     return r 
# def fib(a):
#     k = goldenR(a)
#     res = ((k ** a) - (1 - k) ** a) / math.sqrt(5)
#     return res
# print(fib(5))

# 37-masala

# def powerF(a,b):
#     res = 1
#     for i in range(b):
#         res *= a
#     return res
# print(powerF(5,2))

# 38-masala

# def power(a,n):
#     res = 1
#     for i in range(n):
        
#         res *= a
            
#         print(res)
# power(2,4)
        
# 39-masala

# def power3(a,n):
#     k = n % 10 // 10
#     if k > 0:
#         power(a,n)
#     else: 
#         powerF(a,n)

# 40-masala

# def exp(a,e):
#     k = 1
#     r1 = 0
#     result = 1
#     for i in range(e):
#         for j in range(i):
#             k *=  a
#         r1 = k + a ** i
#     result /= r1 
#     return result
# print(exp(2,4))

# 41-masala

# def exp(a,e):
#     k = 1
#     r1 = 0
#     result = 1
#     for i in range(e):
#         for j in range(1,i,2):
#             k *=  a
#         r1 = k - a ** i
#     result /= r1 
#     return result
# print(exp(2,4))

# 42-masala

# def exp(a,e):
#     k = 1
#     r1 = 0
#     result = 1
#     for i in range(e):
#         for j in range(2,i,2):
#             k *=  a
#         r1 = k - a ** i
#     result /= r1 
#     return result
# print(exp(2,4))
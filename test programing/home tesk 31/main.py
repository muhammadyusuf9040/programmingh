# import math
# 1-masala

# def powerA3(a,b,c,d,e):
#     arr = [a,b,c,d,e]
#     res = 1
#     for i in arr:
#         res = i  3
#         print(res)
# powerA3(1,5,6,4,8)

# 2-masala

# def powerA3(a,b,c):
#     arr = [a,b,c]
#     res = 1
#     count = 2
#     for i in arr:
#         for j in range(2,5):
#             res = i  count
#             print(f"{i} ning {j} darajasi: {res}")
#             count +=1
# powerA3(2,3,4)

# 3-masala

# def mean(a,b,c,d):
#     arr = [a,b,c,d]
#     aorta = 1
#     count = 2
#     for i in arr:
#         aorta = (i + (i+1)) / 2
#         print(aorta)
# mean(2,3,4,5)

# 4-masala

# def triangle(a,b,c):
#     arr  = [a,b,c]
#     p = 0
#     s = 0
#     for i in arr:
#         p = 3 * i
#         s = (math.sqrt(3) / 4) * (i ** 2)
#         print(f"{i} 3 burchak P: {p} va S: {s}")

# triangle(2,4,6)

# 5-masala

# def rectPs(x1, y1, x2, y2):
#     length = abs(x2 - x1)
#     width = abs(y2 - y1)
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter
# print(rectPs(x1=12,y1=3,x2=18,y2=8))
# # 6.
# def DigitCountSum(n):
#     digits = [int(d) for d in str(n)]
#     count = len(digits)
#     totalSum = sum(digits)
#     return count, totalSum
# print(DigitCountSum(n=32))    


# 8. 
# def addRightDigit(k, r):
#     return int(str(k) + str(r))
# print(addRightDigit(k=23,r=12))    


# 9. 
# def addLeftDigit(k, r):
#     return int(str(r) + str(k))
# print(addLeftDigit(k=23,r=32))    

# 10. 
# def swap(a, b):
#     return b, a
# print(swap(a,b))    
    

# 12. 
# def sortInc3(a, b, c):
#     return sorted([a, b, c])
# print(sortInc3(a,b,c))    

# 13. 
# def sortDec3(a, b, c):
#     return sorted([a, b, c], reverse=True)
# print(sortDec3(a,b,c))    

# 14. 
# def shiftRight3(a, b, c):
#     return c, a, b
# print(shiftRight3(a,b,c))    

# 15.
# def shiftLeft3(a, b, c):
#     return b, c, a
# print(shiftLeft3(a,b,c))    

# 16. 
# def sign(a):
#     return -1 if a < 0 else (1 if a > 0 else 0)
# print(sign(a))    

# 17. 
# def quadraticRoots(a, b, c):
#     discriminant = b**2 - 4*a*c
#     if discriminant < 0:
#         return None
#     x1 = (-b + math.sqrt(discriminant)) / (2*a)
#     x2 = (-b - math.sqrt(discriminant)) / (2*a)
#     return x1, x2
# print(quadraticRoots(a,b,c))    

# 18. 
# def circle(radius):
#     pi = 3.1415
#     return pi * radius**2
# print(circle(radius=40))    

# 19.
# def rings(r1, r2):
#     pi = 3.1415
#     return pi * (r1**2 - r2**2)
# print(rings(r1=302,r2=50))    

# 20. 
# def triangleP(a, b):
#     hypotenuse = (a**2 + b**2)**0.5
#     perimeter = a + b + hypotenuse
#     return perimeter
# print("TriangleP:", triangleP(a,b))
# row = int(input('Row:'))
# col = int(input('Col:'))

# midRow = row // 2
# midCol = row // 2

# for i in range(0,row):
#     for j in range(0,col):
#         print('*', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if j == 0:
#             print('#', end=' ')
#         print('*', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if j == 0 or i == 0:
#             print('#', end=' ')
#         else:
#             print('*', end=' ')
#     print()


# for i in range(0,row):
#     for j in range(0,col):
#         if j == 0 or i == 0 or j == col - 1:
#             print('#', end=' ')
#         else:
#             print('*', end=' ')
#     print()


# for i in range(0,row):
#     for j in range(0,col):
#         if j == 0 or i == 0 or j == col - 1 or i == row - 1:
#             print('#', end=' ')
#         else:
#             print('*', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if (j == 0 or i == 0 
#             or j == col - 1 or i == row - 1
#             or i == midRow
#             ):
#             print('#', end=' ')
#         else:
#             print('*', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if (j == 0 or i == 0 
#             or j == col - 1 or i == row - 1
#             or i == midRow
#             or j == midCol
#             ):
#             print('#', end=' ')
#         else:
#             print(0, end=' ')
#     print()


# for i in range(0,row):
#     for j in range(0,col):
#         if (
#             j == i
#             ):
#             print('#', end=' ')
#         else:
#             print(0, end=' ')
#     print()


# for i in range(0,row):
#     for j in range(0,col):
#         if (
#             j == i or i > j
#             ):
#             print('0', end=' ')
#         else:
#             print('*', end=' ')
#     print()


# for i in range(0,row):
#     for j in range(0,col):
#         if (
#             (i + j) % 2 == 0
#             ):
#             print('0', end=' ')
#         else:
#             print('1', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if (
#             i == j or i + j == col - 1
#             ):
#             print('0', end=' ')
#         else:
#             print('1', end=' ')
#     print()


# for i in range(0,row):
#     for j in range(0,col):
#         if (
#                 (
#                     (
#                     i == midRow - 1 or i == midRow + 1) 
#                     and (j == midCol - 1 or j == midCol + 1) 
#                 )
#             ):
#             print('0', end=' ')
#         else:
#             print('1', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         print(chr(i + 65), end=' ')
#     print()

# k = 1
# for i in range(0,row):
#     for j in range(0,col):
#         print(k, end=' ')
#         k += 1
#     print()

# k = 1
# sum = 0
# for i in range(0,row):
#     for j in range(0,col):
#         print(k, end=' ')
#         if j == 0 or j == col-1 or i == midRow:
#             sum += k
#         k += 1
#     print()
# print(sum)

# k = 1
# sum = 0
# for i in range(0,row):
#     for j in range(0,col):
#         print(k, end=' ')
#         if j == 0 or j == col-1 or i == midRow or j == midCol:
#             sum += k
#         k += 1
#     print()
# print(sum)

# k = 1
# sum = 0
# for i in range(0,row):
#     for j in range(0,col):
#         print(k, end=' ')
#         if i >=j:
#             sum += k
#         k += 1
#     print()
# print(sum)

# k = 1
# sum = 0
# for i in range(0,row):
#     for j in range(0,col):
#         print(k, end=' ')
#         if i == j or i + j == col -1:
#             sum += k
#         k += 1
#     print()
# print(sum)

# for i in range(0,row):
#     for j in range(0,col):
#         if i >=j:
#             print('*',end=' ')
#         else:
#             print(' ', end=' ')
#     print()





# for i in range(0,row):
#     for j in range(0,col):
#         if i >=j:
#             print( j +1,end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if i >=j:
#             print( i +1,end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# for i in range(0,row):
#     for j in range(0,col):
#         if (
#                 (i ==j and i <= midRow)
#                 or (i + j == col -1 and i <= midRow)
#                 or j == 0 or j == col -1
#             ):
#             print('*',end=' ')
#         else:
#             print(' ', end=' ')
#     print()



# ------------------------------------------------


# soat

# import time
# for soat in range (0,24 ):
#     for minut in range (0,60):
#         for sekund in range(0,60):
#             print(f"soat: {soat}, minut:{minut},sekund:{sekund}",end="\r")
#             time.sleep(1)
# i = 1 
# while i < 4:
#     j = 10
#     while j > 7:
#         if i == j % 3:
#             print("Loop", end=" ")
#         j -= 1 
#     i += 1

# p = 2
# while p > 0:
#     q = p
#     while q < 4:
#         print(q, end="")
#         q += 1
#         p -= 1

# x = 0
# while x < 4:
#     x += 1
#     if x == 2:
#         continue


# i = 1
# count = 0
# while i <= 3:
#     j = 1
#     while j <= i:
#         count += 1
#         j += 1
#     i += 1
# print(count)

# 
# a = 15
# b = 25
# 
# if a > 10:
#     if b < 20:
#         print("X", end="")
#     else:
#         print("Y", end="")
#     if a + b == 40:
#         print("Z", end="")
# else:
#     print("W")


# i=0
# while i<=10:
#     for j in range(1,5):
#         print(f"{i},{j}")
#         i+=1

for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()







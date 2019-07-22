# Print a sequence of numbers starting with N, without using loop, in which  A[i+1] = A[i] - 5,
# if  A[i]>0, else A[i+1]=A[i] + 5  repeat it until A[i]=N.

# Example:
# Input:
# 16
# 10
# Output:
# 16 11 6 1 -4 1 6 11 16
# 10 5 0 5 10

# Explanation:
# We basically first reduce 5 one by one until we reach a negative or 0.
# After we reach 0 or negative, we one by one add 5 until we reach N.
# import sys
# c = 0

# n = 0


# def printer():
#     global c, n, x

#     print(n, end=" ")
#     if c > 0 and n == x:

#         return print(n)
#     elif n > 0:
#         n = n-5
#         return printer()
#     else:
#         n = n+5
#         return printer()

#     c += 1


n = 16  # int(input("Enter Number : "))
x = 16
c = 0
flag = 0
while True:
    if c > 0 and n == x:
        print(n)
        break
    print(n, end=" ")

    if n <= 0 or flag > 0:
        flag = 1
        n = n+5
    else:
        n = n-5
    c += 1

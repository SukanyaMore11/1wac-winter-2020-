# factorial of n no.s:
# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i
# print(fact)
# # nested loop
# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print('*', end=" ")
#     print()

# for i in range(n):
#     print('*',*n)

# """
# n=4
# * 
# * *
# * * * 
# * * * *
# """
# n = int(input())
# for i in range(n +1):
#     for j in range(i):
#         print('*', end=" ")
#     print()

# for i in range(n):
#     print('*',*(i+1))

# # PRIME NUMBER
# n= int(input())

# is-prime = True
#  for i in range(2, n):
#     if n % i == 0:
#     is-prime = False

# if is-prime:
#     print("It is prime number")
# else"
#     print("Not prime number")

# number pattern
# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(i,end=" ")
#     print()
# for i in range(1,n+1):
    # for j in range(1,i+1):
    #     print(j,end=" ")
    # print()
# b = 0
# for i in range(n,0,-1):
#     b += 1
#     for j in range(1,i+1):
#         print(b,end=" ")
#     print()
# n = int(input())
# b = n+1
# for i in range(n,0,-1):
#     b -= 1
#     for j in range(1,i+1):
#         print(b,end=" ")
#     print()
n = int(input())
for i in range(n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

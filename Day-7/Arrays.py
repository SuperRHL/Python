# recursion- when a function calls itself
n = int(input())
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(n))

# principle of mathematical induction
# if you want to prove a statement f is true for all natural numbers.
# first prove it is true for a small number
# assume f(k) is true
# second prove f(k+1) is true

# def sum_n(n):
#     if n==0:
#         return 0
#     smallOutput=sum_n(n-1)
#     print(smallOutput,n)
#     return n+smallOutput
# print(sum_n(n))


# def one_to_n(n):
#     if n==0:
#         return
#     one_to_n(n-1)
#     print(n)
#     return
# print(one_to_n(n))

# def n_to_one(n):
#     if n==0:
#         return
#     print(n)
#     n_to_one(n-1)
# print(n_to_one(n))


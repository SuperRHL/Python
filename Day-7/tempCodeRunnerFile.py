
def one_to_n(n):
    if n==0:
        return
    one_to_n(n-1)
    print(n)
    return
print(one_to_n(n))

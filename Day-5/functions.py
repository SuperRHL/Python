# def say_hello(name, age):
#     print(f"Hello {name}, you are {age} years old!")

# say_hello('Rahul',20)

# def sum(num1,num2):
#     return print(num1+num2)
# sum(4,5)

# def super_func(*args,**kwargs):
#     total = 0
#     print(kwargs)
#     for items in kwargs.values():
#         total += items
#     return sum(args)+total

# print(super_func(1,2,3,4,5, num1=5,num2=10))

def highest_even(li):
    li.sort()
    li.reverse()
    for n in li:
        if n % 2 == 0:
            return n
        else:
            pass

# print(highest_even([10,2,3,14,5,6,7,]))

# def highest_even2(li):
#     even_list = []
#     for i in li:
#         if i % 2 == 0:
#             even_list.append(i) 
#     return max(even_list)

# print(highest_even2([10,2,3,14,5,6,7]))

#walrus operator 
# a='yoooooooooooooooooooo'
# if (((n:=len(a)))>10):
#     print(n)

# total = 0 
# def count(total):
#     total += 1
#     return total
# print(count(count(count((total)))))


# ordered sequence of objects of any type

li = [1,2,3,4,5]
li2 = ['a','b','c','d','a']

# amazon_cart = ['notebook','sunglasses','toys', 'books']
# amazon_cart[0] = 'mouse'
# print(amazon_cart)
# new_list = amazon_cart[:]
# new_list[0] = 'gum'

# new_list.append('pen')
# print(new_list)

# new_list.extend(['cheese'])
# print(new_list)

# new_list.pop(0)
# print(new_list)

# new_list.remove('toys')
# print(new_list)

# li2.sort()
li2.sort()
li2.reverse()

# print(list(range(101)))


new_sentence = ' '.join(['Hi','my','name', 'is', 'Rahul'])
# print(new_sentence)

#list unpacking

a,b,c, *others,d = [1,2,3,4,5,6,7,8,9]
# print(others)

# Dictionary
# key cannot change, immutable and has to be unique else overwritten
user = {
    123: [1,[2,4,5],3],
    True: 'Hello',
    'c': True,
    'd': 4,
    'e': 5,
    }

user2 = dict(name = 'John')

# print(user.get('age', 55),user2['name'])

# print(user.popitem())

# print(user)

# tuples = immutable lists
# tuples are faster

my_tuple = (1,2,3,4,5,6)
# print(5 in my_tuple)

x,y,z, * others = my_tuple
# print(my_tuple.index(5))

#  set = unordered collection of unique objects
my_set = {1,2,3,4,5}
my_set.add(2)
# print(my_set)

new_set = {4,5,6,7,8,9,10,10}
# print(new_set)

# print(my_set.difference(new_set))
# print(my_set.discard(5))
# print(my_set)
# print(my_set.difference_update(new_set))
# print(new_set)
# print(my_set.intersection(new_set))
# print(my_set.isdisjoint(new_set))
# print(my_set | new_set) or print(my_set.union(new_set))
# print(my_set.issubset(new_set))
# print(my_set.issuperset(new_set))

some_list = ['a', 'b', 'c','b','d','m','n','n']
duplicates=[]
for i in some_list:
    if some_list.count(i)>1:
        # duplicates.append(i)
        # some_list.remove(i)
        if i not in duplicates:
            duplicates.append(i)
print(duplicates)
print(some_list)
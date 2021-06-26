import random
names = input("Type in the names: ").split(",")
bearer_num = random.randint(0, len(names)-1)
bearer = names[bearer_num]
print(f"{bearer} is going to buy the meal today!")
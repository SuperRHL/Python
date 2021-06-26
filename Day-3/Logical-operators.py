print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
combined = (name1+name2).lower()

t=combined.count("t")
r=combined.count("r")
u=combined.count("u")
e=combined.count("e")
l=combined.count("l")
o=combined.count("o")
v=combined.count("v")

true_count = str(t+r+u+e)
love_count = str(l+o+v+e)
score = int(true_count+love_count)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos!")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
#Tip Calculator
print("Welcome to the tip calculator")

total = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? "))

tip = total * tip_percentage/100
print(f"Each person needs to pay {round(total/people+tip/people,2)}") 
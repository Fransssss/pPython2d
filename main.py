# 2d list = list of lists

fruit = ["Apple", "Orange", "Pineapple"]
vegetable = ["Spinach", "Broccoli", "Cabbage"]
meat = ["Pork", "Chicken", "Beef"]
food = [fruit,vegetable,meat]

print("\n== Food Lists ==")
print("1. List of fruit")
print("2. List of vegetable")
print("3. List of meat")
print("4. List of food")
print("5. Locate specific item in a specific list")
print("E. Exit")
choice = input("choice: ")

while choice != "e" and choice != "E":
    if choice == "1":
        print("\nList of fruit")
        print(fruit)
        print('\n')
    elif choice == "2":
        print("\nList of vegetable")
        print(vegetable)
        print('\n')
    elif choice == "3":
        print("\nList of meat")
        print(meat)
        print('\n')
    elif choice == "4":
        print("\nList of food")
        print(food)
        print('\n')
    elif choice == "5":
        print("\nLocate specific item in a specific list")
        numList = int(input("Input number of list: "))
        numItem = int(input("Input index of item: "))
        print(food[numList][numItem])
        print('\n')
    else:
        print("\n[Invalid input]\n")

    print("Food Lists")
    print("1. List of fruit")
    print("2. List of vegetable")
    print("3. List of meat")
    print("4. List of food")
    print("E. Exit")
    choice = input("choice: ")

if choice == "e" or choice == "E":
    print("\n== Exit Program ==")
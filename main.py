food_list = []
while True:
    print("Type 0. Exit")
    print("Type 1. Add Food")
    print("Type 2. Remove")
    print("Type 3. View all Food")

    user_choice = input("Type your option: ")
    if user_choice == "0":
        print("Thanks for Using")
    elif user_choice == "1":
        food = input("Type your food name: ")
        food_list.append(food)
        print("FooD Added Successfully")

    elif user_choice == "2":
        food = input("Type your food name: ")
        food_list.remove(food)
        print("FooD Remove Successfully")

    elif user_choice == "3":
        if food_list:
            print("your FooD List:")
            for index, food in enumerate(food_list, start=1):
                print(f"{index}.{food}")
        else:
            print("List empty")

    else:
        print("Invalid Choice")

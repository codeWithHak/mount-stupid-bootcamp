print("\nKeep giving numbers to add them in a list")
print("Press enter without any vlaue to stop the input")


# take input from user
number_list = []
total_items = 0
duplicate_items = 0
unique_items = 0

while True:
    try:
        user_input = input("Give a number: ")
        if user_input != "":
            user_input = int(user_input)

            total_items += 1
            
            # add input in a list
            if user_input in number_list:
                duplicate_items += 1
            else:
                unique_items += 1
                number_list.append(user_input)

        else:
            break
    except ValueError:
        print("Invalid value")


print("List: ", number_list)
print('Total Items Entered:', total_items)
print('Unique Items:', unique_items)
print('Duplicate Items:', duplicate_items)
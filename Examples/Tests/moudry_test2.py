def largest_num_in_list(list_param):
    num = 0
    for i in list_param:
        field_check = isinstance(i, int)
        if field_check is True:
            if i > num:
                num = i
    return num

def filter_odd_numbers(list_to_filter):
    filtered_list = list()
    for item in list_to_filter:
        field_check = isinstance(item, int)
        if field_check is True:
            if item%2 != 0:
                filtered_list.append(item)
    return filtered_list

def combine_lists(list1_to_combine, list2_to_combine):
    combined_list = list()
    for item1 in list1_to_combine:
        combined_list.append(item1)
    for item2 in list2_to_combine:
        combined_list.append(item2)
    return combined_list

IS_RETURN = True
while IS_RETURN:
    print("1. Largest number in list")
    print("2. Filtering odd numbers from list")
    print("3. Print list items with indexes")
    print("4. Inserting list into another list")

    PROGRAM_NUMBER = input("Enter program number: ")
    PROGRAM_NUMBER_CHECK = PROGRAM_NUMBER.isdigit()

    if PROGRAM_NUMBER_CHECK is True:
        PROGRAM_NUMBER = int(PROGRAM_NUMBER)

    if PROGRAM_NUMBER == 1:
        print("\n", "----1. Largest number in list----")
        TARGETED_LIST = [1, 2, -8, "f", 0]
        print("Inserted list: ", TARGETED_LIST)
        print("Largest number in list: ", largest_num_in_list(TARGETED_LIST))
    elif PROGRAM_NUMBER == 2:
        print("\n", "----2. Filtering odd numbers from list----")
        UNFILTERED_LIST = [7, 8, 120, "f", 25, 44, 20, 27]
        print("Inserted list: ", UNFILTERED_LIST)
        print("Filtered list: ", filter_odd_numbers(UNFILTERED_LIST))
    elif PROGRAM_NUMBER == 3:
        print("\n", "----3. Print list items with indexes----")
        TARGETED_LIST = [3, 13, 25, 8, 48]
        print("Inserted list: ", TARGETED_LIST)
        for index, value in enumerate(TARGETED_LIST):
            print("[", index, "]", "=>", value)
    elif PROGRAM_NUMBER == 4:
        print("\n", "----4. Inserting list into another list----")
        LIST1 = [1, 2, 3, 0]
        LIST2 = ['Red', 'Green', 'Black']
        print("List n. 1: ", LIST1)
        print("List n. 2: ", LIST2)
        print("Combined list: ", combine_lists(LIST1, LIST2))
    else:
        print("Error")

    print("")
    USER_DECISION = input("Do you want to continue? [Y/N]: ")
    if USER_DECISION == "N":
        IS_RETURN = False
    else:
        print("")
        print("------------")
        print("")

print("\n")
input("Press any key to exit...")
def linear_search(data_list, target):
    for i in range(len(data_list)):
        if data_list[i] == target:
            return f"Index number: {i}"

    return -1


numbers = [10, 25, 30, 45, 55]
print(linear_search(numbers, 30))
print(linear_search(numbers, 90))

names = ["Alice", "Bob", "Charlie"]

print(linear_search(names, "Bob"))
print(linear_search(names, "Dave"))

mixed = [1, "apple", 3.14, True]
print(linear_search(mixed, "apple"))
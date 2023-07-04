def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] < target:
            left = mid + 1
        elif lst[mid] > target:
            right = mid - 1
        else:
            return mid

    return left

def sort_list(lst):
    return sorted(lst)

# Input the sequence of numbers
numbers = input("Enter a sequence of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Check input validity
if len(numbers) < 2:
    print("The sequence should contain at least two numbers.")
    exit()

# Input a number from the user
target_num = int(input("Enter a number: "))

# Sort the list
sorted_numbers = sort_list(numbers)

# Find the position of the element in the sorted list
position = binary_search(sorted_numbers, target_num)

# Check the conditions
if position == len(sorted_numbers):
    print("All elements in the list are smaller than the entered number.")
elif sorted_numbers[position] == target_num:
    print("The entered number is already present in the list.")
else:
    print("The position of the element that is smaller than the entered number and the next element is greater or equal to it:", position)

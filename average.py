def calculate_average(numbers):
    try:
        if not numbers:
            return "Error: Empty list"
        return sum(numbers)/len(numbers)
    except TypeError:
        return "Error: Invalid input"
    

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([]))
print(calculate_average("Invalid"))
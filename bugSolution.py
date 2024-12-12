def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle list with no numeric values
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with error handling
data = [1, 2, 3, 4, 5]
average = calculate_average(data)
print(f"The average is: {average}")

data = []
average = calculate_average(data)
print(f"The average is: {average}")

data = [1, 2, "a", 4, 5]
average = calculate_average(data)
print(f"The average is: {average}")

data = ["a","b","c"]
average = calculate_average(data)
print(f"The average is: {average}") 
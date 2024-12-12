def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with potential error
data = [1, 2, 3, 4, 5]
average = calculate_average(data)
print(f"The average is: {average}")

data = []
average = calculate_average(data)
print(f"The average is: {average}")

data = [1, 2, "a", 4, 5]
average = calculate_average(data)
print(f"The average is: {average}")
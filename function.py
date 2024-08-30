def find_larger(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return num1  # Correctly return num1 or num2 when they are equal

# Example usage:
print(find_larger(10, 10))  # This will correctly return 10

def sum_of_square_numbers(n):
    return (n * (n + 1) * (2*n + 1)) // 6

n = 6 

result = sum_of_square_numbers(n)
print(f"The sum of the squares of the first {n} natural numbers is: {result}")

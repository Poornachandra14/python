def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 9
print_factors(num)

def print_n_factors(number, n):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
 
    print("Factors of", number, ":")
    for i in range(n):
        if i < len(factors):
            print(factors[i])
        else:
            break

number = int(input("Enter a number:"))
n = int(input("Enter the value of n:"))

print_n_factors(number, n)

def print_n_factor(number, n):
    factors = []
    
    
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
     
    print("Number of factors of", number, ":", len(factors))
     
    if n <= len(factors):
        
        print("The", n, "factor of", number, ":", factors[n-1])
    else:
        print("The", n, "factor does not exist for", number)
    
 
number = int(input("Enter a number: "))
n = int(input("Enter the value of n: "))

 
print_n_factor(number, n)

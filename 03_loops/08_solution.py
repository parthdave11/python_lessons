number = 28
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            print("Number is not prime number")
            break
    if is_prime == True:
        print("Number is a prime number")
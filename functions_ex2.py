def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
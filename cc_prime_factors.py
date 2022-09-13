"""
This module returns prime factors of a number as a list given a number
"""

# check if a number is a prime number
def is_prime_number(number):
    try:
        integer_number = int(number)
        if integer_number < 2:
            return False
        elif integer_number == 2:
            return True
        else:
            prime = True
            for n in range(2, integer_number):
                if integer_number % n == 0:
                    return False
            return prime
    except Exception as e:
        return None

def prime_factors(number):
    try:
        integer_number = int(number)
        if integer_number == 0:
            return None
        elif integer_number == 1:
            return integer_number
        elif is_prime_number(integer_number):
            return number
        else:
            factors = list()
            factor = 2

            factorized = False
            divident = integer_number
            while not factorized:
                if is_prime_number(factor):
                    if divident % factor == 0:
                        factors.append(factor)
                        divident = divident // factor
                    else:
                        factor += 1
                    
                    if divident == 1:
                        return factors
                else:
                    factor += 1
    except Exception as e:
        return None


if __name__ == "__main__":
    # testing is_prime_number()
    # numbers = [1,2,3,4,5,6,7,8,9,11,13,56,72,'a','79',0,'',999999977777777]
    # for number in numbers:
    #     prime = is_prime_number(number)
    #     print(f'Number {number}: is prime : {prime}')


    # testing prime_factors()
    test_numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'a','',100000]
    for n in test_numbers:
        factors = prime_factors(n)
        print(f'{n} : {factors}')
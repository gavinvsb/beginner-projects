"""Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors)
- You can (and should!) use your answer to Exercise 4 to help you"""

def get_integer():
    "Return an integer inputted from a user"
    user_input = int(input("Enter a number: "))
    return user_input

def check_prime(number):
    """Returns boolean indicating whether inputted value is prime."""
    result = False # initiate boolean for true false, default false

    if number > 0:
        for x in range (2, number - 1): # this range excludes number and 1, both of which number is divisible by
            if number % x != 0: # If number isn't evenly divisible by x, start over with the next one
                continue 
            elif number % x == 0: # If number is evenly divisible by x, it can't be prime
                result = False
                return result
        result = True
    elif number == 0:
        result = False
    elif number < 0: #if number is less than 0, the number is not prime (according to the Google).
        result = False
    return result

check_prime(get_integer())

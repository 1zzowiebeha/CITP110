"""Exercise #17 from our textbook."""

def is_prime(input_num: int) -> bool:
    """Test if the input number is prime.
    
    Rules to test if a number is prime:
        1. Number must be divisible by itself.
        2. Number must be divisible by one.
        3. Number must return a remainder when divided by
            another number.
    """
    
    # Check this here so that
    # .. we don't perform is_self_divisible
    # .. and throw a ZeroDivisionError.
    if input_num == 0:
        return False
    
    is_divisible_by_another = False
    
    # This test is purely to check divisibility by numbers
    # .. between 2 and (input_num - 1). (second range arg is exclusive)
    # If we include input_num, (input_num % num == 0) will always be True and
    # .. so False will return.
    # If we include 1, (input_num % 1 == 0) will always be True and
    # .. so False will return.
    # This is why self-divisibility & one-divisibility is checked
    # .. further down.
    for num in range(input_num - 1, 1, -1):
        if input_num % num == 0:
            return False
    
    return True
    # is_self_divisible = input_num % input_num == 0
    # # The user could enter zero (a non-prime), thus this check
    # # .. is important.
    # is_divisible_by_one = input_num % 1 == input_num
    
    # if is_divisible_by_one and is_self_divisible:
    #     return True
    # else:
    #     return False




for i in range(100):
    print(i, is_prime(i))
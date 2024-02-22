def prime_number_analysis(number_under_test):
    """
    Performs a test, if the single argument is a prime number.
    """
    prime_number = True

    for number in range(2, number_under_test):
        if number_under_test % number == 0:
            prime_number = False
            break

    if prime_number is True:
        print(f"{number_under_test} is a prime number.")
    else:
        print(
            f"{number_under_test} is a composite number. The smallest divider is: {number}."
        )


prime_number_analysis(99991)
prime_number_analysis(999983)
prime_number_analysis(9999991)
prime_number_analysis(99999989)
prime_number_analysis(999999937)
# prime_number_analysis(2147483647)
# prime_number_analysis(162259276829213363391578010288127)

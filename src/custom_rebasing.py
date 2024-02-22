# Custom Rebasing
#################

# formula
# number = (number // base) * base  + number % base

def from_base10(number, base):
 
    if base < 2:
        raise ValueError("Base must be >= 2")

    if base < 0:
        raise ValueError("Number must be >= 0")

    if number == 0:
        return [0]

    digits = []
    while number > 0:
        modulo = number % base 
        number = number // base
        digits.insert(0, modulo)
    
    return digits

def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")
    
    encoding = ''.join([digit_map[d] for d in digits])

    return encoding

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end
    sign = -1 if number < 0 else 1
    number *= sign
    
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


print(rebase_from10(number=10, base=16))

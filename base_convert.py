# int, int -> int
# Converts a given int from base 10 to base b, with b being an int from 2 to 16
def convert(num, b):
    """Recursive function that returns a string representing num (int) in the base b (int)"""

    if num == 0:        # Base case
        return ''
        
    remainder = num % b
    reduced_quotient = convert(num // b, b)
    return str(reduced_quotient) + f"{remainder:x}".upper()
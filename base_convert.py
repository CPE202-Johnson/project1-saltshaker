# int, int -> int
# Converts a given int from base 10 to base b, with b being an int from 2 to 16
def convert(num, b):
    """Recursive function that returns a string representing num (int) in the base b (int)"""

    if num == 0:        # Base case
        return '0'
        
    remainder = num % b         # Modulous to get remainder
    reduced_quotient = convert(num // b, b)     # Long division to get whole number
    combine = str(reduced_quotient) + f"{remainder:x}".upper()      # Converts int to str and converts remainder values above 9 to hex
    if combine[0] == '0':       # Gets rid of leading zero 
        combine = combine.replace('0', '', 1)
    return combine
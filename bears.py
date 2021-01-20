# int -> bool
# Takes a number input and checks if it can be manipulated to exactly 42 by the three rules
def bears(n):
    """Takes an input int and checks if it can win the bear game"""
    if n == 42:         # Base case of number found
        return True
    if n < 42:          # Base case of number too low to get to 42
        return False    
        
    isStuck = True      # Set to false if any of the rules are possible
    possible = False    # Set to true if any of the potential routes result in 42
    
    if n % 2 == 0:      # Divisible by 2
        isStuck = False
        possible |= bears(n//2)     # Use // to avoid number converting to float
    if (n % 3 == 0) | (n % 4 == 0):     # Divisible by 3 or 4
        bears_str = str(n)
        giveBears = int(bears_str[-1]) * int(bears_str[-2])
        if giveBears != 0:      # Avoid program getting stuck infinite loop of subtracting 0
            isStuck = False
            possible |= bears(n - giveBears)    
    if n % 5 == 0:      # Divisible by 5
        isStuck = False
        possible |= bears(n-42)
        
    if isStuck:         # Number isn't divisible by 2, 3, 4, or 5
        return False
        
    return possible
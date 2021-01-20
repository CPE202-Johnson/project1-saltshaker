# string -> list of strings
# Take a string input and returns a list containing the input string
# and all possible permutations. The input string is assumed to be made of unique, lowercase letters
def perm_gen_lex(a): 
    """Takes a string input and returns a list of all possible permutations"""
    if a == '':         # Deals with no input
        return []
    if len(a) == 1:     # Base case
        return [a]
        
    perm = []       # List that contains permutations          
        
    for i in a:     # Repeat for each letter in a
        reduced_perm = perm_gen_lex(a.replace(i, ''))       # Reduction by replacing a letter with nothing
        for j in range(0,len(reduced_perm)):                
            reduced_perm[j] = i + reduced_perm[j]           # Add the removed letter back to each sub-permutation
        perm.extend(reduced_perm)                           # Extend to add items in list to complete list
    return perm
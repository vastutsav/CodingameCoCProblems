print(str(sum(map(lambda x: (ord(x)-64)*2 if x.isupper() else ord(x)-96 , input().replace(" ","")))).ljust(6, '0')[:6])

#SHORTEST MODE
# Implement the following hashing algorithm:
#
# Given any sequence of characters, sum the positions in the alphabet for all letters, where you multiply this position by 2 if the letter is uppercase.
#
# Constrain the amount of digits in the hash to 6 by removing the last digits, or by adding zeros to the end.
#
# Example:

# Input:

# Clash Of Code

# Positions in the alphabet:

# C: 3, l: 12, a: 1, s : 19, h: 8, O: 15, f: 6, C: 3, o: 15, d: 4, e: 5

# C, O and C will be multiplied by 2, since they are uppercase.

# The sum is: 3*2 + 12 + 1 + 19 + 8 + 15*2 + 6 + 3*2 + 15 + 4 + 5 = 112

# 112 has less than 6 digits, so the final hash is:

# 112000
# Input
# Line 1: A string sequence.
# Output
# Line 1: The result of the hashing algorithm applied on sequence.
# Constraints
# 1 <= sequence.length <= 10000
# Example
# Input
# Clash Of Code
# Output
# 112000

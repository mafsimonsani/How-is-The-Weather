# WC '17 Contest 1 J2 - How's the Weather?

celsius = int(input())

# Given a value of C , which is an integer between -40 and 40 (inclusive), 
# determine the corresponding value of F.
# C = 5/9 * (F-32)

# F = (9/5 * C) + 32

fahrenheit = (9/5 * celsius) + 32

print(fahrenheit)
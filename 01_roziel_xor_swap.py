input("XOR swap does not require 3 variables to swap values. press enter. ")
print("Before: a is 5 and b is 9")
a, b = 5, 9
a ^=b; b^=a; a^=b
print("After: a is now: ", a, "and b is now: ", b)

n = int(input("Enter a number (3 or 7): "))
guess = input("What will " + str(n) + " become after XOR swap? ")
a, b = n, 8
a^=b; b^=a; a^=b
input("XOR swap will reverse the numbers. press enter")
print("n became: ", a, "Your guess was", guess)
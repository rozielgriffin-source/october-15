input("XOR sign detection - n ^ m < 0 means different signs. Press enter. ")
print("4 ^ 2: ", 4 ^ 2, "Same signs will return positive. ")
print("4 ^ -2: ", 4 ^ -2, " Different signs will return negative.")

n = int(input("Enter a number like 5 or -7: "))
guess = input("Will " + str(n) + " ^ -8 be positive or negative? ")
input("XOR is negative when signs are opposite. Press enter. ")
print("n is: ", n, "n ^ -8 is: ", n^-8, " your guess was, ", guess)
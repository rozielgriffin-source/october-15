input("Left shift will double the number, while right shift halves it. Press enter. ")
print("3 << 1: ", 3 << 1, "12 >> 1: ", 12 >> 1)
print("3 << 2: ", 3 << 2, "12 << 2: ", 12 << 2)

n = int(input("Enter a number (5 or 8): "))
guess = input("What is " + str(n) + " << 2")
input("Left shift by 2 will multiply by 4. Press enter. ")
print("N was: ", n, "Now n << 2 is: ", n << 2, "  your guess was, ", guess)
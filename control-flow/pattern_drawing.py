# Let request the user to enter the size of the pattern he wants
size = int(input("Enter the size of the pattern: "))
# Using Row Counters
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  
    row += 1
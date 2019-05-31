# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num): 
    if num % 2 == 0: 
        print("Even!")
        return True
    else:
        print("Odd")
        return False

print(is_even(5))
print(is_even(6))

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

is_even(num)

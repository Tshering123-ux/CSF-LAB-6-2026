# This is for a Linear Search Program #

# First, lets create a list #
numbers = [10, 20, 30, 40, 50, 60]

# Then, we Display the list #
print("The List is:", numbers)

# Take user input
target = int(input("Enter element to search: "))

# Then we use Linear search #
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print("The Element found at position is:", i + 1)
        found = True
        break

# If element is not found
if not found:
    print("Element not found")
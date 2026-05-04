# Since this is a Indexed (Block) Search Program, we need to import math to calculate block size and block search #

import math

# Create a given sorted list #
numbers = [5, 10, 15, 20, 25, 30, 35, 40]
print("The List is:", numbers)

# Now we gather input from user #
target = int(input("Enter any element: "))

# Firstly we determine the block size #
n = len(numbers)
block_size = int(math.sqrt(n))

# Secondly, we find the block where an element may exist #
start = 0
end = block_size

while start < n and numbers[min(end, n) - 1] < target:
    start = end
    end += block_size

# Next, we simply perform linear search within the block #
found = False
for i in range(start, min(end, n)):
    if numbers[i] == target:
        print("Element found")
        found = True
        break

if not found:
    print("Element not found")
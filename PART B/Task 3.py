# This is for selection Sort Program #

# Lets create a given list #
numbers = [64, 25, 12, 22, 11]

# Then, display original list
print("The Original List is:", numbers)

# Now we perform selection sort #
n = len(numbers)

for i in range(n):
    min_index = i
    
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    
    # Swap the found minimum element with the first element #
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Finally, we display sorted list #
print("Sorted List:", numbers)
# This is for selection Sort with Trace (Pass-wise Output) #

numbers = [64, 25, 12, 22, 11]

n = len(numbers)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Next perform Swap just like we did in task 3 
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    # And finally display after each pass 
    print(f"Pass {i + 1}:", numbers)
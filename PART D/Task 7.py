# This program is for implementing Stack Implementation and Selection Sort #

# Create a Stack class #
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "The Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items

# Next, we perform and define Selection Sort function #
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Now using real values we implement the main Program #
stack = Stack()

# Push elements
stack.push(22)
stack.push(78)
stack.push(89)
stack.push(105)
stack.push(15)

print("The Stack elements are:", stack.display())

# Then, Convert stack to list #
data = stack.display().copy()

# And finally Sort the list #
sorted_data = selection_sort(data)

print("The final Sorted List is:", sorted_data)
# This is for Queue Implementation + Linear Search #

# Create Queue class #
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


# Create Linear Search function #
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1   # position (1-based)
    return -1


# Next we start the Main Program and enter input #
queue = Queue()

# Insert elements
queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
queue.enqueue(20)
queue.enqueue(25)

print("The Queue elements are:", queue.display())

# Input element to search #
element = int(input("Enter element to search: "))

# Perform Search #
position = linear_search(queue.display(), element)

if position != -1:
    print("Element found at position", position)
else:
    print("Element not found")
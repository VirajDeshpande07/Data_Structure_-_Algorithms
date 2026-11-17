
# Enqueue operation
def enqueue(queue, element):
    queue.append(element)
    print(element, "inserted into queue")


# Dequeue operation
def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Deleted element:", queue.pop(0))


# Display operation
def display(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)


# Reverse queue using stack
def reverse_queue(queue):
    stack = []

    while len(queue) > 0:
        stack.append(queue.pop(0))

    while len(stack) > 0:
        queue.append(stack.pop())

    return queue


# Merge two queues
def merge_queues(queue1, queue2):
    merged = queue1 + queue2
    return merged


# Check whether two queues are identical
def identical_queues(queue1, queue2):
    if queue1 == queue2:
        print("Both queues are identical")
    else:
        print("Queues are not identical")


# Main program

queue1 = []
queue2 = []

# 1. Enqueue
enqueue(queue1, 10)
enqueue(queue1, 20)
enqueue(queue1, 30)

enqueue(queue2, 10)
enqueue(queue2, 20)
enqueue(queue2, 30)

# 2. Display
print("\nQueue 1:")
display(queue1)

# 3. Dequeue
dequeue(queue1)

print("\nAfter Dequeue:")
display(queue1)

# 4. Reverse queue using stack
reverse_queue(queue1)

print("\nReversed Queue:")
display(queue1)

# 5. Merge two queues
merged = merge_queues(queue1, queue2)

print("\nMerged Queue:")
display(merged)

# 6. Check identical queues
print("\nChecking identical queues:")
identical_queues(queue1, queue2)

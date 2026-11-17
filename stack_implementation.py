
def push(stack, element):
    stack.append(element)
    print(element, "pushed into stack")


def pop(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element:", stack.pop())


def display(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements (top to bottom):")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])


# Reverse a string using stack
def reverse_string(string):
    stack = []

    for ch in string:
        stack.append(ch)

    result = ""

    while len(stack) > 0:
        result += stack.pop()

    return result


# Reverse stack using another stack
def reverse_stack(stack):
    temp = []

    while len(stack) > 0:
        temp.append(stack.pop())

    while len(temp) > 0:
        stack.append(temp.pop())

    return stack


# Main program
stack = []

push(stack, 10)
push(stack, 20)
push(stack, 30)

display(stack)

pop(stack)

display(stack)

string = "PYTHON"
print("Original string:", string)
print("Reversed string:", reverse_string(string))

print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)

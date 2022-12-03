# add value at the top of the stack
def push(stack, value):
    stack.append(value)
    
# remove the topmost element of the stack
# and return its value    
def pop(stack):
    if not empty(stack):
        return stack.pop()
    else:
        return None
    
# return true if the stack is empty
def empty(stack):
    return len(stack) == 0

# display stack
def display(stack):
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()


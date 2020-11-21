class Stack:

    def __init__(self):
        self.top = -1
        self.S = []

    def stack_empty(self):
        return self.top == -1

    def push(self,x):
        self.top += 1
        self.S.append(x)

    def pop(self):
        if (self.stack_empty()):
            print("Stack is empty")
            return None
        else:
            self.top -= 1
            return self.S[self.top+1]

    def peek(self):
        return self.S[self.top]

stack = Stack()
stack.pop()
stack.pop()
stack.push(10)
stack.push(15)
print(stack.pop())
print(stack.top)
print(stack.pop())
print(stack.top)
print(stack.stack_empty())
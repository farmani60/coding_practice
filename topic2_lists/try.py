

def isBalanced(expression):
    stack = list()
    for c in expression:
        if c == '{':
            stack.append('}')
        elif c == '[':
            stack.append(']')
        elif c == '(':
            stack.append(')')
        else:
            if (not stack) or (stack[-1] != c):
                return False
            stack.pop()
    return not stack


class Stack:
    def __init__(self):
        self.stack = []
    def add(self, data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def remove(self):
        if len(self.stack) <= 0:
            return False
        else:
            return self.stack.pop()

class Queue:
    def __init__(self):
        self.queue = []
    def add(self, data):
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False
    def size(self):
        return len(self.queue)
    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
print(AStack.remove())
print(AStack.peek())
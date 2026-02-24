#14_queue_using_stackes.py
#
#
#

class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, x: int):
        self.in_stack.append(x)
    
    def pop(self, x: int):
        self.peek()
        return self.out_stack.pop()
    
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
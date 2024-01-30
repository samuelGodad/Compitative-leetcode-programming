class MyQueue:

    def __init__(self):
        self.stack_one =[]
        self.stack_two = []
        
        

    def push(self, x: int) -> None:
        self.stack_one.append(x)
        

    def pop(self) -> int:
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        if self.stack_two:
            return self.stack_two.pop()
        else:
            return None
        
    def peek(self) -> int:
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        if self.stack_two:
            return self.stack_two[-1]
        else:
            return None
        
        
        

    def empty(self) -> bool:
        return not self.stack_two and not self.stack_one
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
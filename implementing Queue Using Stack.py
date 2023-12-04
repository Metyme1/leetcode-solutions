class MyQueue:
    
    def __init__(self):
        
        self.p = []
        

    def push(self, x: int) -> None:
        self.p.append(x)
        

    def pop(self) -> int:
        return self.p.pop(0)

    def peek(self) -> int:
        return self.p[0]
        

    def empty(self) -> bool:
        return len(self.p)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
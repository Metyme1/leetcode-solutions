from collections import deque
class MyStack:
    
    def __init__(self):
        
        self.p = deque()
        

    def push(self, x: int) -> None:
        self.p.append(x)

    def pop(self) -> int:
        for i in range(len(self.p)-1):
            self.push(self.p.popleft())
        return self.p.popleft()
        

    def top(self) -> int:
        return self.p[-1]
       
        

    def empty(self) -> bool:
        return len(self.p)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
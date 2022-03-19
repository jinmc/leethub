from collections import Counter, defaultdict

class FreqStack:

    def __init__(self):
        self.stacks = defaultdict(list)
        self.ctr = Counter()
        self.max_freq = 0

    def push(self, val: int) -> None:
        
        if val in self.ctr:
            self.ctr[val] += 1
        else:
            self.ctr[val] = 1
        self.max_freq = max(self.max_freq, self.ctr[val])
        self.stacks[self.ctr[val]].append(val)
        
    def pop(self) -> int:
        popped = self.stacks[self.max_freq].pop()
        self.ctr[popped] -= 1
        if len(self.stacks[self.max_freq]) == 0:
            self.max_freq -= 1
                    
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
class Bitset:
    def __init__(self, size: int):
        self.bitlist = [0] * size
        self.size = size
        self.flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.flipped and self.bitlist[idx] == 1:
            self.ones += 1     
            self.bitlist[idx] = 0
        elif not self.flipped and self.bitlist[idx] == 0:
            self.ones += 1 
            self.bitlist[idx] = 1
        
    def unfix(self, idx: int) -> None:
        if self.flipped and self.bitlist[idx] == 0:
            self.ones -= 1
            self.bitlist[idx] = 1
        elif not self.flipped and self.bitlist[idx] == 1:
            self.ones -= 1
            self.bitlist[idx] = 0
        
    def flip(self) -> None:
        self.flipped = ~self.flipped
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        
        if not self.flipped:
            # print("bitlist", self.bitlist)
            str_list = [str(s) for s in self.bitlist]
            # print("str_list", str_list)
            return "".join(str_list)
        else:
            # print("bitlist", self.bitlist)
            str_list = [str(abs(s-1)) for s in self.bitlist]
            # print("str_list", str_list)
            return "".join(str_list) 

        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
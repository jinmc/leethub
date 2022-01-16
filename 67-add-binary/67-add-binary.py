class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        result = []
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            
            num = carry % 2
            if carry >= 2:
                carry = 1
            else:
                carry = 0
            result.append(str(num))
        return "".join(result)[::-1]
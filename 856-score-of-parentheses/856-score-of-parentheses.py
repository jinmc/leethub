class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def recurse(st, isValid=False):
            # print(st)
            if st == "()":
                return 1
            if isValid:
                return 2 * recurse(st[1:-1])
            else: 
                stack = ["("]
                mid_point = 0
                for i in range(1, len(st)):
                    if st[i] == "(":
                        stack.append("(")
                    else:
                        stack.pop()
                    if len(stack) == 0:
                        mid_point = i
                        break
                # print(f'midpoint : {mid_point}')
                if mid_point == len(st)-1:
                    return recurse(st, True)
                return recurse(st[:mid_point+1], True) + recurse(st[mid_point+1:])
        return recurse(s)
        

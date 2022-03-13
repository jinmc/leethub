class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_set = set('({[')
        close_set = set('])}')
        for c in s:
            if c in open_set:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c ==')':
                    if stack.pop() != '(':
                        return False
                elif c == '}':
                    if stack.pop() != '{':
                        return False
                elif c == ']':
                    if stack.pop() != '[':
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
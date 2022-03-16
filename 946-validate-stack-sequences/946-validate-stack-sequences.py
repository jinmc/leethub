class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # initialize stack
        stack = []
        
        # push
        while pushed or popped:
            # print(stack, pushed, popped)
            
            if len(pushed) == 0:
                if not stack:
                    return False
                if stack[-1] != popped[0]:
                    return False
                else:
                    stack.pop()
                    popped.pop(0)
                
            # if nothing in popped
            elif len(popped) == 0:
                stack.append(pushed[0])
                pushed.pop(0)
            
            # if empty or last of pushed is not first of popped
            elif len(stack) == 0 or stack[-1] != popped[0]:
                stack.append(pushed[0])
                pushed.pop(0)
            
            elif len(pushed) == 0 and stack[-1] != popped[0]:
                return False
            
            # pop
            else:
                stack.pop()
                popped.pop(0)
        return True
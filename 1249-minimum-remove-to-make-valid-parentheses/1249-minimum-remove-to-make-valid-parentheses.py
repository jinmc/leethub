class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        slist = list(s)
        # print("slist", slist)
        c = 0
        stack = []
        while True:
            if len(slist) <= c:
                break
            # print(f'c : {c} slist[c]: {slist[c]}')
            if slist[c] != '(' and slist[c] != ")":
                c += 1
            elif slist[c] == '(':
                stack.append('(')
                c += 1
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                    c += 1
                else:
                    # print(f"pop c : {c}")
                    slist.pop(c)
                    
        c = len(slist) - 1
        openlen = len(stack)
        print(openlen, stack)
        while openlen > 0:
            if slist[c] == "(":
                slist.pop(c)
                openlen -= 1
            c -= 1
        return "".join(slist)
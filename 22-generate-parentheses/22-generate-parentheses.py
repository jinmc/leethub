class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def recurse(o=0, c=0, lst=[]):
            if o == c and o == n:
                ans.append("".join(lst))
                return
            elif o == c:
                lst.append("(")
                recurse(o+1, c, lst)
            elif o == n:
                lst.append(")")
                recurse(o, c+1, lst)
            else:
                # ["(("]
                for i in range(2):
                    new_list = list(lst)
                    new_list.append("()"[i])
                    if i == 0:
                        recurse(o+1, c, new_list)
                    else:
                        recurse(o, c+1, new_list)        
        ans = []
        recurse()
        return ans
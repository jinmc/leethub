class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def recurse(l=0,r=0,lst=[]):
            if l == n and r == n:
                ans.append("".join(lst))
                return
            elif l == n:
                lst.append(")")
                recurse(l, r+1, lst)
            elif l == r:
                lst.append("(")
                recurse(l+1, r, lst)
            else:
                for i in range(2):
                    new_list = list(lst)
                    new_list.append("()"[i])
                    recurse(l + 1 - i, r + i, new_list)
        recurse()
        return ans
                    
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        isNeg = False
        # isStart = False
        res = ""
        for i in range(len(s)):
            if i == 0 and (s[i] == "-" or s[i] == "+"):
                if s[i] == "-":
                    res += "-"
            elif not s[i].isnumeric():
                break
            else:
                res += s[i]
                

        if res == "" or res == "-":
            return 0
        int_res = int(res)
        if int_res < -2**31:
            return -2**31
        elif int_res >= 2**31 - 1:
            return 2**31 - 1
        else:
            return int_res

class Solution:
    def romanToInt(self, s: str) -> int:
        c = 0
        result = 0
        while c < len(s):
            # print("c", c)
            # print(s[c])
            # print(s[c:2])
            if s[c:c+2] == "CM":
                result += 900
                c += 1
            elif s[c] == "M":
                result += 1000
            elif s[c:c+2] == "CD":
                result += 400
                c += 1
            elif s[c] == "D":
                result += 500
            elif s[c:c+2] == "XC":
                result += 90
                c += 1
            elif s[c] == "C":
                result += 100
            elif s[c:c+2] == "XL":
                result += 40
                c += 1
            elif s[c] == "L":
                result += 50
            elif s[c:c+2] == "IX":
                c += 1
                result += 9
            elif s[c] == "X":
                result += 10
            elif s[c:c+2] == "IV":
                result += 4
                c += 1
            elif s[c] == "V":
                result += 5
            elif s[c] == "I":
                result += 1
            else:
                print("edge case")
            # print(result)
            
            c += 1
        return result
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            remain = 64 + columnNumber % 26
            if remain == 64:
                if columnNumber // 26 != 0:
                    columnNumber = columnNumber // 26 - 1
                    remain = 90
            else:
                columnNumber = columnNumber // 26
            # print(remain)
            # print(chr(remain))
            result = chr(remain) + result
        return result
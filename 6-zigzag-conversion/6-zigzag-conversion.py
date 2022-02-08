class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists = [[] for _ in range(numRows)]
        print(lists)
        row, down = 0, True
        for c in s:
            lists[row].append(c)
            if down and (row + 1 < numRows):
                row += 1
            elif down and (row + 1 == numRows):
                down = False
                row -= 1
            elif not down and row > 0:
                row -= 1
            elif not down and row == 0:
                row += 1
                down = True
        return "".join(["".join(lst) for lst in lists])

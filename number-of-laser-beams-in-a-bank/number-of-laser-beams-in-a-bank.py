class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        latest = 0
        result = 0
        for i in range(len(bank)):
            this_count = 0
            for j in range(len(bank[0])):
                # print(i, j)
                if bank[i][j] == '1':
                    this_count += 1
            if latest == 0:
                latest = this_count
            else:
                if this_count == 0:
                    continue
                result += this_count * latest
                latest = this_count
            # print("this_count", this_count)
            # print("latest", latest)
            # print("result", result)
        
        return result
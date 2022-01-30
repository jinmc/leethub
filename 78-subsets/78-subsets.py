class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        for num in nums:
            temp = []
            for curr in output: # curr = []
                # curr.extend([num])
                # output.append(curr)
                curr_temp = list(curr)
                curr_temp.extend([num]) # curr = [1]
                temp.append(curr_temp) # temp = [[1]]
            # temp = [curr + [num] for curr in output]
            # output.append(temp)
            output.extend(temp) # output = [[], [[1]]]
            print(temp, output)
        return output
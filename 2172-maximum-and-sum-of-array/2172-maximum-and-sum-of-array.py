class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        ans = 0
        for i in range(1000):
            random.shuffle(nums) # try different order randomly
            cur = 0
            counter = defaultdict(int)
            for n in nums:
                j = 0
                for i in range(1, numSlots+1): # Greedy part
                    if counter[i] < 2 and n & i > n & j:
                        j = i
                counter[j] += 1
                cur += n & j
            ans = max(ans, cur)
    
        return ans    
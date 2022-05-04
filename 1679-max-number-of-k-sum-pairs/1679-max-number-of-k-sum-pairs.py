from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ctr = Counter(nums)
        cnt = 0
        
        print(ctr)
        for key, val in ctr.items():
            # if key == k // 2:
            #     cnt += val
            # else:
            if k-key in ctr:
                print(key, k-key, val, ctr[k-key])
                cnt += min(val, ctr[k-key])
        print(cnt)
        return cnt // 2
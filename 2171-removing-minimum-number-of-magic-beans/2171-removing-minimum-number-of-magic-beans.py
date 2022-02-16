class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        this_sum = sum(beans)
        beans.sort()
        result = this_sum
        for i in range(len(beans)):
            bag_num = len(beans)-i
            result = min(result, this_sum - beans[i] * bag_num)
        return result

# [1,4,5,6] => [1,1,1,1] 전체합 - 1*4
# [1,4,5,6] => [0,4,4,4] 전체합 - 4*3
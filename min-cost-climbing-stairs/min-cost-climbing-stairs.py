## n개가 있다고 하면
## n = 100
## n-1번째까지의 최적의 값 vs n-2까지의 최적의값 + n번째
## n-1번째는 
## n-2번째까지의 최적의 값 vs n-3까지의 최적의 값 + n-1번째
## 2^n

# 1일때 최적의값 (1이 들어갈 때) -> list[0]
# 2일 때(2가 들어갈때) > list[1]
# 3일때는 1+3이랑 2랑 비교 > list[2]
# 4일때는 2+4랑 3이랑 비교 > list[3] ....
# n번째는 list[n-1]
# n 번만 계산
# O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = []
        for i in range(len(cost)):
            if i < 2:
                result.append(cost[i])
            else:
                this_item = min(cost[i] + result[-1], cost[i] + result[-2])
                result.append(this_item)
        # print(result)
        return min(result[-1], result[-2])
class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        N, output = len(nums), 0
        divisors = []
        counter = Counter()
        
        for i in range(1, k + 1):
            if k % i == 0:
                divisors.append(i)
        
        for i in range(0, N):
            remainder = k // math.gcd(k, nums[i])
            output += counter[remainder]
            for divisor in divisors:
                if nums[i] % divisor == 0:
                    counter[divisor] += 1
            
        return output
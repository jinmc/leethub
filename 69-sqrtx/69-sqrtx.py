class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 1, x
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 <= x and (mid+1) ** 2 > x:
                return mid
            elif mid ** 2 < x:
                l = mid
            else:
                r = mid
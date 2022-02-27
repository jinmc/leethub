from functools import reduce

class Solution:    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def cal_trips(time_took):
            res = 0
            for tm in time:
                res += time_took // tm
            return res
        
        l, h = 0, 10 ** 14
        mid = 10 ** 14
        while l <= h:
            mid = (l + h) // 2
            # print("mid: ", mid, "cal_trips(mid)", cal_trips(mid), "totalTrips: ", totalTrips, "l",l,"h",h)
            if cal_trips(mid) >= totalTrips:
                if cal_trips(mid-1) < totalTrips:
                    return mid
                h = mid - 1
            elif cal_trips(mid) < totalTrips:
                if cal_trips(mid+1) == totalTrips:
                    return mid+1
                l = mid + 1
            
        return mid
        
        
        
        ## time limit exceeded
        # res=0
        # t = 1
        # while True:
        #     for tm in time:
        #         if t % tm == 0:
        #             res += 1
        #     if res >= totalTrips:
        #         break
        #     t += 1
        # return t
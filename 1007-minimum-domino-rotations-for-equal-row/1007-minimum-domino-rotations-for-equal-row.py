class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # (2,5) => 2 ans -> 0
        # (5,2) => 2 (swap) ans -> 1
        # (2,6) => 2 ans -> 1
        # (4,2) => 2 (swap) ans -> 2
        
        # for loop를 두번 사용
        # 처음 for loop -> candidate 구함 (1개 또는 2개의 candidate가 나옴)
        # 두번째 for loop는 ans 구함
        candidate = [tops[0],bottoms[0]]
        candidate = list(set(candidate))
        for i in range(1,len(tops)):
            can1 = candidate[0]
            if can1 not in [tops[i], bottoms[i]]:
                candidate.remove(can1)
            if len(candidate) == 2:
                can2 = candidate[1]
                if can2 not in [tops[i], bottoms[i]]:
                    candidate.remove(can2)
            if len(candidate) == 0:
                return -1
            print(candidate)
            
        # [top index 0, bottom index 0, top index 1, bottom index 1]
        ans = [0 for _ in range(len(candidate)*2)]
        for i in range(len(tops)):
            if tops[i] == candidate[0] and bottoms[i] != candidate[0]:
                ans[1] += 1
            if bottoms[i] == candidate[0] and tops[i] != candidate[0]:
                ans[0] += 1
            
            if len(candidate) == 2:
                if bottoms[i] == candidate[1] and tops[i] != candidate[1]:
                    ans[2] += 1
                if tops[i] == candidate[1] and bottoms[i] != candidate[1]:
                    ans[3] += 1
                
        return min(ans)
                
        
        
            
            
        
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # "abcdabcdabcde" O(n^2)
        idx = s.index(c)
        answer = [0 for _ in range(len(s))]
        count = 0
        for i in range(idx, -1, -1):
            answer[i] = count
            count += 1
        count = 0
        
        last_idx = -1
        for i in range(idx, len(s)):
            if s[i] == c:
                count = 0
                last_idx = i
            else:
                count += 1
                answer[i] = count
            # print(f'i : {i} count :  {count}')
        
        count =0
        for i in range(last_idx, idx, -1):
            if s[i] == c:
                count = 0
            else:
                count += 1
                answer[i] = min(count, answer[i])
        return answer
            
            
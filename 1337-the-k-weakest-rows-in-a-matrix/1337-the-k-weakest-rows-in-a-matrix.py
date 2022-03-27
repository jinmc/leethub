class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst = []
        for i in range(len(mat)):
            lst.append((sum(mat[i]), i))
        # print(lst)
        lst.sort()
        # print(lst)
        return [x[1] for x in lst[:k]]
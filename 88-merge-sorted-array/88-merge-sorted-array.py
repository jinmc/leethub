class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_list = [0] * (m+n)
        count, idx1, idx2 = 0, 0, 0
        
        while count < m+n:
            if idx2 >= n or (idx1 < m and nums1[idx1] < nums2[idx2]):
                new_list[count] = nums1[idx1]
                idx1 += 1
            else:
                new_list[count] = nums2[idx2]
                idx2 += 1
            # print(count, new_list)
            count += 1
        # print(new_list)
        for i in range(len(new_list)):
            nums1[i] = new_list[i]

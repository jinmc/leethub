class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        
        # create a prefix sum array of nums
        prefix_sum = [0] + list(itertools.accumulate(nums))
        
        @functools.lru_cache(None)
        def get_min_largest_split_sum(curr_index: int, subarray_count: int):
            #base case: if there is only one subarray left, then all of the remaining numbers
            # must go in the current subarray. so return the sum of the remaining numbers
            if subarray_count == 1:
                return prefix_sum[n] - prefix_sum[curr_index]
            
            # otherwise, use the recurrence relation to determine the minimum largest subarray sum
            # between curr_index and the end of the array with subarray_count subarrays remaining
            minimum_largest_split_sum = prefix_sum[n]
            for i in range(curr_index, n - subarray_count + 1):
                # store the sum of the first subarray
                first_split_sum = prefix_sum[i+1] - prefix_sum[curr_index]
                
                # find the maximum subarray sum for the current
                largest_split_sum = max(first_split_sum, get_min_largest_split_sum(i+1, subarray_count-1))
                
                # find the minimum among all possible combinations.
                minimum_largest_split_sum = min(minimum_largest_split_sum, largest_split_sum)
                
                if first_split_sum >= minimum_largest_split_sum:
                    break
            return minimum_largest_split_sum
        return get_min_largest_split_sum(0, m)
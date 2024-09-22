## T(c) : O (logn) using Binary Search

## S(c) : O(1)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)

        while (l < r):

            m = l + (r - l) // 2

            if(target < nums[m] ):
                r = m

            elif(target > nums[m]):
                l = m + 1

            else:
                return m
            
        return l


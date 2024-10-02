class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        l , r = 0, 1

        while (r < n):

            if nums[l] == 0 and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0
                l += 1
            
            elif nums[l] != 0:
                l += 1

            r += 1

## Two Pointer Solution

## T(C) -- O (n)
## S(C) -- O (1)



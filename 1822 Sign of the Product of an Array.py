# 1822 Leetcode Easy
# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:

        initialInt = 0

        for i in nums:
            if i == 0:
                return 0
            else:
                initialInt += (1 if i < 0 else 0)
            
        return -1 if initialInt % 2 else 1;

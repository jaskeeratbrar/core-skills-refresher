## T(C) : O(n^2)
## S(C) : O(1)

class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        for i in range(len(s)):

            

            left = right = i

            while(left >= 0 and right < len(s) and s[left] == s[right]):
                res += 1
                left -= 1
                right +=1
            
            left = i
            right = left + 1

            while(left >= 0 and right < len(s) and s[left] == s[right]):
                res += 1
                left -= 1
                right +=1
            
        
        return res




        

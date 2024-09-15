#T(c) = O(n)
#S(c) = O(1)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def nextValidChar(str, idx):
            backspace = 0

            while idx >= 0:

                if(backspace == 0 and str[idx] != '#'):
                    break
                elif (str[idx] == '#'):
                    backspace += 1
                else:
                    backspace -=1
                idx -= 1
            return idx

        idxS, idxT = len(s) - 1, len(t) - 1

        while idxS >= 0 or idxT >= 0:

            idxS = nextValidChar(s, idxS)
            idxT = nextValidChar(t, idxT)

            charC = s[idxS] if idxS >= 0 else " " 
            charS = t[idxT] if idxT >= 0 else " "

            if(charC != charS):
                return False

            idxS -= 1
            idxT -= 1

        return True

        

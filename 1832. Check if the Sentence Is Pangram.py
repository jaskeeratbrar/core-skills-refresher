# T(C) = O(len(sentence))
# S(C) = O(1) # Constant space and time
# Maximum space our hashmap can be initialized to is of 26

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        trackMap = {}

        for i in sentence:

            if i not in trackMap:
                trackMap[i] = 1
            else:
                trackMap[i] += 1

        if len(trackMap) != 26:
            return False
        else:
            return True
        

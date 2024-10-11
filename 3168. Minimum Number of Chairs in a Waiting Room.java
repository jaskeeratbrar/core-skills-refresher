class Solution {
    public int minimumChairs(String s) {

        int max = 0;

        int chairs = 0;

        for(int i = 0; i < s.length(); i++){

            if(s.charAt(i) == 'E'){
                chairs += 1;
            }
            else{
                chairs -= 1;
            }

            max = Math.max(max, chairs);


        }
        
        return max;
    }
}


// T(C): O(n)
// S(C): O(1)

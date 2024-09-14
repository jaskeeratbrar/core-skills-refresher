// T (C) : O(n)
// S (C) : O(1) # number of alphabets stored in hashmap

class Solution {
    public int firstUniqChar(String s) {

        Map<Character, Integer> map = new HashMap<>(); 

        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);

            if(!map.containsKey(c)){
                map.put(c, 1);
            }
            else{
                map.put(c, map.get(c) + 1);
            }

        }

        for(int j = 0; j < s.length(); j++){
            char c = s.charAt(j);

            if(map.get(c) == 1){
                return j;
            }

        }
        
        return -1;
    }
}

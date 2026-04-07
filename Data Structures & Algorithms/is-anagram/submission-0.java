class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) { return false; }
        HashMap<Character, Integer> letter_map = new HashMap<>();
        for(int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if(letter_map.containsKey(cur)) {
                letter_map.put(cur, letter_map.get(cur)+1);
            }
            else { letter_map.put(cur, 1); }
        }

        for(int i = 0; i < t.length(); i++) {
            char cur = t.charAt(i);
            if(!letter_map.containsKey(cur) 
                || letter_map.get(cur) == 0) 
                { return false; }
            letter_map.replace(cur, letter_map.get(cur)-1);
        }
        return true;
    }
}

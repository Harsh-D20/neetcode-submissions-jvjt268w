class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase().trim();
        int j = s.length()-1;
        for(int i = 0; i < s.length()/2; i++) {
            while(!Character.isLetterOrDigit(s.charAt(i))) { 
                i++;
                if(i >= j) { return true; }
            }
            while(!Character.isLetterOrDigit(s.charAt(j))) {
                j--;
                if(j <= i) { return true; }
            }
            if(s.charAt(i) != s.charAt(j)) { return false; }
            j--;
        }    
        return true;
    }
}

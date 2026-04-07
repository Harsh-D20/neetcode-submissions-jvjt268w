class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        for(int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if(cur == '(' || cur == '{' || cur == '[') {
                stk.push(cur);
            }
            else {
                if(stk.empty()) { return false; }
                if((cur == ')' && stk.peek() == '(')
                || (cur == ']' && stk.peek() == '[')
                || (cur == '}' && stk.peek() == '{')) { 
                    stk.pop(); 
                    }
                else return false;
            }
        }
        if(stk.empty()) { return true; }
        return false;
    }
}

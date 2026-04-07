class Solution {
    ArrayList<Integer> cache = new ArrayList<Integer>(Collections.nCopies(45,0));
    public int climbStairs(int n) {
        if(n == 1) { return 1; }
        if(n == 2) { return 2; }
        if(cache.get(n-1) != 0) { return cache.get(n-1); }
        cache.set(n-1, climbStairs(n-1) + climbStairs(n-2));
        return cache.get(n-1);
    }
}
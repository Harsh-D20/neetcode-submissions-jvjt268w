class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" or s == None: return 0
        max_len = 1
        left = 0
        window = s[left:left+1]
        seen = set(s[left:left+1])
        
        for right in range(1, len(s)):
            next = s[right:right + 1]
            if next in seen:
                while next in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(next)
            right += 1
            window = s[left:right]
            max_len = max(len(window), max_len)
        return max_len
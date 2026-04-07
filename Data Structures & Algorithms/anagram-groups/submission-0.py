from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freq = [0 for _ in range(26)]
            for c in s:
                freq[ord(c) - ord('a')] += 1
            if tuple(freq) in groups:
                groups[tuple(freq)].append(s)
            else:
                groups[tuple(freq)] = [s]
        out = []
        for g,ss in groups.items():
            out.append(ss)
        return out
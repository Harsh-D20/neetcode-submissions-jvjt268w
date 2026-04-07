class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += s + "\t"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        words = []
        end_of_last = 0
        for i,c in enumerate(s):
            if c == "\t": 
                words.append(s[end_of_last:i])
                end_of_last = i+1
        return words
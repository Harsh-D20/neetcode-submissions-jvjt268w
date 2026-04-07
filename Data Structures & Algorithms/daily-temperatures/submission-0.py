class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stk = []
        for i,t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                _, stk_idx = stk.pop()
                result[stk_idx] = i - stk_idx
            stk.append((t, i))
        return result
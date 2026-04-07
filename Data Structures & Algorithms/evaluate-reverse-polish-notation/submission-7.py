class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = set(["+", "-", "*", "/"])
        for t in tokens:
            print(t, stk)
            if t not in ops:
                stk.append(int(t))
            if t in ops:
                b = stk.pop()
                a = stk.pop()
                if t == "+":
                    stk.append(a + b)
                if t == "-":
                    stk.append(a - b)
                if t == "*":
                    stk.append(a * b)
                if t == "/":
                    res = a / b
                    res = math.ceil(res) if res < 0 else math.floor(res)
                    stk.append(res)
        return stk.pop()
                
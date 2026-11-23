class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for ch in tokens:
            if ch not in '+-/*':
                stk.append(int(ch))
            else:
                valTwo = stk.pop()
                valOne = stk.pop()
                if ch == '+':
                    stk.append(valOne + valTwo)
                elif ch == '-':
                    stk.append(valOne - valTwo)
                elif ch == '*':
                    stk.append(valOne * valTwo)
                else:
                    stk.append(int(valOne/valTwo))
        return stk[-1]


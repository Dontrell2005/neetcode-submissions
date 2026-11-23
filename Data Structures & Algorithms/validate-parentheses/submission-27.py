class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        m = {'[':']', '{': '}', '(':')'}
        stk = []
        for ch in s:
            if ch in m.keys():
                stk.append(ch)
            elif stk and m[stk[-1]] == ch:
                stk.pop()
            else:
                return False
        return len(stk) == 0
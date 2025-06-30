class Solution(object):
    def backspaceCompare(self, s, t):
        p1, p2 = len(s) - 1, len(t) - 1
        
        while p1 >= 0 or p2 >= 0:
            if (p1 >= 0 and s[p1] == '#') or (p2 >= 0 and t[p2] == '#'):
                if p1 >= 0 and s[p1] == '#':
                    backCount = 2
                    while backCount > 0:
                        p1 -= 1
                        backCount -= 1
                        if p1 >= 0 and s[p1] == '#':
                            backCount += 2
                if p2 >= 0 and t[p2] == '#':
                    backCount = 2
                    while backCount > 0:
                        p2 -= 1
                        backCount -= 1
                        if p2 >= 0 and t[p2] == '#':
                            backCount += 2
            else:
                if (p1 >= 0 and p2 >= 0 and s[p1] != t[p2]) or ((p1 >= 0) != (p2 >= 0)):
                    return False
                p1 -= 1
                p2 -= 1
        
        return True
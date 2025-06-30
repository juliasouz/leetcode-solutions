class Solution(object):
    def backspaceCompare(self, s, t):
        p1, p2 = len(s) - 1, len(t) - 1
    
        while p1 >= 0 or p2 >= 0:
            if (s[p1] == '#') or (t[p2] == '#'):
                if p1 >= 0 and s[p1] == '#':
                    back_count = 2
                    while back_count > 0:
                        p1 -= 1
                        back_count -= 1
                        if p1 >= 0 and s[p1] == '#':
                            back_count += 2
                if  t[p2] == '#':
                    back_count = 2
                    while back_count > 0:
                        p2 -= 1
                        back_count -= 1
                        if p2 >= 0 and t[p2] == '#':
                            back_count += 2
            else:
                if s[p1] != t[p2]:
                    return False
                else:
                    p1 -= 1
                    p2 -= 1
        return True
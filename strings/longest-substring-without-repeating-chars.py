class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
    
        seen_char = {}
        left = 0
        longest = 0

        for right in range(len(s)):
            current_char = s[right]
            previously_seen_char = seen_char.get(current_char)

            if previously_seen_char >= left:
                left = previously_seen_char + 1
        
            seen_char[current_char] = right
            longest = max(longest, right - left + 1)
    
        return longest
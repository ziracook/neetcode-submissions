class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest = 0

        curchars = set()

        while r < len(s):
            if s[r] not in curchars:
                curchars.add(s[r])
                r += 1
                longest = max(longest, len(curchars))
            else:
                curchars.remove(s[l])
                l += 1
        
        return longest

        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = {}
        largest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in store:
                l = max(store[s[r]] + 1, l)
            store[s[r]] = r
            largest = max(largest, r - l + 1)

        return largest
        
        
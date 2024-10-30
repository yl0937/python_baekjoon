class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == len(s):
            return len(s)
        max = 0
        maxRepeat = len(set(s))
        for i in range(maxRepeat,-1,-1):
            j = 0
            while j + i <= len(s):
                if len(set(s[j:j+i])) > max and len(set(s[j:j+i])) == len(s[j:j+i]):
                    max = len(set(s[j:j+i]))
                j += 1
        return max


s = Solution()
print(s.lengthOfLongestSubstring("bbbbb"))
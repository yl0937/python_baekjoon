class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for element in s:
            if 0 < ord(element) < 48 or 57 < ord(element) < 97 or 122 < ord(element) < 128:
                s = s.replace(element,"")
        if (s[::-1] != s) :
            return False
        else:
            return True

s = Solution()
print(s.isPalindrome("0P"))
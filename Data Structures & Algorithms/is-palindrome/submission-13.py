class Solution:
    '''
    Plan:
    - pointer: start + end of string
    - while l < r:
        if s[l] = ' ':
            l += 1
        if s[r] = ' ':
            r -= 1
        if and s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return false
        
    '''
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and (s[l].isalnum() == False):
                l += 1
            while l < r and (s[r].isalnum() == False):
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True



        
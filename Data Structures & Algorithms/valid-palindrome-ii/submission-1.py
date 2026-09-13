class Solution:
    def validPalindrome(self, s: str) -> bool:
        # If you don't need to ignore non-alnum / case for this LeetCode problem,
        # you can drop the isalnum/lower handling. Keeping it here for minimal change.
        def is_pal(i, j):
            while i < j:
                while i < j and not s[i].isalnum():
                    i += 1
                while i < j and not s[j].isalnum():
                    j -= 1
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                # Try deleting left OR right char exactly once
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True
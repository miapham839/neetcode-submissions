class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        
        # Transform string to handle even/odd lengths uniformly without bounds checking
        # Example: "abc" -> "^#a#b#c#$"
        t = "^#" + "#".join(s) + "#$"
        n = len(t)
        
        # Array to store the palindrome radius at each center
        p = [0] * n
        
        center = 0
        right_boundary = 0
        
        for i in range(1, n - 1):
            # Find the mirror index of 'i' relative to the current 'center'
            mirror = 2 * center - i
            
            # If 'i' is within the right boundary, initialize with the mirrored value
            if i < right_boundary:
                p[i] = min(right_boundary - i, p[mirror])
                
            # Attempt to expand the palindrome centered at 'i'
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
                
            # If the new palindrome extends past the current right boundary, adjust the center
            if i + p[i] > right_boundary:
                center = i
                right_boundary = i + p[i]
                
        # Each radius p[i] represents a maximum palindrome of length p[i] in the original string.
        # A max length of p[i] contributes (p[i] + 1) // 2 palindromic substrings from that center.
        return sum((radius + 1) // 2 for radius in p)
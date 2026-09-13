class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        - U
            I: two strings s and t
            O: boolean
                - True: s and t are anagrams (contains the exact same characters not considering order)
                - False: s and t are NOT anagrams
            C: s and t are lowercase letters.
            E: 
            - 2 empty strings
            - contains numbers
        - Plan:
            initiate an empty dic_s 
            [aim: key: char, val: number of occurences of that character]
            - iterate through s
                if char in dic:
                    increment its value by 1
                else
                    add it to dic with value of 1
            initiate an empty dic_t
            - iterate through t:
                do the same
            check if dic_s == dic_t
        '''
        dic_s = {}
        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 1
        dic_t = {}
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 1   
        return dic_s == dic_t         
        
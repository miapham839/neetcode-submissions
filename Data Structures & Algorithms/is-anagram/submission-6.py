class Solution:
    '''
    - I: 2 strings s and t
    - O: T: anagrams (contains the exact same characters)
         F: not anagrams
    - E: empty string

    Plan:
    init hasmap1
    iterate over 1st string. for each char, add to set (k,v) = (char, freq)
    init hashmap2
    interate over 2nd string. for each char, add to set (k,v) = (char, freq)
    return hasmap1 == hashmap2
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for char in s:
            if dict1.get(char) != None:
                dict1[char] += 1
            else:
                dict1[char] = 1
        dict2 = {}
        for char in t:
            if dict2.get(char) != None:
                dict2[char] += 1
            else:
                dict2[char] = 1
        return dict1 == dict2

        
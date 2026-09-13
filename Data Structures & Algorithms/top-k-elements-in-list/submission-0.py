class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        - U
            - I: integer array
            - O: array containing k most frequent elements. order does not matter
            - C
            - E:
                - There are 2 numbers with the same frequency
                -> Take smaller number
        - P: 
            - Initialize a dictionary. Loop through the array and add K-V pairs as num-frequency pairs
            - Get the frequency list -> sort descending
            - Get the nums associated with the k top frequencies
        '''
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        freq_list = list(freq.items()) #list of tuples of K-V pairs
        #sort the dictionary based on descending values
        def sort_key(pair):
            num = pair[0]
            freq = pair[1]
            return (-freq, num)
        freq_list.sort(key=sort_key)
        res = []
        for i in range (k):
            res.append(freq_list[i][0])
        return res
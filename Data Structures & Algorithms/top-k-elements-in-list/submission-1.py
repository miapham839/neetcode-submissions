class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        - dung chuot nhieu hon de wak through
        - dung de silence
        - viet comment
        - shorter intro
        - time complexity ki hon
        - ask to make assumption if forget syntax
        - edge cases questions
        - Viet plan ra truoc (psuedocode)
        - Say brute force (optional) and ask if you want me to implement brute force
        - use smart variable names

        Plan:
        - init hashmap
        - int res
        - loop through nums -> create hashmap with num-freq as K-V pairs 
        - loop through freq list -> choose k largest freqs
        - get the values associated with that freq -> append to res list
        '''
        res = []
        dic = {}
        # Loop through nums -> create hashmap with num-freq as K-V pairs
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        # List of tuples of K-V pairs
        freq_list = list(dic.items())
        def swap_kv(e):
            val = e[0]
            freq = e[1]
            return (freq, val)
        # Sort based on frequency
        freq_list.sort(reverse=True, key=swap_kv)
        # Append to res list
        for i in range(k):
            res.append(freq_list[i][0])
        return res
        


        
        
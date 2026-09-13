class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        U:
        - I: list of strings
        - O: list of lists, with sublists containing words that are anagram of each other
                - if a word has no anagram, it has its own sublist
                - if the input list is a mere empty string, it has its own sublist
                (every word must be in a sublist even if it has no anagram)
        - C: each string in the list is made up of lowercase eng letters
        P:
        - initiate res_list
        - initiate dic_dic
        - for i in strs:
            create an empty list and append i
            create a dic wit K-V pairs = char:char count
            if dic in dic_dic.keys():
                #How to find the specific sublist that contains the anagram?
                 #To keep track of where the sublist is -> initiate a dictionary with K-V: dic: index in res_list
                append i to res_list[dic_dic[dic]]
            else if dic NOT in dic_dic.keys():
                #add dic to dic_list
                add sublist to res_list
                add dic: res_list.index(sublist) to dic_dic
        return res_list
            ##How are sublists arranged?
             ##output can be in any order --> are the elements in each sublit can be in any order too?
        '''
        res_list = []
        dic_dic = {}
        for i in strs:
            sublist = [i]
            char_dic = {}
            for j in i:
                if j in char_dic:
                    char_dic[j] += 1
                else:
                    char_dic[j] = 1
            char_dic = tuple(sorted(char_dic.items()))
            if char_dic in dic_dic.keys():
                to_append = res_list[dic_dic[char_dic]]
                to_append.append(i)
            else:
                res_list.append(sublist)
                dic_dic[char_dic] = res_list.index(sublist)
        return res_list
        
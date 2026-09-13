class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> charactersS = new HashMap<>();
        for (int i = 0; i < s.length(); i++){
            //If char already in hashmap
            if (charactersS.containsKey(s.charAt(i))){
                //Increment the key by 1
                charactersS.replace(s.charAt(i), ((charactersS.get(s.charAt(i)))+1));
            } else{
                //If char not already in hashmap
                charactersS.put(s.charAt(i), 1);
            }
        }
        System.out.println(charactersS);
        HashMap<Character, Integer> charactersT = new HashMap<>();
        for (int i = 0; i < t.length(); i++){
            //If char already in hashmap
            if (charactersT.containsKey(t.charAt(i))){
                //Increment the key by 1
                charactersT.replace(t.charAt(i), (charactersT.get(t.charAt(i))+1));
            } else{
                //If char not already in hashmap
                charactersT.put(t.charAt(i), 1);
            }
        }
        System.out.println(charactersT);
        return (charactersS.equals(charactersT));
        //Sorting option that optimizes space complexity
    }
}

class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Brute force
        // for (int j = 0; j < nums.length; j++){
        //     for (int i = 0; i < nums.length; i++){
        //         if ((i != j) && (nums[i] == nums[j])){
        //             return true;
        //         }
        //     }
        // }
        // return false;
        //Hash Table
        HashSet<Integer> pastNums = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if (pastNums.contains(nums[i])){
                return true;
            }
            pastNums.add(nums[i]);
        }
        return false;
    }
}

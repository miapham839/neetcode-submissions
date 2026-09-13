class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Brute force
        // for (int i = 0; i < nums.length; i++){
        //     for (int j = 0; j < nums.length; j++){
        //         if ((i != j) && (nums[j] == nums[i])){
        //             return true;
        //         }
        //     }
        // }
        // return false;
        //Optimized with HashSet
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++){
            if (set.contains(nums[i])){
                return true;
            }
            set.add(nums[i]);
        }
        return false;
    }
}

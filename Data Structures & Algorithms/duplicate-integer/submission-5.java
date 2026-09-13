class Solution {
    public boolean hasDuplicate(int[] nums) {
        for (int j = 0; j < nums.length; j++){
            for (int i = 0; i < nums.length; i++){
                if ((i != j) && (nums[i] == nums[j])){
                    return true;
                }
            }
        }
        return false;
    }
}

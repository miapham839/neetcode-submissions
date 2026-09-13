class Solution {
    public boolean hasDuplicate(int[] nums) {
        //boolean res = false;
        int j = 0;
        while (j < nums.length){
            for (int i = 0; i < nums.length; i++){
                if ((i != j) && (nums[i] == nums[j])){
                    return true;
                }
            }
            j++;
        }
        return false;
    }
}

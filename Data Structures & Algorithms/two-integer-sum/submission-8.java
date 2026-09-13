class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        //Brute force
        // for (int i = 0; i < nums.length; i++){
        //     for (int j = 0; j < nums.length; j++){
        //         if ((i != j) && (nums[i] + nums[j] == target)){
        //             if (i < j){
        //                 res[0] = i;
        //                 res[1] = j;
        //             } else{
        //                 res[0] = j;
        //                 res[1] = i;
        //             }
        //         }
        //     }
        // }
        // return res;

        //Hashmap
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            int difference = target - nums[i];
            if (map.get(difference) == null){
                map.put(nums[i], i);
            } else{
                res[0] = map.get(difference);
                res[1] = i;                  
            }
        }
        return res;
    }
}

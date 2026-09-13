class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder rawS = new StringBuilder();
        for (int i = 0; i < s.length(); i++){
            if (Character.isLetterOrDigit(s.charAt(i))){
                rawS.append((Character.toLowerCase(s.charAt(i))));
            }
        }
        boolean res = true;
        int i = 0;
        int j = rawS.length() - 1;
        while (!(j <= i)){
            if (rawS.charAt(j) == rawS.charAt(i)){
                res = true;
            }
            else{
                res = false;
            }
            i++;
            j--;
        }
        return res;   
    }
}

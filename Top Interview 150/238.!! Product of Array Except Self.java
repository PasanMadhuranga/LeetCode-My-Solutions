class Solution {
    public int[] productExceptSelf(int[] nums) {
        // Length of the input array
        int l = nums.length;

        // Initialize the answer array of the same length
        int[] answer = new int[l];

        // preArr stores the product of all elements to the left of the current index
        int[] preArr = new int[l];

        // sufArr stores the product of all elements to the right of the current index
        int[] sufArr = new int[l];

        // Initialize the first element of preArr as 1 since there are no elements to
        // the left of the first element
        preArr[0] = 1;

        // Initialize the last element of sufArr as 1 since there are no elements to the
        // right of the last element
        sufArr[l - 1] = 1;

        // Calculate the prefix product for each element
        for (int i = 1; i < l; i++) {
            preArr[i] = preArr[i - 1] * nums[i - 1];
        }

        // Calculate the suffix product for each element
        for (int i = l - 2; i >= 0; i--) {
            sufArr[i] = sufArr[i + 1] * nums[i + 1];
        }

        // Calculate the product of all elements except self
        // by multiplying the prefix and suffix products
        for (int i = 0; i < l; i++) {
            answer[i] = preArr[i] * sufArr[i];
        }

        return answer;
    }
}

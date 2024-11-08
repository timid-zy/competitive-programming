# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        vector<int> res;
        int total = 0;
        int ceil = (1 << maximumBit) - 1;
        for (int i = 0; i < size(nums); i++) {
            total = total ^ nums[i];
            res.push_back(total ^ ceil);
        }   

        reverse(res.begin(), res.end());
        return res;
    }
};
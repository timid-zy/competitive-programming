# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> dct;
        for (int i = 0; i < size(nums); i++) {
            if (dct.find(target-nums[i]) != dct.end()) {
                return {dct[target-nums[i]], i};
            }
            dct[nums[i]] = i;
        }

        return {0, 0};
    }
};
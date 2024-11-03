# Problem: Partition Array According to Given Pivot - https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> arr;
        for (int i = 0; i < size(nums); i++) {
            if (nums[i] < pivot) {
                arr.push_back(nums[i]);
            }   
        }

        for (int i = 0; i < size(nums); i++) {
            if (nums[i] == pivot) {
                arr.push_back(nums[i]);
            }   
        }

        for (int i = 0; i < size(nums); i++) {
            if (nums[i] > pivot) {
                arr.push_back(nums[i]);
            }   
        }

        return arr;
    }
};
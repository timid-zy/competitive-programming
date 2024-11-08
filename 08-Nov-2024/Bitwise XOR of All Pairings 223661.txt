# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int total = 0;

        if (size(nums1) % 2 == 1) {
            for (int n: nums2) total ^= n;
        }      

        if (size(nums2) % 2 == 1) {
            for (int n: nums1) total ^= n;
        }

        return total;
    }
};
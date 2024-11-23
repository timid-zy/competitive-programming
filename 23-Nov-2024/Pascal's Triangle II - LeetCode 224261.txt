# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res = {1};
        for (;rowIndex > 0; rowIndex--) {
            vector<int> tmp = {1};
            for (int i = 1; i < size(res); i++) {
                tmp.push_back(res[i] + res[i-1]);
            }

            tmp.push_back(1);
            res = tmp;
        }

        return res;
    }
};
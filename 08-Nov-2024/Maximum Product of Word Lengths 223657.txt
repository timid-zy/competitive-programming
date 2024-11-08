# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector<int> mask;
        for (int i = 0; i < size(words); i++) {
            mask.push_back(0);
            for (int j = 0; j < size(words[i]); j++) {
                mask[i] = mask[i] | (1 << (words[i][j] - 'a'));
            }
        }

        int res = 0;
        for (int i = 0; i < size(words); i++) {
            for (int j = 0; j < size(words); j++) {
                if ((mask[i] & mask[j]) == 0) {
                    int cand = size(words[i]) * size(words[j]);
                    res = max(res, cand);
                }
            }
        }

        return res;
    }
};
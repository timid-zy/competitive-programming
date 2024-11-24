class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        int mn = pow(10, 5);
        int c = 0;
        long long sum = 0;
        for (vector<int> row: matrix) for (int val: row) {
            if (val < 0) {
                c += 1;
            }
            mn = min(abs(val), mn);
            sum += abs(val);
        }

        if (c % 2 == 0) return sum;
        return sum - 2*mn;
    }
};
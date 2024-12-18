class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        vector<int> stk;
        for (int i = size(prices)-1; i >= 0; i--) {
            while (size(stk) > 0 && stk[size(stk)-1] > prices[i]) stk.pop_back();
            int ov = prices[i];
            if (size(stk) > 0) {
                prices[i] -= stk[size(stk) - 1];
            }

            if (size(stk) == 0 || stk[size(stk) - 1] < ov) stk.push_back(ov);
        }

        return prices;
    }
};
# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<int> pd(n, pow(10, 9));
        pd[src] = 0;
        for (;k > -1; k--) {
            vector<int> cd(pd.begin(), pd.end());
            for (auto& f: flights) {
                cd[f[1]] = min(cd[f[1]], pd[f[0]] + f[2]);
            }

            pd.assign(cd.begin(), cd.end());
        }

        return pd[dst] < pow(10, 9) ? pd[dst] : -1;
    }
};
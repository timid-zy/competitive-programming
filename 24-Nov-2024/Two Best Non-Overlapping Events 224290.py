# Problem: Two Best Non-Overlapping Events - https://leetcode.com/problems/two-best-non-overlapping-events/

class Solution {
public:
    int maxTwoEvents(vector<vector<int>>& events) {
        sort(begin(events), end(events));
        int res = 0, prev = 0;
        priority_queue<pair<int, int>> heap;
        for (auto& e: events) {
            heap.push({-e[1], e[2]});
            while (!heap.empty() && -heap.top().first < e[0]) {
                prev = max(prev, heap.top().second);
                heap.pop();
            }

            res = max(res, prev + e[2]);
        }

        return res;
    }
};
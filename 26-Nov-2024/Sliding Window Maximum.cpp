class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> Q;
        vector<int> res;
        for (int i = 0; i < k; i++) {
            while (size(Q) > 0 && nums[i] > Q.back()) {
                Q.pop_back();
            }

            Q.push_back(nums[i]);
        }

        res.push_back(Q.front());
        int l = 0;
        for (int r = k; r < size(nums); r++) {
            if (nums[l++] == Q.front()) Q.pop_front();

            cout << endl;
            while (!Q.empty() && nums[r] > Q.back()) {
                Q.pop_back();
            }

            Q.push_back(nums[r]);
            res.push_back(Q.front());
        }

        return res;
    }
};
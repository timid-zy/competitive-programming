class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        map<int, int> mp;
        sort(arr.begin(), arr.end());
        for (int i = size(arr)-1; i >= 0; i--) {
            if (mp.find(arr[i]*2) != mp.end()) {
                return true;
            }

            mp[arr[i]] = i;
        }

        for (int i = 0; i < size(arr); i++) {
            if (mp.find(arr[i]*2) != mp.end() && i != mp[arr[i]*2]) {
                return true;
            }
        }

        return false;
    }
};
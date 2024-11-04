class Solution {
public:
    string compressedString(string word) {
        char prev = 0;
        int count = 0;
        string res = "";

        for (int i = 0; i < size(word); i++) {
            if (word[i] == prev) {
                count += 1;
                if (count == 9) {
                    res += to_string(count) + prev;
                    count = 0;
                }
            } else {
                if (count > 0) {
                    res += to_string(count) + prev;
                }

                prev = word[i];
                count = 1;
            }
        }

        if (count > 0) {
            res += to_string(count) + prev;
        }

        return res;
    }
};
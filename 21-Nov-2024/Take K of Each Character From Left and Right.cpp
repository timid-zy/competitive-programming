class Solution {
public:
    int takeCharacters(string s, int k) {
        int n = size(s);
        int count[3] = {-1 * k, -1 * k, -1 * k};
        for (int i = 0; i < size(s); i++) count[s[i]-'a']++;

        if (min({count[0], count[1], count[2]}) < 0) return -1;
        int curr[3] = { };
        int l = 0;
        int res = size(s)+1;
        for (int r = 0; r < size(s); r++) {
            curr[int(s[r]) - 'a']++;
            while (l <= r && curr[int(s[r])-'a'] > count[int(s[r])-'a'])  
                curr[int(s[l++]) - 'a']--;
            
            res = min(res, n-r+l-1);
        }

        return res;
    }
};
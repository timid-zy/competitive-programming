# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution {
public:
    string decodeHelper(int idx, string s) {
        if (idx == s.size()) {
            return "";
        }

        if (s[idx] == ']') {
            return "";
        }

        if (!isdigit(s[idx])) {
            return s[idx] + decodeHelper(idx+1, s);
        }

        string count = "";
        while (idx < s.size() && isdigit(s[idx])) {
            count += s[idx];
            idx += 1;
        }

        string res = "";
        if (s[idx] != ']' && s[idx] != '[') {
            for (int i = 0; i < stoi(count); i++) res += s[idx]; 
        }

        int lvl = 0;
        if (s[idx] == '[') {
            idx += 1;
            string rep = decodeHelper(idx, s);
            for (int i = 0; i < stoi(count); i++) res += rep; 
            lvl -= 1;
        }

        while (idx < size(s) && lvl < 0) {
            if (s[idx] == '[') lvl -= 1;
            if (s[idx] == ']') lvl += 1;
            idx += 1;
        }

        return res + decodeHelper(idx, s);
    }

public:
    string decodeString(string s) {
        return decodeHelper(0, s);
    }
};
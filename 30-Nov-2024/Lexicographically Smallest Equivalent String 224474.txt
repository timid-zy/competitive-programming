# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class DisjointSet {
public:
    map<char, char> mp;
    DisjointSet() {
        for (int i = 'a'; i <= 'z'; i++) {
            mp[char(i)] = char(i);
        }
    }

    char Find(char x) {
        char curr = x;
        while (curr != mp[curr]) {
            curr = mp[curr];
        }

        while (x != mp[x]) {
            char nx = mp[x];
            mp[x] = curr;
            x = nx;
        }

        return curr;
    } 

    void Union(char x, char y) {
        char X = Find(x), Y = Find(y);
        if (X < Y) {
            mp[Y] = X;
        } else {
            mp[X] = Y;
        }
    }
};

class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        map<char, int> count;
        DisjointSet dsj;
        for (int i = 0; i < size(s1); i++) {
            dsj.Union(s1[i], s2[i]);
        }

        string res;
        for (auto& e: baseStr) {
            res += dsj.Find(e);
        }

        return res;
    }
};
# Problem: Count Unguarded Cells in the Grid - https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        int mat[m][n];
        memset(mat, 0, sizeof(mat));
        for (auto& g: guards) mat[g[0]][g[1]] = 1;
        for (auto& w: walls) mat[w[0]][w[1]] = -1;

        int dir[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        for (auto& g: guards) {
            for (auto& di: dir) {
                int r = g[0], c = g[1];
                r -= di[0];
                c -= di[1];

                while (0 <= r && r < m && 0 <= c && c < n) {
                    if (mat[r][c] == 1 || mat[r][c] == -1) break;
                    mat[r][c] = 2;
                    r -= di[0];
                    c -= di[1];
                }
            }
        }

        int res = 0;
        for (auto& row: mat) for (auto& v: row) if (v == 0) res++;

        return res;
    }
};
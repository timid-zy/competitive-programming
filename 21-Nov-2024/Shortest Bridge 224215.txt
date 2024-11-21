# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution {
public:
    bool inbound(int x, int y, int n, int m) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

public:
    int shortestBridge(vector<vector<int>>& grid) {
        int n = size(grid), m = size(grid[0]);
        queue<vector<int>> Q;
        queue<vector<int>> Q2;
        bool visited[n][m];
        memset(visited, false, sizeof(visited));
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r][c] == 1) {
                    Q.push({r, c});
                    Q2.push({r, c, 0});
                    visited[r][c] = true;
                    break; 
                }
            }

            if (size(Q) > 0) break;
        }

        int dir[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        
        while (size(Q) > 0) {
            auto curr = Q.front();
            Q.pop();
            int x = curr[0], y = curr[1];

            for (auto& di: dir) {
                int nx = x + di[0], ny = y + di[1];
                if (inbound(nx, y + di[1], n, m) && grid[nx][ny] == 1 && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    Q.push({nx, ny});
                    Q2.push({nx, ny, 0});
                }
            }
        }

        while (size(Q2) > 0) {
            auto curr = Q2.front();
            Q2.pop();
            int x = curr[0], y = curr[1];

            for (auto& di: dir) {
                int nx = x + di[0], ny = y + di[1];
                if (inbound(nx, ny, n, m) && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    if (grid[nx][ny] == 1) return curr[2];
                    Q2.push({nx, ny, curr[2]+1});
                }
            }
        }

        return 0;
    }
};
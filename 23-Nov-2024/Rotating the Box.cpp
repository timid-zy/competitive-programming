class Solution
{
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>> &box)
    {
        int n = size(box), m = size(box[0]);
        for (int i = 0; i < n; i++)
        {
            int c = 0;
            for (int j = 0; j < m; j++)
            {
                if (box[i][j] == '#')
                {
                    c++;
                    box[i][j] = '.';
                }
                else if (box[i][j] == '.')
                    continue;
                else
                {
                    int ci = j;
                    for (; c > 0; c--)
                        box[i][--ci] = '#';
                }
            }

            int ci = m;
            for (; c > 0; c--)
                box[i][--ci] = '#';
        }

        vector<vector<char>> res;
        for (int i = 0; i < m; i++)
        {
            res.push_back({});
            for (int j = n - 1; j >= 0; j--)
            {
                res[i].push_back(box[j][i]);
            }
        }

        return res;
    }
};
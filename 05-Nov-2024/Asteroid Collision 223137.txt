# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> stk;
        for (int i = 0; i < size(asteroids); i++) {
            bool cont = false;
            while (size(stk) > 0 && stk[size(stk) - 1] > 0 && asteroids[i] < 0) {
                if (stk[size(stk) - 1] > asteroids[i] * -1) {
                    cont = true;
                    break;
                } else if (stk[size(stk)-1] == asteroids[i] * -1) {
                    stk.pop_back();
                    cont = true; 
                    break;
                }

                stk.pop_back();
            }

            if (!cont) stk.push_back(asteroids[i]);
        }

        return stk;
    }
};
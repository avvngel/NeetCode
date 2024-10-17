#include <unordered_set>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_set<char> seen;
        int l = 0, max_len = 0;
        for (int r = 0; r < s.size(); ++r){
            if (seen.find(s[r]) != seen.end()){
                while (s[l] != s[r]){
                    seen.erase(s[l]);
                    ++l;
                }
                ++l;
            }
            else{
                seen.insert(s[r]);
                max_len = std::max(r - l + 1, max_len);
            }
        }
        return max_len;
    }
};


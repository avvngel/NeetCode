#include <string>
#include <algorithm>
class Solution {
public:
    string longestPalindrome(string s) {
        int max_len = 0;
        std::string max_pali{};
        for ( int i = 0; i < s.size(); ++i ){
            int l{i}, r{i};
            while (0 <= l && r < s.size() && s[l] == s[r]){
                --l;
                ++r;
            }

            if (max_len < r - l - 1){
                max_len = r - l - 1;
                max_pali = s.substr(l+1, max_len);
            }

            l = i;
            r = i+1;
            while (0 <= l && r < s.size() && s[l] == s[r]){
                --l;
                ++r;
            }
            
            if (max_len < r - l - 1){
                max_len = r - l - 1;
                max_pali = s.substr(l+1, max_len);
            }
        }
        return max_pali;
    }
};


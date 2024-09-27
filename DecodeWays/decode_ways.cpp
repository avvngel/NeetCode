#include <array>
#include <algorithm>
class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0')
            return 0;
        std::array<int, 4> prev{1, 1, 0, 0};
        int count{};
        for (int i = 1; i < s.size(); ++i){
            if ( (s[i-1] == '1' && s[i] != '0') ||
                 (s[i-1] == '2' && '0' < s[i] && s[i] < '7') ){
                count = prev[0] + prev[1];
            }
            else if ( (s[i-1] == '1' || s[i-1] == '2') && s[i] == '0' ){
                count = prev[1];
            }
            else if ( (s[i-1] != '1') && s[i] != '0' ){
                
                count = prev[0];
            }
            else {
                return 0;
            }

            prev[3] = prev[2];
            prev[2] = prev[1];
            prev[1] = prev[0];
            prev[0] = count;
        }
        return prev[0];
    }
};


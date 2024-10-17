#include <unordered_map>
#include <tuple>
#include <cstdint>
class Solution {
public:
    using Idx = std::uint16_t;
    using Key = std::uint64_t;
    using Memo = std::unordered_map<Key, bool>;
    int idx_width = sizeof(Idx)*8;
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size())
            return false;
        Memo memo;
        return dfs(0, 0, 0, s1, s2, s3, memo);
    
    }

    bool dfs(Idx i, Idx j, Idx k, string& s1, string& s2, string& s3, Memo& memo){
        Key key = (static_cast<Key>(i) << idx_width*2) |
                  (static_cast<Key>(j) << idx_width)   |
                   static_cast<Key>(k);
        auto it = memo.find(key);
        if (it != memo.end()){
            return it->second;
        }
        if (i == s1.size() && j == s2.size() && k == s3.size()){
            return true;
        }
        
        memo[key] = false;
        if (i < s1.size() && s1[i] == s3[k]){
            memo[key] = memo[key] || dfs(i+1, j, k+1, s1, s2, s3, memo);
        }
        if (j < s2.size() && s2[j] == s3[k]){
            memo[key] = memo[key] || dfs(i, j+1, k+1, s1, s2, s3, memo);
        }
        return memo[key];
    }
};


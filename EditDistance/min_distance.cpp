#include <unordered_map>
#include <cstdint>
#include <algorithm>

class Solution {
public:
    using Key = std::uint32_t;
    using Idx = Key;
    using Memo = std::unordered_map<Key, int>;
    int shift = 16;

    int minDistance(string word1, string word2) {
        Memo memo;
        return dfs(0, 0, word1, word2, memo);
        
    }

    int dfs(Idx i, Idx j, const string& word1, const string& word2, Memo& memo){
        Key key = (i << shift) | j;
        auto it = memo.find(key);
        if (it != memo.end()){
            return it->second;
        }
        if (i == word1.size() && j == word2.size()){
            return 0;
        }
        if (i == word1.size() ^ j == word2.size()){
            return (word1.size() - i) + (word2.size() - j);
        }
        if (word1[i] == word2[j]){
            memo[key] = dfs(i+1, j+1, word1, word2, memo);
        }
        else
            memo[key] = 1 + std::min({ dfs(i, j+1, word1, word2, memo)
                                     , dfs(i+1, j, word1, word2, memo)
                                     , dfs(i+1, j+1, word1, word2, memo) });
        return memo[key];
    }
};


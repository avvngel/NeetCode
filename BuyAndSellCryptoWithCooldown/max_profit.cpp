#include <unordered_map>
#include <utility>
#include <vector>
#include <algorithm>

using Memo = std::unordered_map<long, int>;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        Memo memo;
        return dfs(0, false, prices, memo);
    }

    int dfs(int i, bool holding_coin, std::vector<int>& prices, Memo& memo){
        long key = static_cast<long>(i) << 1 | static_cast<long>(holding_coin);
        auto it = memo.find(key);

        if (it != memo.end()){
            return it->second;
        }
        if (i >= prices.size()){
            return 0;
        }
        if (holding_coin){
            memo[key] = std::max( dfs(i+2, false, prices, memo) + prices[i]
                                , dfs(i+1, true, prices, memo) );
        }
        else{
            memo[key] = std::max( dfs(i+1, true, prices, memo) - prices[i]
                                , dfs(i+1, false, prices, memo) );
        }
        return memo[key];
        }
};


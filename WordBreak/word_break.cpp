class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<int> dp(s.size()+1, false);
        dp[0] = true;
        for (int i = 1; i < s.size()+1; ++i){
            for (auto& word : wordDict){
                if (word.size() <= i && s.substr(i-word.size(), word.size()) == word){
                    dp[i] = dp[i] || dp[i - word.size()];
                if (dp[i]) 
                    break;
                }
            }
        }
        return dp[dp.size()-1];
    }
};


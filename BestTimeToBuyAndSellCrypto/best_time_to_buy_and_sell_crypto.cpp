#include <algorithm>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy_price = 101, profit = 0;
        for (int price : prices){
            if (price < buy_price){
                buy_price = price;
            }
            else{
                profit = std::max(profit, price - buy_price);
            }
        }
        return profit;
    }
};


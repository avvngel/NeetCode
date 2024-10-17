#include <algorithm>
#include <iostream>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        vector<vector<int>> triplets;
        for (int i = 0; i < nums.size()-2; ++i){
            if (0 < i && nums[i] == nums[i-1]){
                continue;}

            int l = i+1, r = nums.size()-1;
            std::cout << nums[i] << std::endl;
            while (l < r){
                if (-nums[i] < nums[l] + nums[r])
                    --r;
                else if (nums[l] + nums[r] < -nums[i])
                    ++l;
                else{
                    triplets.push_back({nums[l], nums[i], nums[r]});
                    ++l;
                    --r;
                    while (l < r && nums[l] == nums[l-1])
                        ++l;
                }
            }
        }
        return triplets;
    }
};


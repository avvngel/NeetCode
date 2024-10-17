class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int l = 0, r = matrix.size()*matrix[0].size()-1;
        while (l <= r){
            int mid = l + (r - l)/2;
            int row = mid/matrix[0].size(), col = mid%matrix[0].size();
            if (matrix[row][col] < target){
                l = mid + 1;
            }
            else if (target < matrix[row][col]){
                r = mid - 1;
            }
            else{
                return true;
            }
        }   
        return false;
    }
};


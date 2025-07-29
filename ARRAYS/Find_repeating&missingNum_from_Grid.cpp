class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        unordered_map<int, int>mpp;
        int n = grid.size();
        for(int i = 0 ; i <n ; i++){
            for(int j=0; j < grid[i].size();  j++){
                mpp[grid[i][j]]++;
                
            }
        }
        int a = -1;
        int b = -1;

        for(int i= 1; i<= n * n ; i++){
            if(mpp[i] == 2)a= i;
            if(mpp[i] ==0)b =i;
             
        }
        return {a,b};
    }
};
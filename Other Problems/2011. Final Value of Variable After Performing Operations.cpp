class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int X = 0;
        for (int i=0; i<operations.size(); i++){
            X = X + (44 - operations[i][1]);
        }
        return X;
    }
};
class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        int size = score.size();
        int j;
        vector<int> key;
        for (int i = 1; i < size; i++){
            j = i;
            key = score[i];
            while (j > 0 && key[k] > score[j-1][k]){
                score[j] = score[j-1];
                j--;
            }
            score[j] = key; 
        }
        return score;
    }
};


// Found another solution in the discussion section

// The function works as follows:
// It uses Python's built-in sorted() function to sort the list A. 
// The sorted() function returns a new list that is ordered according to the criteria specified by its key parameter.
// The key parameter is a function that will be called on each element of the list A before making comparisons. 
// In this case, a lambda function is used as the key function.
// The lambda function lambda a: -a[k] takes an element a (which, in this context, 
// is one of the inner lists or tuples from A) and returns the value at the k-th index within a, negated (-a[k]).
// Negating the k-th value (-a[k]) means that the sorting will be done in descending order. 
// Without the negation, the sorted() function would sort the elements in ascending order based on the k-th value.
// Finally, the sorted() function returns the newly sorted list.

// class Solution:
//     def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
//         return sorted(score, key = lambda a: -a[k])
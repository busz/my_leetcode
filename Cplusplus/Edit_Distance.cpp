/*
Edit_Distance.cpp

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
*/

class Solution {
public:
    int minDistance(string word1, string word2) {
        if(word1.size() == 0 || word2.size() == 0)
            return max(word1.size() , word2.size());
        vector<vector<int> > arr(word2.size() + 1 , vector<int>(word1.size() + 1,0));
        for(int i = 1; i < word1.size() +1 ; i++)
        {
            arr[0][i] = i;
        }
        for(int i = 1 ; i < word2.size() + 1 ; i++)
        {
            arr[i][0] = i;
        }
        for(int x = 1 ; x < word2.size() + 1 ; x++)
        {
            for(int y = 1 ; y < word1.size() + 1 ; y++)
            {
                int tmp = min(arr[x-1][y] + 1 , arr[x][y-1] + 1);
                int addStep = 0;
                if(word2[x-1] != word1[y-1])
                    addStep = 1;
                arr[x][y] = min(tmp , arr[x-1][y-1] + addStep);
            }
        }
        return arr[word2.size()][word1.size()];
    }
};

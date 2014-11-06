/*
Leetcode : Longest_Palindromic_Substring.cpp
Given a string S, find the longest palindromic substring in S.

You may assume that the maximum length of S is 1000, and there

exists one unique longest palindromic substring.


Manacher's ALGORITHM

*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        string newS = "#";
        for( int i = 0 ; i < s.size() ; i++)
        {
            newS.push_back(s[i]);
            newS.push_back('#');

        }

        vector<int> p(newS.size() , 1);
        int id = 0;
        int maxId = 0;
        int maxV = 0;
        int rightE = 0;
        for(int i = 0 ; i < newS.size() ; i++)
        {
            if (rightE > i)
            {
                p[i] = min(rightE - i , p[2*id - i]);
            }
            while(i+p[i]<newS.size() && i-p[i]>=0 && newS[i+p[i]] == newS[i-p[i]])
                p[i]++;
            if(i+p[i]>rightE)
            {
                rightE = i+p[i];
                id = i;

            }
            if(p[i]>maxV)
            {
                maxId = i;
                maxV = p[i];
            }

        }
        string result = "";
        for(int i = maxId - maxV + 1 ; i < maxId+maxV ; i++ )
        {
            if (newS[i]!='#')
                result.push_back(newS[i]);
        }
        return result;

    }
};

int main()
{
    Solution test = Solution();
    string s = "daomdukomcayjwgmmetypncdeixarhbectjcwftjjtwjrctixtrse\
    hegwlfotpljeeqhntacfihecdjysgfmxxbjfeskvvfqdoedfxriujnoeteleftsjgd\
    sagqvcgcdjbxgmguunhbjxyajutohgbdwqtjghdftpvidkbftqbpeahxbfyamonazvu\
    bzirhqseetaneptnpjbtrtitttxsyjckjvwtrmuwgidkofvobrwrffzrpnxbectsydbv\
    swstfiqranjzhsebjnmprjoirqkgttahrivkcjtitdcpohwwerwgrdivqbltfnigavydx\
    pmitttjjzyrmpaptkczzgnsovebvxezkkovgqegctxacvjfqwtiycnhartzczcgosiquhm\
    dbljjzyrnmffcwnkyzytnsvyzayrieqyrfpxintbbiyrawxlguzaisedwabpzvevlejadzt\
    uclcpwvonehkhknicdksdcnjfaoeaqhcdkdtywilwewadcnaprcasccdcnvdgjdqirrsqwzh\
    qqorlhbgpelpupdvuynzybcqkffnnpocidkkigimsa";
    cout<<test.longestPalindrome(s)<<endl;
    return 0;
}

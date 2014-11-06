/*
leetcode : Evaluate_Reverse_Polish_Notation.cpp

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

*/
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include<stdlib.h>
using namespace std;

class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        stack<int> comStack;
        comStack.push(atoi(tokens[0].c_str()));
        for( int i = 1 ; i < tokens.size() ; i++)
        {
            if(tokens[i] == "+")
            {
                vector<int> numVec = getNumber(comStack);
                comStack.push(numVec[0]+numVec[1]);
            }
            else if(tokens[i] == "-")
            {
                vector<int> numVec = getNumber(comStack);
                comStack.push(numVec[0]-numVec[1]);
            }
            else if(tokens[i] == "*")
            {
                vector<int> numVec = getNumber(comStack);
                comStack.push(numVec[0]*numVec[1]);
            }
            else if(tokens[i] == "/")
            {
                vector<int> numVec = getNumber(comStack);
                
                comStack.push(numVec[0]/numVec[1]);
            }
            else
            {
                comStack.push(atoi(tokens[i].c_str()));
            }
        }
        return comStack.top();
    }
    vector<int> getNumber(stack<int> &comStack)
    {
        vector<int> numVec;
        int num2 = comStack.top();
        comStack.pop();
        numVec.push_back(comStack.top());
        numVec.push_back(num2);
        comStack.pop();
        return numVec;

    }

    int checkNumber(string s)
    {
        int ascii = s[0];
        if( (ascii > 47 && ascii < 58) || (s.size()>1 && ( s[0] == '+' || s[0] == '-' ) ) )
            return true;
        else
            return false;
    }
};


int main()
{
    Solution test = Solution();

    vector<string> tokens;
    tokens.push_back("0");
    tokens.push_back("3");
    tokens.push_back("/");
    cout<<test.evalRPN(tokens)<<endl;

}

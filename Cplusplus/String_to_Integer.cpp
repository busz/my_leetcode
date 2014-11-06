/*
Leetcode : String_to_Integer.cpp

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,

please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given

input specs). You are responsible to gather all the input requirements up front.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the

first non-whitespace character is found. Then, starting from this character, takes

an optional initial plus or minus sign followed by as many numerical digits as possible,

and interprets them as a numerical value.

The string can contain additional characters after those that form the integral

number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral

number, or if no such sequence exists because either str is empty or it contains

only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct

value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648)

is returned.
*/

#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

class Solution {
public:
    int atoi(const char *str) {
        unsigned int MAX = (1<<31) ;
        int length = strlen(str);
        int num = 0;
        unsigned int sum = 0;
        int pos = 0;
        while(pos < length && str[pos] == ' ')
            pos++;
        if(pos == length)
            return sum;
        int flag = 1;
        if(str[pos] == '-')
        {
            flag = -1;
            pos++;
        }
        else if(str[pos] == '+')
        {
            pos++;
        }

        for(int i = pos ; i < length ; i++)
        {
            if(str[i] >= '0' && str[i] <= '9')
            {
                if(num == 10)
                {
                    sum = MAX;
                    break;
                }
                unsigned int tmp = sum*10 + int(str[i] - '0');
                num++;
                if(tmp > MAX )
                {
                    sum = MAX;
                    break;
                }

                sum = tmp;
            }
            else if(str[i] == '-' || str[i] == '+')
                return 0;
            else
                break;
        }

        if(flag == 1)
        {
            if(sum == MAX)
                sum = sum - 1;
        }
        int result = int(sum)*flag;
        return result;
    }
};

int main()
{
    Solution test = Solution();
    char *str = "    10522545459";
    cout<<test.atoi(str)<<endl;
}

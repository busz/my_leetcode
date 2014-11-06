'''
Created on 2014.8.11

Leetcode : ZigZag_Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 

like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        num = len(s)
        cols = len(s)/(nRows*2 - 2)*2 + 1
        arr = [ [ '' for i in range(cols)] for i in range(nRows) ]
        pos = 0
        row = 0
        col = 0
        step = 1
        while pos < num:
            if row == nRows:
                row = nRows - 2
                col = col + 1
                step = -1
            if row == 0 and step == -1:
                col = col + 1
                step = 1
                
            arr[row][col] = s[pos]
            pos = pos + 1
            row = row + step
            
        r = ''
        for i in range(nRows):
            for j in range(cols):
                if arr[i][j] != '':
                    r = r + arr[i][j]
        return r
test  = Solution()
s = "PAYPALISHIRING"
s = ''
nRows = 1
print test.convert(s, nRows)

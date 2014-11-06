'''
Created on 2014-8-15

Leetcode : Text_Justification

Given an array of words and a length L, format the text such that each line has

 exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as

 you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the 

number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is 

inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        r = []
        
        
        while words:
            length = 0
            pos = 0
            while pos < len(words) and length + len(words[pos]) + pos <= L:
                
                length += len(words[pos])
                pos = pos + 1
            
            if pos == 1:
                newline = words[0] + ' '*(L-len(words[0]) )
                r.append(newline)
                words = words[1:]
            else:
                if pos == len(words):
                    newline = ' '.join(words)
                    newline += ' '*(L - len(newline))
                    words = words[pos:]
                    r.append(newline)
                
                else:   
                    space = (L - length)/(pos - 1)
                    remain = (L - length)%(pos - 1)
                    newline = words[0]
                    for i in range(1,pos):
                        newline += ' '*space
                        if remain:
                            newline += ' '
                            remain -= 1
                        newline += words[i]
                    words = words[pos:]
                    r.append(newline)
        return r

test = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
words = ["a","b","c","d","e"]
L = 1
words = ["What","must","be","shall","be."]
L = 12
print test.fullJustify(words, L)

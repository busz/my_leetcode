'''
Created on 2014.7.24

Leetcode : Simplify Path

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.

Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".


'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        
        
        
        while len(path) > 0 and path[len(path)-1] == '/':
            path = path[:len(path)-1]
        
        if len(path) == 0:
            return '/'
           
        num = len(path)
        stack = [];
        
        pos = 1
        while path[pos] == '/':
            pos = pos+1;
            
        start = pos;
        
        while pos <= num-1:
            if path[pos] == '/':
                stack.append(path[start:pos]);
                pos = pos + 1;
                while path[pos] == '/':
                        pos = pos+1;
                start = pos ;
                
            elif path[pos] == '.' :
                if pos + 1 == num :
                    break;
                elif path[pos+1] == '/':
                    pos = pos + 2;
                    while path[pos] == '/':
                        pos = pos+1;
                    start = pos
                elif path[pos+1] == '.':
                    if pos + 2 < num and path[pos+2]!='/':
                        pos = pos+2
                        while pos < num and path[pos] == '.':
                            pos=pos+1
                        continue
                    if len(stack) != 0:
                        stack.pop(len(stack)-1);
                    pos = pos + 3
                    while pos < num and path[pos] == '/' :
                        pos = pos+1;
                    start = pos
                else:
                    pos = pos +1
                    #start = pos
            else:
                pos = pos+1
        stack.append(path[start:pos])
        
        sPath = '/'
        for name in stack:
            if name != '' :
                sPath = sPath  + name + '/';
        if len(sPath)>1:
            sPath = sPath[:-1];  
        return sPath;
    
test = Solution();
path = "/."
print test.simplifyPath(path)

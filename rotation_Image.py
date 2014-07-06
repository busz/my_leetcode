# -*- coding:utf-8 -*-
'''
Created on 2014��7��6��

Leetcode :

Problem : 
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?


@author: xqk
'''
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if matrix == None:
            return None;
        r = [ [0 for i in range(len(matrix[0]) ) ] for i in range(len(matrix) ) ];
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                r[col][n-1-row] = matrix[row][col];
        return r

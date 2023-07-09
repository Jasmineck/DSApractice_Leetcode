"""Link:https://leetcode.com/problems/rotate-image/
SOLVED
Q:You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
 #CODE
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Transpose of a matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix [i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #Reverse of every row
        for x in range(len(matrix)):
            matrix[x]=matrix[x][::-1]
        
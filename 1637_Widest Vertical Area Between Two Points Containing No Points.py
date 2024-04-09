"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3

"""

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        max_delta = 0

        for idx, num in enumerate(points):
            arr.append(num[0])

        arr.sort()

        for i in range(1, len(arr)):
            max_delta = max(max_delta, arr[i] - arr[i-1])

        return max_delta
"""
  @Author       : Liujianhan
  @Date         : 20/8/16 0:10
  @FileName     : 733.图像渲染.py
  @ProjectName  : leetcode_in_python
  @Description  : 有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

    给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

    为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

    最后返回经过上色渲染后的图像。

    示例 1:

    输入:
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    输出: [[2,2,2],[2,2,0],[2,0,1]]
    解析:
    在图像的正中间，(坐标(sr,sc)=(1,1)),
    在路径上所有符合条件的像素点的颜色都被更改成2。
    注意，右下角的像素没有更改为2，
    因为它不是在上下左右四个方向上与初始点相连的像素点。
    注意:

    image 和 image[0] 的长度在范围 [1, 50] 内。
    给出的初始点将满足 0 <= sr < image.length 和 0 <= sc < image[0].length。
    image[i][j] 和 newColor 表示的颜色值在范围 [0, 65535]内。
 """
from typing import List


class Solution:
    # 112ms, 13.9MB
    @staticmethod
    def flood_fill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        currColor = image[sr][sc]

        def dfs(x: int, y: int):
            if image[x][y] == currColor:
                image[x][y] = newColor
                for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                        dfs(mx, my)

        if currColor != newColor:
            dfs(sr, sc)
        return image


if __name__ == '__main__':
    print(Solution.flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))

# Write a function that takes in the image and returns the coordinates of the rectangle of 0’s -- either top-left and bottom-right; or top-left, width, and height.

# Sample output:

# x: 3, y: 2, width: 3, height: 2
# 2 3 3 5
# 3,2 5,3 -- it’s ok to reverse columns/rows as long as you’re consistent
image = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
def solution(image):
    def dfs1(i, j, width):
        # To calculate the width of the rectangle
        if 0 <= j < n and image[i][j] == 0:
            width += dfs1(i, j + 1, width)
            # print("Hi, width:", width)

        return width

    def dfs2(i, j, height):
        # To calculate the height of the rectangle
        if 0 <= i < m and image[i][j] == 0:
            height += dfs2(i + 1, j, height)
            # print("see height:",height)
        return height

    width = 1
    height = 1
    m = len(image)
    n = len(image[0])
    for i in range(m):
        for j in range(n):
            if image[i][j] == 0:
                # See the sample output #2 where the coordinates of the top-left cell and coordinates of the bottom right-cell are returned
                print(i, j, i + dfs2(i, j, height) - 2, j + dfs1(i, j, width) - 2)
                #return i, j, i + dfs2(i, j, height) - 2, j + dfs1(i, j, width) - 2
                exit()
print(solution(image))

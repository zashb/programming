"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limit" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
"""
dp = True
if not dp:
    def get_path(maze):
        if len(maze) == 0 or len(maze[0]) == 0:
            return False
        path = []
        if find_path(maze, len(maze) - 1, len(maze[0]) - 1, path):
            return path


    def find_path(maze, r, c, path):
        if r < 0 or c < 0 or not maze[r][c]:
            return False
        is_origin = r == 0 and c == 0
        if is_origin or find_path(maze, r - 1, c, path) or find_path(maze, r, c - 1, path):
            path.append((r, c))
            return True
        return False
else:
    def get_path(maze):
        if len(maze) == 0 or len(maze[0]) == 0:
            return False
        path = []
        failed_points = set()
        if find_path(maze, len(maze) - 1, len(maze[0]) - 1, path, failed_points):
            return True


    def find_path(maze, r, c, path, failed_points):
        if r < 0 or c < 0 or not maze[r][c]:
            return False
        is_origin = r == 0 and c == 0
        point = (r, c)
        if point in failed_points:
            return False
        if is_origin or find_path(maze, r - 1, c, path, failed_points) or find_path(maze, r, c - 1, path,
                                                                                    failed_points):
            path.append((r, c))
            return True
        failed_points.add((r, c))
        return False

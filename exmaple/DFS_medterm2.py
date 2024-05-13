output = """
+---+---+---+---+---+---+---+
|   | X | X | X | X |   | X |
+---+---+---+---+---+---+---+
|   | X | X |   |   | X |   |
+---+---+---+---+---+---+---+
|   |   |   |   | X | X |   |
+---+---+---+---+---+---+---+
|   | X |   | X | X | X | X |
+---+---+---+---+---+---+---+
|   | X | X | X | X | X |   |
+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+
"""

#output = '\n+---+---+---+---+---+---+\n| * | X |   | X | X |   |\n+---+---+---+---+---+---+\n| * | * |   | X | X | X |\n+---+---+---+---+---+---+\n| X | * | X | X | X | X |\n+---+---+---+---+---+---+\n| X | * | * | * | * | * |\n+---+---+---+---+---+---+\n| X |   | X |   | X | * |\n+---+---+---+---+---+---+\n'

def DFS_medterm2(output, count_str=' X '):
    lines = output.strip().split('\n')

    matrix = [line.split('|')[1:-1] for line in lines if '|' in line]
    len_ = [len(i) for i in matrix]
    rows_len_ = max(len_)
    columns_len_ = len(matrix)

    count_ = sum([i.count(count_str) for i in matrix])

    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

    def is_valid(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] != ' X ' and not visited[row][col]

    def dfs(row, col):
        visited[row][col] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col):
                dfs(new_row, new_col)

    start = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != ' X ':
                start = (i, j)
                break
        if start:
            break
    if not start:
        return False  # 沒有找到起點
    dfs(start[0], start[1])
    return (max(len_) == min(len_), rows_len_, columns_len_), count_, visited[-1][-1]

print(DFS_medterm2(output))
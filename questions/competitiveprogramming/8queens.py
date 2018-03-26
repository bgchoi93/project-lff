import sys

def validate(board):
    count = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if (board[i][j]):
                count = count + 1
                if not visit(i,j, board):
                    return False
    return count == 8

def visit(i, j, visited):
    return \
    visit_up(i - 1, j, visited) and \
    visit_down(i + 1, j, visited) and \
    visit_left(i, j - 1, visited) and \
    visit_right(i, j + 1, visited) and \
    visit_downleft(i + 1, j - 1, visited) and \
    visit_downright(i + 1, j + 1, visited) and \
    visit_upleft(i - 1, j - 1, visited) and \
    visit_upright(i - 1, j + 1, visited)

def visit_up(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if visited[i][j]:
        return False
    else:
        return visit_up(i-1, j, visited)

def visit_down(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_down(i+1, j, visited)

def visit_left(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_left(i, j-1, visited)

def visit_right(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_right(i, j+1, visited)

def visit_upright(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_upright(i-1, j+1, visited)

def visit_upleft(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_upleft(i-1, j-1, visited)

def visit_downright(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_downright(i+1, j+1, visited)

def visit_downleft(i,j, visited):
    if (i < 0) or (i > 7) or (j < 0) or (j > 7):
        return True
    if (visited[i][j]):
        return False
    else:
        return visit_downleft(i+1, j-1, visited)

def main():
    board = []
    for i in range(0, 8):
        line = sys.stdin.readline()
        row = []
        for j in range(0, 8):
            row.append(line[j] == '*')
        board.append(row)
    if (validate(board)):
        print("valid")
    else:
        print("invalid")


if __name__ == "__main__": main()

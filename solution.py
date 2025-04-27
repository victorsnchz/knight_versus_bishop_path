from collections import deque

def main():
    count = min_jumps(8, 0, 0, 7, 7, 1, 1)
    print(count)

def min_jumps(n: int, 
              start_row: int, start_col: int, 
              end_row: int, end_col: int,
              bishop_row: int, bishop_col: int):

    def make_board_with_bishop():
        
        board_with_bishop = [[1] * n for _ in range(n)]
        board_with_bishop[bishop_row][bishop_col] = 2
        
        for row_move, col_move in bishop_moves:
             
            next_row = bishop_row + row_move
            next_col = bishop_col + col_move
            while min(next_row, next_col) >= 0 and max(next_row, next_col) < n:
                board_with_bishop[next_row][next_col] = 0
                next_row -= row_move
                next_col -= col_move

        return board_with_bishop

    if (start_row, start_col) == (end_row, end_col): return 0

    knight_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                    (2, 1), (2, -1), (-2, 1), (-2, -1)]

    bishop_moves = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    board_no_bishop = [[1] * n for _ in range(n)]    
    board_with_bishop = make_board_with_bishop()

    boards = (board_with_bishop, board_no_bishop)
    
    board_flag = 1 if (start_row, start_col) == (bishop_row, bishop_col) else 0
    
    visited = set()
    queue = deque()
    queue.append((start_row, start_col, board_flag))
    next_moves = deque()
    moves_count = 1

    while queue:
        row, col, board_flag = queue.popleft()
        
        for row_move, col_move in knight_moves:
            next_row = row + row_move
            next_col = col + col_move

            if (next_row, next_col) == (end_row, end_col): return moves_count
            
            if (min(next_row, next_col) >= 0 and
                max(next_row, next_col) < n and
                (next_row, next_col) not in visited and
                boards[board_flag][next_row][next_col]
                ):

                visited.add((next_row, next_col))
                if boards[board_flag][next_row][next_col] == 2:
                    next_moves.append((next_row, next_col, 1))
                else:
                    next_moves.append((next_row, next_col, board_flag))

        if not queue:
            queue = next_moves
            next_moves = deque()
            moves_count += 1
        

    return -1

if __name__ == '__main__':
    main()

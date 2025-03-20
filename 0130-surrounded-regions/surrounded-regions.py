class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
    
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # down, up, right, left
        
        # Helper function for DFS
        def mark_unsurrounded(r, c):
            # Check boundaries and if current cell is 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark as temporary value to indicate this 'O' is not surrounded
            board[r][c] = 'T'
            
            # Recursively check adjacent cells using directions array
            for dr, dc in directions:
                mark_unsurrounded(r + dr, c + dc)
        
        # Check all border cells first - any 'O's on border cannot be surrounded
        for r in range(rows):
            mark_unsurrounded(r, 0)           # Left border
            mark_unsurrounded(r, cols-1)      # Right border
        
        for c in range(cols):
            mark_unsurrounded(0, c)           # Top border
            mark_unsurrounded(rows-1, c)      # Bottom border
        
        # Step 2: Process all cells - convert remaining 'O's to 'X' (as they are surrounded)
        # and restore temporarily marked cells back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    # These 'O's are surrounded, so capture them
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    # Restore unsurrounded 'O's
                    board[r][c] = 'O'
        
        # No return needed as we've modified the board in-place
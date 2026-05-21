class Solution:
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_row(board) and self.check_column(board) and self.check_sub_box(board)
        
    def check_row(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.check_list(row):
                return False
        return True

    def check_list(self, subset: list) -> bool:
        row = [x for x in subset if x != "."]
        if not len(set(row)) == len(row):
            return False
        return True

    def check_column(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            col = []
            for row in board:
                col.append(row[i])
            if not self.check_list(col):
                return False
        return True
    
    def check_sub_box(self, board: List[List[str]]) -> bool:
        print("Checking sub boxes.")
        i = j = 0

        for i in range(0, 8, 3):
            box = []
            for j in range(9):
                box += board[j][i: i + 3]
                if (j+1)%3 == 0:
                    if not self.check_list(box):
                        return False
                    box = []
        return True
                    
                 
            

        

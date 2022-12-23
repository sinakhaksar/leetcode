

class Solution:
    def diagonalSum(self, mat: list) -> int:
        s = 0 
        rounds = 0 
        while True :
            i = 0 
            for row in mat :
                s += row[i]
                i += 1
            if rounds == 1 :
                if len(mat) % 2 != 0 :
                    avr = len(mat) // 2
                    s -= mat[avr][avr]
                return s 
            mat = list(map(lambda row: row[::-1], mat))
            rounds += 1 
        return s
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        negatives = zeroes = total = 0
        minnum = inf
        for row in matrix:
            for cell in row:
                if cell < 0:
                    negatives += 1
                    minnum = min(minnum, -cell)
                    total -= cell
                elif cell > 0:
                    minnum = min(minnum, cell)
                    total += cell
                else:
                    zeroes += 1
        
        if negatives % 2:
            if zeroes:
                return total
            else:
                return total - (2 * minnum)
        else:
            return total

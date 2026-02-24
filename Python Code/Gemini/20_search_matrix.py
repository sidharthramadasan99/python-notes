#20_search_matrix.py
#
#
#

def search_matrix(matrix, target):
    if not matrix: return False 
    rows, cols = len(matrix), len(matrix[0])
    l, r=0, rows * cols -1 

    while l <= r:
        mid = (l + r) // 2
        # Virtual 1D to 2D mapping
        mid_val = matrix[mid // cols][mid % cols]
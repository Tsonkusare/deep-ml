def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == 'row':
        return [sum(row) / len(row) for row in matrix]
        
    elif mode == 'column':
        # Calculate the mean of each column
        num_rows = len(matrix)
        num_cols = len(matrix[0]) if num_rows > 0 else 0
        result = []
        
        for col in range(num_cols):
            col_sum = 0.0
            for row in range(num_rows):
                col_sum += matrix[row][col]
            result.append(col_sum / num_rows)
            
        return result
        
    return []
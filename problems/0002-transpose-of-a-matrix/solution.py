def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    ans = []
    answe = []
    for x in range(len(a[0])):
        for i in range(len(a)):
            answe.append(a[i][x])
        ans.append(answe)
        answe = []
    return ans
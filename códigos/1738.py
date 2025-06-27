class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0]) 
        xor_colunas = [0] * n  
        resultados = []

        for i in range(m):
            xor_linha = 0  
            for j in range(n):
                xor_colunas[j] ^= matrix[i][j]  
                xor_linha ^= xor_colunas[j]     
                resultados.append(xor_linha)    

        return sorted(resultados, reverse=True)[k - 1]
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, otherMatrix):
        if (len(self.matrix) != len(otherMatrix.matrix) or len(self.matrix[0]) != len(otherMatrix.matrix[0])):
            return
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] += otherMatrix.matrix[i][j]
    
    def sub(self, otherMatrix):
        if (len(self.matrix) != len(otherMatrix.matrix) or len(self.matrix[0]) != len(otherMatrix.matrix[0])):
            return
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] -= otherMatrix.matrix[i][j]
    
    def mult(self, otherMatrix):
        if len(self.matrix[0]) != len(otherMatrix.matrix):
            raise ValueError("Matrices cannot be multiplied")
        
        result = [[0 for _ in range(len(otherMatrix.matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(otherMatrix.matrix[0])):
                for k in range(len(otherMatrix.matrix)):
                    result[i][j] += self.matrix[i][k] * otherMatrix.matrix[k][j]
        
        self.matrix = result

matrixA = Matrix([[1, 6, 8], 
                  [2, 3, 7]])
print("matrix a: ", matrixA.matrix)

matrixB = Matrix([[4, 2, 5], 
                  [9, 5, 9]])
print("matrix b:", matrixB.matrix)

matrixC = Matrix([[1],[2]])
print("matrix c:", matrixC.matrix)

# matrixA.add(matrixB)
# print("matrixA + matrixB = ", matrixA.matrix)

# matrixA.add(matrixC)
# print(matrixA.matrix)

# matrixA.sub(matrixB)
# print("matrixA - matrixB = ", matrixA.matrix)

matrixA.mult(matrixB)
print("matrix a * matrix b = ", matrixA.matrix)

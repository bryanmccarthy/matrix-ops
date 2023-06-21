class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def add(self, otherMatrix):
        if (len(self.matrix) != len(otherMatrix.matrix) or len(self.matrix[0]) != len(otherMatrix.matrix[0])):
            raise ValueError("Matrices cannot be added due to shape mismatch")
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] += otherMatrix.matrix[i][j]
    
    def sub(self, otherMatrix):
        if (len(self.matrix) != len(otherMatrix.matrix) or len(self.matrix[0]) != len(otherMatrix.matrix[0])):
            raise ValueError("Matrices cannot be subtracted due to shape mismatch")
        
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] -= otherMatrix.matrix[i][j]
    
    def mult(self, otherMatrix):
        if len(self.matrix[0]) != len(otherMatrix.matrix):
            raise ValueError("Matrices cannot be multiplied due to shape mismatch")
        
        result = [[0 for _ in range(len(otherMatrix.matrix[0]))] for _ in range(len(self.matrix))]

        for i in range(len(self.matrix)):
            for j in range(len(otherMatrix.matrix[0])):
                for k in range(len(otherMatrix.matrix)):
                    result[i][j] += self.matrix[i][k] * otherMatrix.matrix[k][j]
        
        self.matrix = result

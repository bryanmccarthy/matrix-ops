import unittest
from main import Matrix

class TestMatrix(unittest.TestCase):
    def test_add(self):
        a = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Matrix([[9, 8, 7], [6, 5, 4]])
        a.add(b)
        self.assertEqual(a.matrix, [[10, 10, 10], [10, 10, 10]])
    
    def test_sub(self):
        a = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Matrix([[9, 8, 7], [6, 5, 4]])
        a.sub(b)
        self.assertEqual(a.matrix, [[-8, -6, -4], [-2, 0, 2]])
    
    def test_mult(self):
        a = Matrix([[1, 2, 3], [4, 5, 6]])
        b = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        a.mult(b)
        self.assertEqual(a.matrix, [[30, 24, 18], [84, 69, 54]])
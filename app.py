from flask import Flask, jsonify
import unittest

app = Flask(__name__)

def max_in_row_min_in_col(matrix):
    result = set()
    for i in range(len(matrix)):
        max_val = max(matrix[i])
        max_col = matrix[i].index(max_val)
        if all(matrix[j][max_col] >= max_val for j in range(len(matrix))):
            result.add(max_val)
    return list(result)
  
  
class TestMaxInRowMinInCol(unittest.TestCase):
    def test_case1(self):
        matrix = [[5, 16, 20], [9, 11, 18], [15, 16, 17]]
        expected = [17]
        self.assertEqual(max_in_row_min_in_col(matrix), expected)

    def test_case2(self):
        matrix = [[100, 60, 20, 50], [70, 80, 10, 90], [10, 50, 44, 30]]
        expected = [50]
        self.assertEqual(max_in_row_min_in_col(matrix), expected)

        
@app.route('/')
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxInRowMinInCol)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return jsonify(result=result.wasSuccessful())

if __name__ == '__main__':
    app.run()
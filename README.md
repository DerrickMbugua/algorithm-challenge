## Algorithm Challenge
Algorithm challenge done in Flask

# To run the app:

flask run

check the terminal and browser 'http://127.0.0.1:5000/'

# Answer to the second question:

b) Time Complexity:

The time complexity of this algorithm is O(m * n^2), where m is the number of rows and n is the number of columns in the matrix. This is because we iterate over each row of the matrix to find the maximum value and its column index, and then we iterate over each element in the same column to check if it is greater than or equal to the maximum value. The worst-case scenario is when all values in the matrix have to be compared, resulting in a time complexity of O(m * n^2).

Space Complexity:

The space complexity of this algorithm is O(m) since we use a set to store the result, which can have at most m elements.

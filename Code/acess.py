# printing the specific coulumn of matrix

import numpy as np

A = np.array([[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]])

print(A[:,3]) # Fourth Column


print(A[:,-1]) # Last Column (4th column in this case)

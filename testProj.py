import numpy as np
R0 = np.random.randn(3,3)
print(R0)
print(np.linalg.det(R0))
import projSO3
R =projSO3.projSO3(R0)
print(R)
print(np.linalg.det(R))
print(R.dot(R.T))



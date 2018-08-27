import numpy as np

def projSO3(R0):
	M	 = R0.T.dot(R0)
	D, U	 = np.linalg.eig(M)
	s	 = np.sign(np.linalg.det(R0))
	d	 = 1./np.sqrt(D)
	d[-1]	*= s
	R	 = R0.dot(U).dot(np.diag(d)).dot(U.T)
	return R

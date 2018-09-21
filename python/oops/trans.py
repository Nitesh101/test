import numpy as np
def transpose(matrix):
	mat = np.array(matrix)
	return mat.transpose()
#if __name__ == "__main__":
print transpose([[1,4,9]])
print transpose([[1,3,5],[2,4,6]])

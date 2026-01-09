import numpy as np
from numpy.linalg import norm

A = np.array([2, 1, 2, 3, 2, 9])
B = np.array([3, 4, 2, 4, 5, 5])

# compute cosine similarity
print(np.dot(A, B))
cosine = np.dot(A, B) / (norm(A, axis=0) * norm(B))
print("Cosine Similarity:", cosine)

A = np.array([[2, 1, 2], [3, 2, 9], [-1, 2, -3]])
B = np.array([3, 4, 2])
print(np.dot(A, B))
cosine1 = np.dot(A, B) / (norm(A) * norm(B))
print(cosine1)
print(norm(B, axis=0))
#print(norm(B, axis=1))
#print("Cosine Similarity:", cosine)

A = np.array([[1, 1, 1], [2, 3, 4]])
B = np.array([[1, 1, 1], [1, 1, 1],[3 ,5, 6]])
#print(np.sum(A * B, axis=1))
print(np.dot(A, B))

print("=="*25)
a = np.array([[1, 4],
              [5, 6]])

b = np.array([[2, 4],
              [5, 2]])

print(np.dot(a, b))
print(np.sum(a * b, axis=1))
"""Source code for Task 9 – Eigenvalues and Eigenvectors."""

import numpy as np

A = np.array([[0.,1.,1.,0.],
              [1.,0.,1.,1.],
              [1.,1.,0.,1.],
              [0.,1.,1.,0.]])
values, vectors = np.linalg.eig(A)
i = np.argmax(np.real(values))
dominant_value = np.real(values[i])
v = np.abs(np.real(vectors[:, i]))
scores = v / v.sum()

print("Dominant eigenvalue:", dominant_value)
for node, score in zip(["A","B","C","D"], scores):
    print(node, round(score, 4))
print("Verification error:",
      np.linalg.norm(A @ np.real(vectors[:,i]) -
                     dominant_value*np.real(vectors[:,i])))

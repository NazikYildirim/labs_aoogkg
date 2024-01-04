import numpy as np
import matplotlib.pyplot as plt

data_file = np.loadtxt('DS1.txt')

alpha = np.deg2rad(10 * (1 + 1))
rotation_matrix = np.array([[np.cos(alpha), -np.sin(alpha)], [np.sin(alpha), np.cos(alpha)]])
translation_vector = np.array([480, 480])

data_transformed = np.dot(data_file - translation_vector, rotation_matrix) + translation_vector

plt.figure(figsize=(9.6, 9.6))

plt.scatter(data_transformed[:, 0], data_transformed[:, 1], color='blue')

plt.savefig('transformed.png')

plt.show()

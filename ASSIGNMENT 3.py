import numpy as np

# ex 1: Saving and Loading with np.save
a1 = np.array([1, 2, 3, 4, 5])
np.save('ex1_array.npy', a1)
load_a1 = np.load('ex1_array.npy')
print("Loaded array from ex1_array.npy:", load_a1)

# ex 2: Saving and Loading with np.savetxt
a2 = np.array([[1.1, 2.2, 3.3],[4.4, 5.5, 6.6]])
np.savetxt('ex2_array.txt', a2, delimiter=',')
load_a2 = np.loadtxt('ex2_array.txt', delimiter=',')
print("Loaded array from ex2_array.txt:", load_a2)

# ex 3: Saving and Loading with np.savez
array3 = np.array([1, 2, 3])
array4 = np.array([4, 5, 6])
np.savez('ex3_arrays.npz', a1=array3, a2=array4)
load_arrays = np.load('ex3_arrays.npz')
load_array3 = load_arrays['a1']
load_array4 = load_arrays['a2']
print("Loaded a1 from ex3_arrays.npz:", load_array3)
print("Loaded a2 from ex3_arrays.npz:", load_array4)

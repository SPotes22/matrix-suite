import numpy as np

def next_power_of_two(n):
    return 1 if n == 0 else 2**(n - 1).bit_length()

def pad_matrix(A, size):
    new_size = next_power_of_two(size)
    padded = np.zeros((new_size, new_size), dtype=A.dtype)
    padded[:size, :size] = A
    return padded

def unpad_matrix(C, size):
    return C[:size, :size]


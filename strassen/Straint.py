import numpy as np
import threading

# -------- Funciones auxiliares --------

def next_power_of_two(n):
    return 1 if n == 0 else 2**(n - 1).bit_length()

def pad_matrix(A, size):
    new_size = next_power_of_two(size)
    padded = np.zeros((new_size, new_size), dtype=A.dtype)
    padded[:size, :size] = A
    return padded

def unpad_matrix(C, size):
    return C[:size, :size]

# --------- Versión secuencial de Strassen ---------

def strassen_secuencial(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B

    mid = n // 2
    A11, A12, A21, A22 = A[:mid,:mid], A[:mid,mid:], A[mid:,:mid], A[mid:,mid:]
    B11, B12, B21, B22 = B[:mid,:mid], B[:mid,mid:], B[mid:,:mid], B[mid:,mid:]

    M1 = strassen_secuencial(A11 + A22, B11 + B22)
    M2 = strassen_secuencial(A21 + A22, B11)
    M3 = strassen_secuencial(A11, B12 - B22)
    M4 = strassen_secuencial(A22, B21 - B11)
    M5 = strassen_secuencial(A11 + A12, B22)
    M6 = strassen_secuencial(A21 - A11, B11 + B12)
    M7 = strassen_secuencial(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))

# --------- Versión paralela de Strassen ---------

def strassen_multiply(A, B):
    umbral=64
    n = A.shape[0]
    if n <= umbral:
        return strassen_secuencial(A, B)

    mid = n // 2
    A11, A12, A21, A22 = A[:mid,:mid], A[:mid,mid:], A[mid:,:mid], A[mid:,mid:]
    B11, B12, B21, B22 = B[:mid,:mid], B[:mid,mid:], B[mid:,:mid], B[mid:,mid:]

    results = [None] * 7

    def thread_fn(i, func, *args):
        results[i] = func(*args)

    threads = [
        threading.Thread(target=thread_fn, args=(0, strassen_multiply, A11 + A22, B11 + B22)),
        threading.Thread(target=thread_fn, args=(1, strassen_multiply, A21 + A22, B11)),
        threading.Thread(target=thread_fn, args=(2, strassen_multiply, A11, B12 - B22)),
        threading.Thread(target=thread_fn, args=(3, strassen_multiply, A22, B21 - B11)),
        threading.Thread(target=thread_fn, args=(4, strassen_multiply, A11 + A12, B22)),
        threading.Thread(target=thread_fn, args=(5, strassen_multiply, A21 - A11, B11 + B12)),
        threading.Thread(target=thread_fn, args=(6, strassen_multiply, A12 - A22, B21 + B22))
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    M1, M2, M3, M4, M5, M6, M7 = results

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))




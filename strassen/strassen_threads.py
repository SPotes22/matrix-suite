import numpy as np
import threading

def strassen_paralelo(A, B):
    n = A.shape[0]
    if n == 1:
        return A * B

    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    results = [None] * 7
    def thread_fn(i, func, *args):
        results[i] = func(*args)

    threads = [
        threading.Thread(target=thread_fn, args=(0, strassen_paralelo, A11 + A22, B11 + B22)),
        threading.Thread(target=thread_fn, args=(1, strassen_paralelo, A21 + A22, B11)),
        threading.Thread(target=thread_fn, args=(2, strassen_paralelo, A11, B12 - B22)),
        threading.Thread(target=thread_fn, args=(3, strassen_paralelo, A22, B21 - B11)),
        threading.Thread(target=thread_fn, args=(4, strassen_paralelo, A11 + A12, B22)),
        threading.Thread(target=thread_fn, args=(5, strassen_paralelo, A21 - A11, B11 + B12)),
        threading.Thread(target=thread_fn, args=(6, strassen_paralelo, A12 - A22, B21 + B22)),
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

